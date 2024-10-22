from stat_tracker.services.containers import Track


def find_tracks_by_tune(tracks: list[Track], tune: str):
    return [track for track in tracks if track.features.camelot_key == tune]
