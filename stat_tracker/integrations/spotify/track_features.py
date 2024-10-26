from dataclasses import asdict
from pprint import pprint

from stat_tracker.integrations.spotify import client
from stat_tracker.services.containers import Track, TrackFeatures
from stat_tracker.services.pitch_to_key import get_camelot_key


def get_playlist_tracks(playlist_id: str) -> list[Track]:
    """
    Get all tracks from a playlist
    """
    response = client.playlist_items(playlist_id, additional_types=("track",))
    return [
        Track(
            item["track"]["id"],
            [artist["name"] for artist in item["track"]["artists"]],
            item["track"]["name"],
            get_track_features(item["track"]["id"]),
        )
        for item in response["items"]
    ]


def get_track_features(track: str) -> TrackFeatures:
    """
    Get track features from Spotify
    """
    track_features = client.audio_features(track)
    return [
        TrackFeatures(
            get_camelot_key(track_feature["key"], track_feature["mode"]),
            track_feature["tempo"],
            track_feature["key"],
            track_feature["mode"],
            track_feature["danceability"],
        )
        for track_feature in track_features
    ][0]


if __name__ == "__main__":
    playlist_id = "3o8iHwUYlNXH7E6GBwOWB4"
    tracks = get_playlist_tracks(playlist_id)
    pprint([asdict(track) for track in tracks])
