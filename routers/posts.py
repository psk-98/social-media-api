from fastapi import APIRouter, HTTPException, Path
from starlette import status

from core.dependencies import db_dependency, user_dependency
from models import Post
from schemas.posts import CreatePostRequest, PostResponse, UpdatePostRequest

router = APIRouter(prefix="/post", tags=["posts"])


@router.get("/", response_model=PostResponse, status_code=status.HTTP_200_OK)
def posts(auth_user: user_dependency, db: db_dependency):
    posts = db.query(Post).filter(Post.user_id == auth_user.get("user_id")).all()
    return posts


@router.get("/{post_id}", response_model=PostResponse, status_code=status.HTTP_200_OK)
def get(db: db_dependency, post_id: int = Path(gt=0)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(
    request: CreatePostRequest, auth_user: user_dependency, db: db_dependency
):
    if auth_user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    post = Post(**request.model_dump(), user_id=auth_user.get("user_id"))

    db.add(post)
    db.commit()
    return post


@router.put(
    "/{post_id}", response_model=PostResponse, status_code=status.HTTP_202_ACCEPTED
)
def update_post(
    request: UpdatePostRequest,
    auth_user: user_dependency,
    db: db_dependency,
    post_id: int = Path(gt=0),
):
    if auth_user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    post_model = (
        db.query(Post)
        .filter(Post.id == post_id)
        .filter(Post.user_id == auth_user.get("user_id"))
        .first()
    )

    if post_model is None:
        raise HTTPException(status_code=404, detail="Post not found")

    post_model.content = request.content

    db.add(post_model)
    db.commit()
    return post_model


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    auth_user: user_dependency,
    db: db_dependency,
    post_id: int = Path(gt=0),
):
    if auth_user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    post = (
        db.query(Post)
        .filter(Post.id == post_id)
        .filter(Post.user_id == auth_user.get("user_id"))
        .first()
    )

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    db.query(Post).filter(Post.id == post_id).filter(
        Post.user_id == auth_user.get("user_id")
    ).delete()
    db.commit()
    return post
