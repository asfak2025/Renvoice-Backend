import uuid
import time

from fastapi import HTTPException

def generate_epoch_id(prefix):
    return f"{prefix}{str(int(time.time()*1000))}"


def generate_uuid():
    return str(uuid.uuid4())

def generate_indian_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def generate_indian_date():
    return time.strftime("%Y-%m-%d", time.localtime())

def returnIndianTime(date):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(date))