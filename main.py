from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, utils
from journal import schemes, models
from journal.routers import articles, authentication, authors
from myutils import hasher
from myutils.dbutils import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext 


app = FastAPI()
# import routers
app.include_router(authentication.router)
app.include_router(authors.router)
app.include_router(articles.router)

# if not data => create it
models.Base.metadata.create_all(engine)
