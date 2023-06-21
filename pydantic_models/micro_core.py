from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal

class MicroCore(BaseModel):
    ''' A MicroCore entity aims to describes:
            small cylider of rock extracted during drilling at the same time the cuttings are collected
    '''
    id: int = Field(description="The id of the micro core", example=1)
    registered_by: str = Field(
        ..., description="The user who registered the micro core")
    well_name: str = Field(
        ..., description="The name of the well", example="DEL-GT-01")
    micro_core_number: int = Field(
        ..., description="The predefined name of the micro core", example=50)
    
    micro_core_name: str = Field(
        ..., description="The name of the micro core that is generated based on well_name", 
        examples= { "example":"DELGT01-MC-1"})

    collection_time: datetime = Field(
        ..., description="The time when the micro core was collected", example="2023-01-01 12:00:00")
    
    registration_time: datetime = Field(
        ..., description="The time when the micro core was registered in the database", example="2023-01-01 12:00:00")

    lithology: str = Field(
        ..., description="The lithology of the micro core", example="Sandstone")
    
    remarks: str = Field(
        ..., description="The remarks of the micro core", example="Sample micro core")
    
    # Optional fields
    drilling_method: Literal ["Rotary", "Motor", "Both"] = Field(
        default=None,
        description="The method used for drilling", example="Rotary")
    drilling_bit: str = Field(
        default=None,
        description="The bit used for drilling")
    drilling_mud: Literal["Water-based mud", "Oil-based mud"] = Field(
        description="The drilling mud used for the perforation of the micro core", example="Water-based mud")
    