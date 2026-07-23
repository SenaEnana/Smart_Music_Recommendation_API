from typing import Literal
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from database import get_db_connection

app = FastAPI()

class Song(BaseModel):
    title: str
    artist: str
    genre: str 
    mood: str 
    theme: str
    album: str
    language: str 
    explicit: int 

@app.get("/")
def read_root():
    return {
       "message": "Hello, Music Bot!"
    }

@app.post("/songs/", status_code=status.HTTP_201_CREATED)
async def create_song(song: Song):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO songs (title, artist, genre, mood, theme, album, language, explicit)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(query, (
            song.title,
            song.artist,
            song.genre,
            song.mood,
            song.theme,
            song.album,
            song.language,
            song.explicit
        ))
        
        connection.commit()
        connection.close()
        
        return {"message": "Song added successfully", "data": song.model_dump()}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        ) 

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

