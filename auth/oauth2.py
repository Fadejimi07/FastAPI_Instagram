from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import Depends, HTTPException, status
