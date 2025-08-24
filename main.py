import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
client_id=os.environ.get('CLIENT_ID')
client_secret=os.environ.get('CLIENT_SECRET')
redirect_uri=os.environ.get('REDIRECT_URI')
scope=os.getenv('SCOPE', 'playlist-modify-private') # Default scope if not set in .env

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

date=input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
year = date.split("-")[0]
URL=f'https://www.billboard.com/charts/hot-100/{date}/'

response=requests.get(url=URL,headers=header).text

soup=BeautifulSoup(response,'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# SPOTIFY
user = sp.current_user()
user_id=user['id']
# Create a new playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top 100 songs from Billboard on {date}"
)

print("✅ Playlist created!")
playlist_id=playlist['id']

song_uris=[]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)