from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from journal import schemes, operations 
from myutils import dbutils, authenticator

router = APIRouter(
    tags=['Authors'],
    prefix='/authors'
)


@router.post('/', response_model=schemes.AuthorPublic,
          status_code=status.HTTP_201_CREATED)
def author_create(request: schemes.AuthorBase,
                  db: Session = Depends(dbutils.get_db), curent_user:
                  schemes.AuthorBase = Depends(
                     authenticator.get_curent_user)):
    return operations.create_author(db, request)


@router.get('/{id}/', status_code=status.HTTP_200_OK)
def author(id: int, db: Session = Depends(dbutils.get_db), curent_user:
           schemes.AuthorBase = Depends(authenticator.get_curent_user)):
   return operations.get_author(db, id)
