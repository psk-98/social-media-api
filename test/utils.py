import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from models import Base, Post, User
from routers.users import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://admin:password@127.0.0.1:6543/social_media_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {"username": "Testuser", "user_id": 1, "role": "admin"}


client = TestClient(app)


@pytest.fixture
def test_user_instance():
    user = User(
        username="Testuser",
        email="test@email.com",
        password=bcrypt_context.hash("testpassword"),
        role="admin",
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()

    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()


@pytest.fixture
def test_post_instance():
    post = Post(content="This is a test post", user_id=1)

    db = TestingSessionLocal()
    db.add(post)
    db.commit()
    yield post
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM posts;"))
        connection.commit()
