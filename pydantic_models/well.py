from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal, List
from rockin.pydantic_models.core import Core
from rockin.pydantic_models.cuttings import Cuttings
from rockin.pydantic_models.micro_core import MicroCore


class Well(BaseModel):
    id: int = Field(description="The id of the well", example=1)
    well_name: str = Field(
        ..., description="The name of the well", example="DEL-GT-01")
    cores: list = List[Core]
    cuttings: list = List[Cuttings]
    micro_cores: list = List[MicroCore]