from passlib.context import CryptContext 

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashit(password):
    return password_context.hash(password)


def verify(hashed_password, plain_password):
    return password_context.verify(plain_password, hashed_password)
