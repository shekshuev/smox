# Скрипт для перехода от старой БД, которая была к проге на c#

import sqlite3
import datetime
import mysql.connector

new_conn = mysql.connector.connect(
    host="localhost",
    user="smox",
    password="Qwerty123!",
    database="smox"
)
new = new_conn.cursor()

old_conn = sqlite3.connect("app/Database.db")
#new_conn = sqlite3.connect("app/app.db")
old = old_conn.cursor()
#new = new_conn.cursor()

def drop_all():
    new.execute("DELETE from log;")
    new.execute("DELETE from post_timestamp;")
    new.execute("DELETE from post_attachment;")
    new.execute("DELETE from post;")
    new.execute("DELETE from task_source;")
    new.execute("DELETE from source;")
    new.execute("DELETE from task;")
    new.execute("DELETE from access_profile;")
    
    
    
    new_conn.commit()


def move_source():
    old.execute("SELECT Id, SourceId, Name, Domain, Description, Photo from Sources;")
    rows = []
    for row in old:
        rows.append((row[0], row[1], row[2], row[3], row[4], row[5]))
    new.executemany(f"INSERT INTO source (id, source_id, name, domain, description, photo) values (%s, %s, %s, %s, %s, %s)", rows)
    new_conn.commit()

def move_post():
    old.execute("SELECT Id, PostId, OwnerId, FromId, SourceId, PostedDate, Text, Class from Posts;")
    rows = []
    for row in old:
        rows.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6] if row[6] != None else "", row[7]))
    new.executemany(f"INSERT INTO post (id, post_id, owner_id, from_id, source_id, created_at, text, value) values (%s, %s, %s, %s, %s, %s, %s, %s)", rows)
    new_conn.commit()

def move_post_timestamp():
    old.execute("SELECT PostId, DownloadedDate, LikesCount, RepostsCount, ViewsCount, CommentsCount from PostTimeStamps;")
    rows = []
    for row in old:
        rows.append((row[0], row[1][:19], row[2], row[3], row[4], row[5]))
    new.executemany("INSERT INTO post_timestamp (post_id, created_at, likes_count, reposts_count, views_count, comments_count) VALUES (%s, %s, %s, %s, %s, %s)", rows)
    new_conn.commit()

def move_post_attachment():
    old.execute("SELECT Id, PostId, Type, Text, Url from PostAttachments;")
    rows = []
    for row in old:
        rows.append((row[0], row[1], row[2], "", row[3], row[4]))
    new.executemany("INSERT INTO post_attachment (id, post_id, type, title, text, url) VALUES (%s, %s, %s, %s, %s, %s);", rows)
    new_conn.commit()

def move_access_profile():
    old.execute("SELECT Id, Name, AccessToken from AccessProfiles;")
    rows = []
    for row in old:
        rows.append((row[0], row[1], row[2]))
    new.executemany("INSERT INTO access_profile (id, name, access_token) VALUES (%s, %s, %s);", rows)
    new_conn.commit()

def move_task():
    old.execute("SELECT Id, IsFinished, BeginDate, EndDate, RequestsCount, AccessProfileId from DownloadTasks;")
    rows = []
    for row in old:
        rows.append((row[0], row[1], row[2][:19], row[3][:19] if row[3] else None, row[4], row[5], False, ""))
    new.executemany("INSERT INTO task (id, is_finished, begin_datetime, end_datetime, requests_count, access_profile_id, is_error, error) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", rows)
    new_conn.commit()

def move_task_source():
    old.execute("SELECT SourceId, DownloadTaskId, TotalObjectsDownloaded, Offset, Count, BeginCount from TaskSources;")
    rows = []
    for row in old:
        rows.append((row[0], row[1], row[2], row[3], row[4], row[5]))
    new.executemany("INSERT INTO task_source (source_id, task_id, total_objects_downloaded, offset, count, begin_count) VALUES (%s, %s, %s, %s, %s, %s);", rows)
    new_conn.commit()

def move_logs():
    old.execute("SELECT Id, Message, Date, Type from Logs;")
    rows = []
    for row in old:
        rows.append((row[0], row[1] if row[1] else "", row[2], row[3]))
    new.executemany("INSERT INTO log (id, message, datetime, type) VALUES (%s, %s, %s, %s);", rows)
    new_conn.commit()

drop_all()
move_source()
move_post()
move_post_timestamp()
move_post_attachment()
move_access_profile()
move_task()
move_task_source()
move_logs()
