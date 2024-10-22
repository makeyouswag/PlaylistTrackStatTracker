from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class TrackFeatures:
    pitch_class: int  # 0-11
    mode: int  # major=1 / minor=0
    camelot_key: str
    tempo: float
    danceability: Optional[float]


@dataclass
class Track:
    id: str
    name: str
    artists: list
    features: TrackFeatures
