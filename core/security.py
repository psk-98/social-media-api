from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(entered_password: str, user_password: str):
    return bcrypt_context.verify(entered_password, user_password)


def hash_password(password: str):
    return bcrypt_context.hash(password)
