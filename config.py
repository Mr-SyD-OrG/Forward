#!/usr/bin/env python3
import os
from os import environ 

class Config:
    API_ID = int(environ.get('API_ID', ''))
    API_HASH = environ.get('API_HASH', '')
    BOT_TOKEN = environ.get('BOT_TOKEN', "") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get('DATABASE_URI', "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "cluster0")
    BOT_OWNER_ID = os.environ.get("BOT_OWNER_ID", "")

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
