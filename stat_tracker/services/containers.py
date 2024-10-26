from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class TrackFeatures:
    camelot_key: str
    tempo: float
    pitch_class: int  # 0-11
    mode: int  # major=1 / minor=0
    danceability: Optional[float]


@dataclass
class Track:
    id: str
    artists: list
    name: str
    features: TrackFeatures
