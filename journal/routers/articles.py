from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from journal import schemes, models, operations 
from myutils import hasher, dbutils, authenticator

router = APIRouter(
    tags=['Articles'],
    prefix='/articles'
)


@router.get('/', response_model=List[schemes.ArticlePublic])
def articles(db: Session = Depends(dbutils.get_db), curent_user:
             schemes.AuthorBase = Depends(authenticator.get_curent_user)):
    return operations.get_articles(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def article_create(request: schemes.ArticlePublic,
                   db: Session = Depends(dbutils.get_db), curent_user:
                   schemes.AuthorBase = Depends(authenticator.get_curent_user)):
    return operations.create_article(db, request)


@router.get('/{id}/', status_code=status.HTTP_200_OK,
            response_model=schemes.ArticlePublic)
def article(id: int, db: Session = Depends(dbutils.get_db),
            curent_user: schemes.AuthorBase = Depends(
                authenticator.get_curent_user)):
    return operations.get_article(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def article_update(id: int, request: schemes.ArticlePublic, 
                   db: Session = Depends(dbutils.get_db), curent_user:
                   schemes.AuthorBase = Depends(authenticator.get_curent_user)):
    return operations.update_article(db, id, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def article_delete(id: int, db: Session = Depends(dbutils.get_db), curent_user:
                   schemes.AuthorBase = Depends(authenticator.get_curent_user)):
    return operations.delete_article(db, id)
