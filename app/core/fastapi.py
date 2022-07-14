from fastapi import FastAPI
from config import config

app = FastAPI(
    title=config.APP_NAME,
    description=config.APP_DESCRIPTION,
)
