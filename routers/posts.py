from fastapi import APIRouter, HTTPException, Path
from starlette import status

from core.dependencies import db_dependency, user_dependency
from models import Post
from schemas.posts import CreatePostRequest, PostRespoonse, UpdatePostRequest

router = APIRouter(prefix="/post", tags=["posts"])


@router.get("/", status_code=status.HTTP_200_OK)
def posts(user: user_dependency, db: db_dependency, post_id: int = Path(gt=0)):
    posts = db.query(Post).filter(Post.user_id == user.get("user_id")).all()
    return posts


@router.get("/{post_id}", status_code=status.HTTP_200_OK)
def get(user: user_dependency, db: db_dependency, post_id: int = Path(gt=0)):
    post = db.query(Post).filter(Post.user_id == user.get("user_id")).first()
    return post


@router.post("/", response_model=PostRespoonse, status_code=status.HTTP_201_CREATED)
def create_post(request: CreatePostRequest, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    post_model = Post(**request.model_dump(), user_id=user.get("user_id"))

    db.add(post_model)
    db.commit()
    return post_model


@router.put(
    "/{post_id}", response_model=PostRespoonse, status_code=status.HTTP_202_ACCEPTED
)
def update_post(
    request: UpdatePostRequest,
    user: user_dependency,
    db: db_dependency,
    post_id: int = Path(gt=0),
):
    if user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    post_model = (
        db.query(Post)
        .filter(Post.id == post_id)
        .filter(Post.user_id == user.get("user_id"))
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
    user: user_dependency,
    db: db_dependency,
    post_id: int = Path(gt=0),
):
    if user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    post_model = (
        db.query(Post)
        .filter(Post.id == post_id)
        .filter(Post.user_id == user.get("user_id"))
        .first()
    )

    if post_model is None:
        raise HTTPException(status_code=404, detail="Post not found")

    db.query(Post).filter(Post.id == post_id).filter(
        Post.user_id == user.get("user_id")
    ).delete()
    db.commit()
    return post_model
