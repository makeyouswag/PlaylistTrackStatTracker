import io
import os
import pathlib
from dataclasses import asdict

from stat_tracker.integrations.spotify.track_features import get_playlist_tracks
from stat_tracker.services.containers import Track
import pandas as pd


def create_track_table(tracks: list[Track]) -> pd.DataFrame:
    """
    Write a list of tracks to a csv file
    """
    tracks_with_features = []
    for track in tracks:
        track_dict = asdict(track)
        features = track_dict.pop("features")
        tracks_with_features.append({**track_dict, **features})
    return pd.DataFrame(tracks_with_features)


def write_track_table(tracks: list[Track], path: str | os.PathLike | pathlib.Path):
    create_track_table(tracks).to_csv(path)


def get_track_table_buffer(tracks: list[Track]):
    buffer = io.BytesIO()
    return create_track_table(tracks).to_csv(buffer)


if __name__ == "__main__":
    playlist_id = "3o8iHwUYlNXH7E6GBwOWB4"
    write_track_table(get_playlist_tracks(playlist_id), "example.csv")
