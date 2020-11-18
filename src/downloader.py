from database.social.models import *
import vk
import datetime

VK_API_VERSION = 5.95

def log(message, type=LogType.info, db=True):
    date = datetime.datetime.now()
    if db:
        LogModel.create(**{
                        "message": message,
                        "datetime": date,
                        "type": type
                    })
    print(f"{'Error' if type == LogType.error else 'Info'} on {date}: {message}")


if TaskModel.select().count() == 0:
    log("No active tasks", db=False)
for task in TaskModel.select().iterator():
    session = vk.Session(access_token=task.access_profile.access_token)
    vk_api = vk.API(session, v=VK_API_VERSION)
    for task_source in task.task_sources:
        max = 100
        posts_count = vk_api.wall.get(count=1, owner_id=task_source.source.source_id)["count"]
        if task_source.begin_count == 0:
            task_source.begin_count = posts_count
            task_source.save()
            task.requests_count += 1
            task.save()
            log(f"Source {task_source.source.name}: updated posts count {posts_count}")
            continue
        task_source.count = posts_count - task_source.begin_count
        task_source.save()
        count = task_source.count if task_source.count < max else max
        if count == 0:
            task.requests_count += 1
            task.save()
            log(f"Source {task_source.source.name}: nothing to download")
        downloaded = 0
        wallposts = vk_api.wall.get(count=count, owner_id=task_source.source.source_id, extended=True, fields="all")
        for wallpost in wallposts["items"]:
            same = PostModel.select().where((PostModel.post_id==wallpost["id"]) & (PostModel.owner_id==wallpost["owner_id"]) & (PostModel.from_id==wallpost["from_id"]))
            if not same.exists():    
                post = PostModel.create(**
                {
                    "post_id": wallpost["id"],
                    "owner_id": wallpost["owner_id"],
                    "from_id": wallpost["from_id"],
                    "source": task_source.source,
                    "posted_date": datetime.datetime.fromtimestamp(wallpost["date"]),
                    "text": wallpost["text"]
                })
                if "attachments" in wallpost:
                    for attachment in wallpost["attachments"]:
                        type = AttachmentType.undefined
                        url = ""
                        text = ""
                        title = ""
                        if attachment["type"] == "photo":
                            type = AttachmentType.photo
                            if "photo" in attachment:
                                photo = attachment["photo"]
                                if "sizes" in photo:
                                    sizes = dict()
                                    for size in photo["sizes"]:
                                        sizes[size["type"]] = size["url"]
                                    if "z" in sizes:
                                        url = sizes["z"]
                                    elif "y" in sizes:
                                        url = sizes["y"]
                                    elif "x" in sizes:
                                        url = sizes["x"]
                                    elif "m" in sizes:
                                        url = sizes["m"]
                                    elif "s" in sizes:
                                        url = sizes["s"]
                                elif "photo_2560" in photo:
                                    url = photo["photo_2560"]
                                elif "photo_1280" in photo:
                                    url = photo["photo_1280"]
                                elif "photo_807" in photo:
                                    url = photo["photo_807"]
                                elif "photo_604" in photo:
                                    url = photo["photo_604"]
                                elif "photo_130" in photo:
                                    url = photo["photo_130"]
                                elif "photo_75" in photo:
                                    url = photo["photo_75"]
                                text = photo["text"] if "text" in photo else ""
                        elif attachment["type"] == "video":
                            type = AttachmentType.video
                            if "video" in attachment:
                                video = attachment["video"]
                                title = video["title"] if "title" in video else ""
                                text = video["description"] if "description" in video else ""
                                url = video["url"] if "url" in video else ""
                        elif attachment["type"] == "audio":
                            type = AttachmentType.audio
                            if "audio" in attachment:
                                audio = attachment["audio"]
                                title = audio["title"] if "title" in audio else ""
                                url = audio["url"] if "url" in audio else ""
                        elif attachment["type"] == "doc":
                            type = AttachmentType.document
                            if "doc" in attachment:
                                doc = attachment["doc"]
                                title = doc["title"] if "title" in doc else ""
                                url = doc["url"] if "url" in doc else ""
                        elif attachment["type"] == "link":
                            type = AttachmentType.link
                            if "link" in attachment:
                                link = attachment["link"]
                                title = link["title"] if "title" in link else ""
                                text = link["description"] if "description" in link else ""
                                url = link["url"] if "url" in link else ""
                        PostAttachmentModel.create(**
                        {
                            "post": post,
                            "type": type,
                            "text": text,
                            "title": title,
                            "url": url
                        })
                PostTimestampModel.create(**
                {
                    "downloaded_date": datetime.datetime.now(),
                    "likes_count": wallpost["likes"]["count"] if "likes" in wallpost else 0,
                    "reposts_count": wallpost["reposts"]["count"] if "reposts" in wallpost else 0,
                    "views_count": wallpost["views"]["count"] if "views" in wallpost else 0,
                    "comments_count": wallpost["comments"]["count"] if "comments" in wallpost else 0,
                    "post": post
                })
                log(f"Source {task_source.source.name}: added new post")
                downloaded += 1
            else:
                s = same.get()
                PostTimestampModel.create(**
                {
                    "downloaded_date": datetime.datetime.now(),
                    "likes_count": wallpost["likes"]["count"] if "likes" in wallpost else 0,
                    "reposts_count": wallpost["reposts"]["count"] if "reposts" in wallpost else 0,
                    "views_count": wallpost["views"]["count"] if "views" in wallpost else 0,
                    "comments_count": wallpost["comments"]["count"] if "comments" in wallpost else 0,
                    "post": same.get()
                })
                log(f"Post {same.get().id}: timestamps were updated")
        task_source.total_objects_downloaded += downloaded
        task_source.save()
        task.requests_count += 2
        task.save()
    log(f"VK data downloaded in task {task.id}")
    