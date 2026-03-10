from fastapi import status

from core.dependencies import get_db
from core.jwt import get_current_user
from main import app
from test.utils import (
    client,
    override_get_current_user,
    override_get_db,
    test_post_instance,
    test_user_instance,
)

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_get_user_posts(test_user_instance, test_post_instance):
    response = client.get("/post/")

    assert response.status_code == status.HTTP_200_OK
