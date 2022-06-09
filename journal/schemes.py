from pydantic import BaseModel
from typing import List, Optional


class ArticleBase(BaseModel):
    title: str
    body: str


class ArticlePublic(ArticleBase):
    author_id: int

    class Config():
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    email: str
    password: str


class AuthorPublic(AuthorBase):
    id: int
    articles: List[ArticlePublic] = [] 

    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
