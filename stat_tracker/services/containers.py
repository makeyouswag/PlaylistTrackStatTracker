from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class TrackFeatures:
    key: int  # 0-11
    mode: int  # major=1 / minor=2
    tempo: float
    danceability: Optional[float]


@dataclass
class Track:
    id: str
    name: str
    artists: list
    features: list[TrackFeatures]
