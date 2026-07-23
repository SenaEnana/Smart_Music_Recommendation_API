from fastapi import FastAPI, status

app = FastAPI()


@app.get("/")
def read_root():
    return {
       "message": "Hello, Music Bot!"
    }

@app.get("/songs")
def get_all_songs():
    return {
       "message": "Here you can see all songs!"
    }

@app.get("/songs/search")
def search_song():
    return {
       "message": "Here you can search what you want!"
    }

@app.get("/recommend")
def recommend_song():
    return {
       "message": "Here is what I recommend based on your input!"
    }


@app.get("/songs/{id}")
def view_song():
    return {
       "message": "Here you can view the song!"
    }
