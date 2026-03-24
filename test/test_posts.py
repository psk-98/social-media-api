from fastapi import status

from core.dependencies import get_db
from core.jwt import get_current_user
from main import app
from models import Post
from test.utils import (
    TestingSessionLocal,
    client,
    override_get_current_user,
    override_get_db,
    test_post_instance,
    test_user_instance,
)

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


# def test_get_user_posts(test_post_instance, test_user_instance):
#     response = client.get("/post/")

#     assert response.status_code == status.HTTP_200_OK


def test_get_post_by_id(test_post_instance):
    response = client.get("/post/1")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id": 1, "content": "This is a test post", "user_id": 1}


def test_get_post_by_id_not_found(test_post_instance):
    response = client.get("/post/2")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Post not found"}


def test_create_post(test_post_instance):
    request_data = {"content": "Testing post creation", "user_id": 1}
    response = client.post("/post", json=request_data)

    assert response.status_code == status.HTTP_201_CREATED

    db = TestingSessionLocal()
    post_model = db.query(Post).filter(Post.id == 2).first()
    assert post_model.content == request_data.get("content")
    assert post_model.user_id == request_data.get("user_id")


def test_update_post(test_post_instance):
    request_data = {"content": "Testing post creation", "user_id": 1}
    response = client.put("/post/1", json=request_data)

    assert response.status_code == status.HTTP_202_ACCEPTED

    db = TestingSessionLocal()
    post_model = db.query(Post).filter(Post.id == 1).first()
    assert post_model.content == request_data.get("content")
    assert post_model.user_id == request_data.get("user_id")
