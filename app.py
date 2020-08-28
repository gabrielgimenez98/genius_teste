import lyricsgenius
from flask import Flask, jsonify
from pymongo import MongoClient 

client = MongoClient('localhost', 27017) 


app = Flask(__name__)
mydatabase = client['Genius']
mycollection = mydatabase['artistas'] 

def get_songs(artist_name):
	genius = lyricsgenius.Genius("Q_7TOUYh4QjwD3f-NUMTIIlJoakhZVdBG1JVovS0Ulm8qX-RGGdTrGGbbs7cvNRU")
	artist = genius.search_artist(artist_name, max_songs=10, sort="popularity")
	return artist.songs

@app.route("/")
def hello():
	return "Adicione o nome do artista para buscar"


@app.route("/<artista>")
def busca(artista):

	songs = get_songs(artista)
	songs = [i.title for i in songs]
	record={ 
	"artista": artista,   
	"songs": list(songs)
	}   
	rec = mydatabase.myTable.insert_one(record)
	return ','.join(list(songs))



if __name__ == "__main__":
	app.run()