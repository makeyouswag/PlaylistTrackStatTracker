import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from stat_tracker.settings import settings

auth_manager = SpotifyClientCredentials(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET,
)
client = spotipy.Spotify(auth_manager=auth_manager)
