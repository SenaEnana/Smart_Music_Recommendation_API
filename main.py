from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
       "message": "Hello, Music Bot!"
    }

@app.get("/search-song")
def read_search():
    return {
       "message": "Here you can search what you want!"
    }

@app.get("/all-song")
def read_all():
    return {
       "message": "Here you see all songs!"
    }

