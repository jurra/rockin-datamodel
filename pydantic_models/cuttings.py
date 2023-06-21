from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal


class Cuttings(BaseModel):
    id: int = Field(..., description="The id of the cuttings", example=1)

    # REQUIRED FIELDS
    registered_by: str = Field(
        ..., description="The user who registered the cuttings")
    well_name: str = Field(description="The name of the well", example="DEL-GT-01")
    
    cuttings_number: int = Field(
        # These are given numbers by the drillers
        ..., description="The predefined name of the cuttings", example=50)
    
    cuttings_name: str = Field(
        ..., description="The name of the cuttings", example="DELGT01-53")

    cuttings_depth: float = Field(
        ..., description="The depth of the cuttings in meters", example=100.00)
    
    collection_date: datetime = Field(
        ..., description="The date when the cuttings were collected", example="2023-01-01 12:00:00")

    sample_state: Literal["Wet washed", "Wet unwashed", "Dry washed"] = Field(
        description="The state of the sample", example="Solid")

    lithology: str = Field(
        ..., description="The lithology of the sample", example="Sandstone")
    
    remarks: str = Field(
        ..., description="The remarks of the sample", example="Sample cuttings")
    
    # OPTIONAL FIELDS
    collection_method: Literal["Drilling", "Coring", "Rathole", "Flushing"] = Field(
        # hast three options: Drilling, Coring, Rathole
        default=None, description="The method used for collecting the cuttings", example="Shovel")
    
    drilling_method: Literal ["Rotary", "Motor", "Both"] = Field(
        default=None,
        description="The method used for drilling", example="Rotary")
    
    drilling_mud: Literal["Water-based mud", "Oil-based mud"] = Field(
        description="The drilling mud used for the perforation of the cuttings", example="Water-based mud")

    sample_weight: float = Field(
        default=None,
        description="The weight of the sample in kilograms", example=50.00)

    dried_sample: bool = Field(
        default=None,
        description="Whether the sample was dried or not", example=True)
    
    dried_by: str = Field(
        default=None,
        description="The user who dried the sample", example="user1")
    dried_date: datetime = Field(
        default=None,
        description="The date when the sample was dried", example="2023-01-01 12:00:00")
    registration_time: datetime = Field(
        default=datetime.now(),
        description="The time when the cuttings were registered in the database", example="2023-01-01 12:00:00")

    # TODO: Not sure how this should be generated
    def gen_cuttings_number():
        # This is generated automatically
        # This is the sample number and it has to be secquential
        return 1
    
