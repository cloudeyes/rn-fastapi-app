import os
import sys
import subprocess

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

ENV = os.environ.get('ENV', 'DEV')
DB_TYPE = os.environ.get('DB_TYPE', 'mysql')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'sample')
DB_PASS = os.environ.get('DB_PASS', 'sample')
DB_NAME = os.environ.get('DB_NAME', 'sample')

if DB_HOST[0] > '9':
    process = subprocess.Popen(["nslookup", DB_HOST], stdout=subprocess.PIPE)
    output = process.communicate()[0].decode().strip().split('\n')
    DB_HOST = output[-1:][0].split(': ')[-1]

DATABASE_URL = {
    'DEV': 'sqlite:///./dev.db',
    'TEST': 'sqlite:///./test.db',
    'PROD': f'{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
}[ENV]

connect_args = {'check_same_thread': False} if ENV != 'PROD' else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

Base = declarative_base()
meta = MetaData(engine)
