from os import environ as env


class Config:
    SECRET_KEY = 'H2,//&%"=O5cL<K9j80O^GhnliI>a/_G' or\
        env.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' or\
        env.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
