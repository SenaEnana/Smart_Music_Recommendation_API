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

@app.get("/recommend")
def read_recommend():
    return {
       "message": "Here is what I recommend based on your input!"
    }

@app.get("/all-song")
def read_all():
    return {
       "message": "Here you can see all songs!"
    }

@app.get("/view-song")
def read_view():
    return {
       "message": "Here you can view the song!"
    }

@app.get("/download")
def read_download():
    return {
       "message": "Here you can download your song!"
    }