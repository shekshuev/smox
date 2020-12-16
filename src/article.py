"""
    только для эксперимента
    к самой программе не относится
"""
from faker import Faker
import random
from datetime import timedelta
from database.social.post import PostModel
from database.social.post_timestamp import PostTimestampModel
from database.social.post_attachment import PostAttachmentModel
from database.social.source import SourceModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "mysql://smox:smoxsmox@localhost:3306/smox"
engine = create_engine(SQLALCHEMY_DATABASE_URI)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

def generate_posts(count):
    fake = Faker()
    id = 1
    for i in range(1, 11, 1):
        source = SourceModel(
            source_id = -i * 10000, 
            name = fake.bs(), 
            domain = fake.domain_name(),
            description = fake.paragraph(nb_sentences=3),
            photo = "https://picsum.photos/200"
        )
        session.add(source)
        session.commit()
        for _ in range(count):
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
            session.add(post)
            session.commit()
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
                session.add(post_attachment)
            session.commit()
            ts = random.randint(100, 10000)
            for j in range(ts):
                Faker.seed(random.randint(0, 100000))
                created = post.created_at + timedelta(hours = j)
                post_timestamp = PostTimestampModel(
                    post_id = post.id, 
                    created_at = created,
                    likes_count = 0,
                    reposts_count = 0,
                    views_count = 0,
                    comments_count = 0
                )
                session.add(post_timestamp)
            session.commit()
            id += 1
            print(f"post {id}, attachments: {attachments}, timestamps: {ts}")

if __name__ == "__main__":
    print("fuck")
    generate_posts(1000)
