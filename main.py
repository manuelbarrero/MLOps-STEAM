from fastapi import FastAPI
import pandas as pd


app = FastAPI()

@app.get("/PlayTimeGenre")
def PlayTimeGenre(genre: str):
    df = pd.read_parquet('data/game_playtime.parquet', engine='pyarrow')
    filtered = df[df['genres'].apply(lambda arr: genre in arr)]
    result = filtered.groupby('year')['playtime_forever'].sum().reset_index()
    imax = df['playtime_forever'].idxmax()
    year = df['year'].loc[imax]
    return {f"Año de lanzamiento con más horas jugadas para Género {genre}" : int(year)}

@app.get("/UserForGenre")
def UserForGenre(genre: str):
    rows = []
    with open('data/game_playtime.json', 'r', -1, 'utf8') as file:
        for row in file:
            rows.append(eval(row))
    df = pd.DataFrame(rows)
    df = df[df['genres'].apply(lambda arr: genre in arr)]
    df = df.groupby('year')['playtime_forever'].sum().reset_index()
    imax = df['playtime_forever'].idxmax()
    year = df['year'].loc[imax]
    return {f"Año de lanzamiento con más horas jugadas para Género {genre}": int(year)}


@app.get("/UsersRecommend")
def UsersRecommend(año: int):
    return ''


@app.get("/UsersNotRecommend")
def UsersNotRecommend(año: int):
    return ''


@app.get("/SentimentAnalysis")
def sentiment_analysis(año: int):
    return ''
