from fastapi import status, HTTPException
from sqlalchemy.orm.session import Session
from journal import models, schemes
from myutils import hasher


# -------------- Authors section --------------
def create_author(db: Session, request: schemes.AuthorBase):
    new_author = models.Author(name=request.name, email=request.email,
                           password=hasher.hashit(request.password))
    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    return new_author


def get_author(db: Session, id: int):
    author = db.query(models.Author).filter(models.Author.id==id).first()
    
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f'Author with id {id} is not available'
        )

    return author


# -------------- Articles section --------------
def get_articles(db: Session):
    articles = db.query(models.Article).all()
    return articles


def create_article(db: Session, request: schemes.ArticlePublic):
    new_article = models.Article(title=request.title, body=request.body,
                                 author_id=request.author_id)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


def get_article(db: Session, id: int):
    article = db.query(models.Article).filter(models.Article.id==id).first()
    
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f'Blog with id {id} is not available'
        )

    return article


def update_article(db: Session, id: int, request: schemes.ArticlePublic):
    article = db.query(models.Article).filter(models.Article.id == id)
    if not article.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    article.update({
        'title': request.title,
        'body': request.body,
    })
    db.commit()

    return {f'Blog with id {id} is updated'}


def delete_article(db: Session, id: int):
    article = db.query(models.Article).filter(models.Article.id == id)
    if not article.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    article.delete(synchronize_session=False)
    db.commit()

    return {f'Blog with id {id} is deleted'}

