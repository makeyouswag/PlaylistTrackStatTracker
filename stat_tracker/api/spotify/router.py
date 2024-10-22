from fastapi import APIRouter, Query
from starlette.responses import StreamingResponse

from stat_tracker.api.spotify.schemas import CamelotKey
from stat_tracker.integrations.spotify.track_features import get_playlist_tracks
from stat_tracker.services.csv_exporter import get_track_table_buffer
from stat_tracker.services.utils import find_tracks_by_tune

router = APIRouter(prefix="/spotify")


@router.post("/track-table")
def get_track_table(playlist_id: str) -> StreamingResponse:
    tracks = get_playlist_tracks(playlist_id)
    filename = f"{playlist_id}.csv"
    return StreamingResponse(
        get_track_table_buffer(tracks),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.post("/chosen-tune-tracks")
def get_chosen_tune_track_table(
    tune: CamelotKey,
    playlist_ids: list[str] = Query(
        [], description="Playlist ids to include in the search"
    ),
):
    tracks = [
        track
        for playlist_id in playlist_ids
        for track in get_playlist_tracks(playlist_id)
    ]
    return StreamingResponse(
        get_track_table_buffer(find_tracks_by_tune(tracks, tune.value)),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={tune.value}.csv"},
    )
