from datetime import timedelta

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm

from fastalchemy import SQLAlchemyMiddleware, db
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from passlib.context import CryptContext
from sample import database, models, schemas
from sample.models import User

SECRET = '6a824282e5030a2d2c4059d0c096a820e22d8e2898036434'
manager = LoginManager(SECRET, tokenUrl='/auth/token')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

app.add_middleware(SQLAlchemyMiddleware,
                   db_module=database,
                   models_module=models)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:19006",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_db = {'test@test.com': {'password': 'test'}}


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


@manager.user_loader
def load_user(email: str):
    user = fake_db._db.get(email)
    return user


@app.get('/hello')
def hello(user=Depends(manager)):
    return user


@app.get('/clean_db')
def clean_db():
    database.meta.drop_all()


@app.get('/generate/sample')
def generate_sample():
    db.query(User).delete()
    users = [
        User(email='kim@test.com', password='1234'),
        User(email='park@test.com', password='1234'),
        User(email='choi@test.com', password='1234'),
    ]
    db.add_all(users)


@app.post('/auth/token')
def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = load_user(
        email)  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=email), expires_delta=timedelta(hours=8))
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    user = User(id=user.id, email=user.email)
    db.add(user)
    return user


@app.get('/users')
def get_users():
    '''Return users.'''
    users = db.query(User).order_by(User.email).all()
    return users
