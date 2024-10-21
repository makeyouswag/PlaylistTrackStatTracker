from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class TrackFeatures:
    pitch_class: int  # 0-11
    mode: int  # major=1 / minor=2
    tempo: float
    danceability: Optional[float]
    camelot_key: str


@dataclass
class Track:
    id: str
    name: str
    artists: list
    features: list[TrackFeatures]
