# from datetime import datetime, timedelta, time
# from typing import Annotated

from fastapi import FastAPI
# from fastapi import Path, Query, Body, Cookie, HTTPException
# from pydantic import BaseModel

app = FastAPI()


# items = {"foo": "The Foo Wrestlers"}


# class Cookies(BaseModel):
#     session_id: str
#     fatebook_tracker: str | None = None
#     googall_tracker: str | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# @app.get("/items/")
# async def read_items(cookies: Annotated[Cookies, Cookie()]):
#     return cookies


# @app.put("/items/{item_id}")
# async def read_items(
#         item_id: int,
#         start_datetime: Annotated[datetime, Body()],
#         end_datetime: Annotated[datetime, Body()],
#         process_after: Annotated[timedelta, Body()],
#         repeat_at: Annotated[time | None, Body()] = None,
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "process_after": process_after,
#         "repeat_at": repeat_at,
#         "start_process": start_process,
#         "duration": duration,
#     }
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}