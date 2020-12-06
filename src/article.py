"""
    только для эксперимента
    к самой программе не относится
"""
from faker import Faker
import random
from datetime import datetime, timedelta
from database import db
from database.social.post import PostModel
from database.social.post_timestamp import PostTimestampModel
from database.social.post_attachment import PostAttachmentModel
from database.social.source import SourceModel

def generate_sources():
    fake = Faker()
    for i in range(1, 11, 1):
        source = SourceModel(
            source_id = -i * 10000, 
            name = fake.bs(), 
            domain = fake.domain_name(),
            description = fake.paragraph(nb_sentences=3),
            photo = "https://picsum.photos/200"
        )
        db.session.add(source)
    db.session.commit()

def generate_posts():
    fake = Faker()
    id = 1
    for source in SourceModel.query.all():
        for _ in range(1000):
            Faker.seed(random.randint(0, 100000))
            post = PostModel(
                post_id = id,
                owner_id = source.source_id,
                from_id = source.source_id,
                source_id = source.id,
                created_at = fake.date_between(start_date="-10d", end_date="-1d"),
                text = fake.paragraph(nb_sentences=10),
                target = 0,
            )
            db.session.add(post)
            db.session.commit()
            attachments = random.randint(0, 10)
            for _ in range(attachments):
                Faker.seed(random.randint(0, 100000))
                post_attachment = PostAttachmentModel(
                    post_id = post.id,
                    type = 1,
                    title = fake.paragraph(nb_sentences=1),
                    text = fake.paragraph(nb_sentences=3),
                    url = "https://picsum.photos/200"
                )
                db.session.add(post_attachment)
            db.session.commit()
            ts = random.randint(100, 10000)
            for i in range(ts):
                Faker.seed(random.randint(0, 100000))
                created = post.created_at + timedelta(hours = i)
                post_timestamp = PostTimestampModel(
                    post_id = post.id, 
                    created_at = created,
                    likes_count = 0,
                    reposts_count = 0,
                    views_count = 0,
                    comments_count = 0
                )
                db.session.add(post_timestamp)
            db.session.commit()
            id += 1

if __name__ == "__main__":
    print("fuck")
