from sqlmodel import SQLModel

from app.db.session import engine
from app.models.comment import Comment
from app.models.follow import Follow
from app.models.like import Like
from app.models.message import Message
from app.models.notification import Notification
from app.models.post import Post
from app.models.thread import Thread
from app.models.threadMember import ThreadMember
from app.models.user import User


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
