from fastapi import APIRouter, HTTPException
from starlette import status

from core.dependencies import db_dependency, user_dependency
from models.likes import Like
from schemas.likes import LikeRequest

router = APIRouter(prefix="/like", tags=["likes"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_like(request: LikeRequest, auth_user: user_dependency, db: db_dependency):
    if auth_user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    like = Like(**request.model_dump(), user_id=auth_user.get("user_id"))

    db.add(like)
    db.commit()
    return like


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_like(request: LikeRequest, auth_user: user_dependency, db: db_dependency):
    if auth_user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    like = (
        db.query(Like)
        .filter(Like.liked_type == request.liked_type)
        .filter(Like.user_id == auth_user.get("user_id"))
        .first()
    )

    if like is None:
        raise HTTPException(status_code=404, detail="Like not found")

    (
        db.query(Like)
        .filter(Like.liked_type == request.liked_type)
        .filter(Like.user_id == auth_user.get("user_id"))
        .delete()
    )
    db.commit()
    return like
