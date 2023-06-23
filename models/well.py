from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal, List
from .core import Core
from .cuttings import Cuttings
from .micro_core import MicroCore


class Well(BaseModel):
    id: int = Field(description="The id of the well", example=1)
    well_name: str = Field(
        ..., description="The name of the well", example="DEL-GT-01")
    cores: list = List[Core]
    cuttings: list = List[Cuttings]
    micro_cores: list = List[MicroCore]