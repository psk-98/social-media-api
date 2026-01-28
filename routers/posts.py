from fastapi import APIRouter

router = APIRouter(prefix="/post", tags=["posts"])


@router.get("/")
def posts():
    return "Hello osts"
