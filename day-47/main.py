import re
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

user_answer = input("Which year do you wanna travel to? Type the date in this format YYYY-MM-DD: ")

if not re.match(r'\d{4}-\d{2}-\d{2}', user_answer):
    raise ValueError("Invalid date format")

url = f"https://www.billboard.com/charts/hot-100/{user_answer}/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

names = [name.get_text().strip() for name in soup.select(selector="li.o-chart-results-list__item h3#title-of-a-story")]

songs = [singer.get_text().strip() for singer in soup.select(
    selector="li.o-chart-results-list__item span.c-label.a-no-trucate"
)]

songs_dict = dict(zip(names, songs))

scope = "playlist-modify-private"
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri="http://example.com",
        scope=scope
    )
)

user = spotify.current_user()

for song in songs_dict:
    result = spotify.search(q=f"track: {song} year: {user_answer.split('-')[0]}", type="track")
    if result["tracks"]["items"]:
        songs_dict[song] = result["tracks"]["items"][0]["uri"]
    else:
        songs_dict[song] = None

playlist = spotify.user_playlist_create(user['id'], f"{user_answer} Billboard 100", public=False)

spotify.playlist_add_items(playlist['id'], [song for song in songs_dict.values() if song])

print('Done!')
