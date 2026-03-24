from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from core.db import SessionLocal
from core.security import hash_password
from models import Follow, Like, Post, User


def seed():
    db: Session = SessionLocal()

    try:
        # --------------------
        # USERS
        # --------------------
        user1 = User(
            email="alice@example.com",
            username="alice",
            password=hash_password("password"),
            role="user",
        )

        user2 = User(
            email="bob@example.com",
            username="bob",
            password=hash_password("password"),
            role="user",
        )

        user3 = User(
            email="admin@example.com",
            username="admin",
            password=hash_password("password"),
            role="admin",
        )

        db.add_all([user1, user2, user3])
        db.commit()

        # refresh to get IDs
        db.refresh(user1)
        db.refresh(user2)
        db.refresh(user3)

        # --------------------
        # POSTS
        # --------------------
        post1 = Post(
            content="Hello world from Alice",
            user_id=user1.id,
        )

        post2 = Post(
            content="Bob’s first post",
            user_id=user2.id,
        )

        post3 = Post(
            content="Admin announcement",
            user_id=user3.id,
        )

        db.add_all([post1, post2, post3])
        db.commit()

        db.refresh(post1)
        db.refresh(post2)
        db.refresh(post3)

        # --------------------
        # LIKES (polymorphic)
        # --------------------
        like1 = Like(
            user_id=user2.id,
            liked_id=post1.id,
            liked_type="Post",
        )

        like2 = Like(
            user_id=user1.id,
            liked_id=post2.id,
            liked_type="Post",
        )

        like3 = Like(
            user_id=user3.id,
            liked_id=post1.id,
            liked_type="Post",
        )

        db.add_all([like1, like2, like3])
        db.commit()

        # --------------------
        # FOLLOWS
        # --------------------
        follow1 = Follow(
            follower_id=user1.id,
            followed_id=user2.id,
        )

        follow2 = Follow(
            follower_id=user2.id,
            followed_id=user1.id,
        )

        follow3 = Follow(
            follower_id=user1.id,
            followed_id=user3.id,
        )

        db.add_all([follow1, follow2, follow3])
        db.commit()

        print("✅ Database seeded successfully")

    except IntegrityError as e:
        db.rollback()
        print("⚠️ Integrity error (maybe already seeded):", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed()
