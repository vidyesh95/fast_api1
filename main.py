from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/read-root")
def read_root():
    """
    This is a path operation function.
    It handles GET requests to the root path "/read-root"
    """
    return {"message": "Hello, World!"}
