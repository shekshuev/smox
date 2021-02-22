# Скрипт для перехода от старой БД, которая была к проге на c#

import sqlite3
import datetime

old_conn = sqlite3.connect("app/Database.db")
new_conn = sqlite3.connect("app/app.db")
old = old_conn.cursor()
new = new_conn.cursor()


def move_source():
    new.execute("DELETE from source;")
    new_conn.commit()
    old.execute("SELECT Id, SourceId, Name, Domain, Description, Photo from Sources;")
    for row in old:
        new.execute(f"INSERT INTO source (id, source_id, name, domain, description, photo) values ({row[0]}, {row[1]}, '{row[2]}', '{row[3]}', '{row[4]}', '{row[4]}')")
    new_conn.commit()

def move_post():
    new.execute("DELETE from post;")
    new_conn.commit()
    old.execute("SELECT Id, PostId, OwnerId, FromId, SourceId, PostedDate, Text, Class from Posts;")
    for row in old:
        new.execute(f"INSERT INTO post (id, post_id, owner_id, from_id, source_id, created_at, text, value) values (?, ?, ?, ?, ?, ?, ?, ?)", 
            (row[0], row[1], row[2], row[3], row[4], datetime.datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S'), row[6] if row[6] != None else "", row[7]))
    new_conn.commit()

def move_post_timestamp():
    new.execute("DELETE from post_timestamp;")
    new_conn.commit()
    old.execute("SELECT PostId, DownloadedDate, LikesCount, RepostsCount, ViewsCount, CommentsCount from PostTimeStamps;")
    for row in old:
        new.execute("INSERT INTO post_timestamp (post_id, created_at, likes_count, reposts_count, views_count, comments_count) VALUES (?, ?, ?, ?, ?, ?)",
            (row[0], datetime.datetime.strptime(row[1][:19], '%Y-%m-%d %H:%M:%S'), row[2], row[3], row[4], row[5]))
    new_conn.commit()

def move_post_attachment():
    new.execute("DELETE from post_attachment;")
    new_conn.commit()
    old.execute("SELECT Id, PostId, Type, Text, Url from PostAttachments;")
    for row in old:
        new.execute("INSERT INTO post_attachment (id, post_id, type, title, text, url) VALUES (?, ?, ?, ?, ?, ?);", 
            (row[0], row[1], row[2], "", row[3], row[4]))
    new_conn.commit()

def move_access_profile():
    new.execute("DELETE from access_profile;")
    new_conn.commit()
    old.execute("SELECT Id, Name, AccessToken from AccessProfiles;")
    for row in old:
        new.execute("INSERT INTO access_profile (id, name, access_token) VALUES (?, ?, ?);", 
            (row[0], row[1], row[2]))
    new_conn.commit()

def move_task():
    new.execute("DELETE from task;")
    new_conn.commit()
    old.execute("SELECT Id, IsFinished, BeginDate, EndDate, RequestsCount, AccessProfileId from DownloadTasks;")
    for row in old:
        new.execute("INSERT INTO task (id, is_finished, begin_datetime, end_datetime, requests_count, access_profile_id, is_error, error) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", 
            (row[0], row[1], datetime.datetime.strptime(row[2][:19], '%Y-%m-%d %H:%M:%S'), datetime.datetime.strptime(row[3][:19], '%Y-%m-%d %H:%M:%S') if row[3] else None, row[4], row[5], False, ""))
    new_conn.commit()

def move_task_source():
    new.execute("DELETE from task_source;")
    new_conn.commit()
    old.execute("SELECT SourceId, DownloadTaskId, TotalObjectsDownloaded, Offset, Count, BeginCount from TaskSources;")
    for row in old:
        new.execute("INSERT INTO task_source (source_id, task_id, total_objects_downloaded, offset, count, begin_count) VALUES (?, ?, ?, ?, ?, ?);", 
            (row[0], row[1], row[2], row[3], row[4], row[5]))
    new_conn.commit()

def move_logs():
    new.execute("DELETE from log;")
    new_conn.commit()
    old.execute("SELECT Id, Message, Date, Type from Logs;")
    for row in old:
        new.execute("INSERT INTO log (id, message, datetime, type) VALUES (?, ?, ?, ?);", 
            (row[0], row[1] if row[1] else "", row[2], row[3]))
    new_conn.commit()

#move_source()
#move_post()
#move_post_timestamp()
#move_post_attachment()
#move_access_profile()
#move_task()
#move_task_source()
#move_logs()
