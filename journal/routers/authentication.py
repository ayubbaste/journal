from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from journal import models, schemes
from myutils import hasher, dbutils, tokenizer

router = APIRouter(
    tags=['Authentication'],
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dbutils.get_db)):
    author = db.query(models.Author).filter(
        models.Author.email==request.username).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not hasher.verify(author.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")

    access_token_expires = tokenizer.timedelta(minutes=tokenizer.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = tokenizer.create_access_token(data={"sub": author.email})
    return {"access_token": access_token, "token_type": "bearer"}

