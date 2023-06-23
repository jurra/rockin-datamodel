from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal

from rockin.pydantic_models.rockin_base import RockinBase


class Cuttings(RockinBase):
    # Override core_number, core_section_number, core_section_name
    # This is needed as these values are not applicable for cuttings
    core_number: str = None
    core_section_number: str = None
    core_section_name: str = None

    id: int = Field(..., description="The id of the cuttings", example=1)

    # REQUIRED FIELDS    
    cuttings_number: int = Field(
        # These are given numbers by the drillers
        ..., description="The predefined name of the cuttings", example=50)
    
    cuttings_name: str = Field(
        ..., description="The name of the cuttings", example="DELGT01-53")

    cuttings_depth: float = Field(
        ..., description="The depth of the cuttings in meters", example=100.00)
    
    sample_state: Literal["Wet washed", "Wet unwashed", "Dry washed"] = Field(
        description="The state of the sample", example="Solid")
        
    # OPTIONAL FIELDS
    collection_method: Literal["Drilling", "Coring", "Rathole", "Flushing"] = Field(
        # hast three options: Drilling, Coring, Rathole
        default=None, description="The method used for collecting the cuttings", example="Shovel")
    
    drilling_method: Literal ["Rotary", "Motor", "Both"] = Field(
        default=None,
        description="The method used for drilling", example="Rotary")
    
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

    # TODO: Not sure how this should be generated
    def gen_cuttings_number():
        # This is generated automatically
        # This is the sample number and it has to be secquential
        return 1
    
