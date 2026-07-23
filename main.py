from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {
       "message": "Hello, Music Bot!"
    }

class Song(BaseModel):
    title: str
    artist: str
    genre: str 
    mood: str 
    theme: str
    album: str
    language: str 
    explicit: int 

music_recommendation_database = []

@app.post("/songs/", status_code=status.HTTP_201_CREATED)
async def create_song(song: Song):
    song_dict = song.model_dump()
    music_recommendation_database.append(song_dict)
    
    return {"message": "Song added successfully", "data": song_dict}

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
