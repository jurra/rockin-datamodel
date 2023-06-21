from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal
from .core import Core

class CoreChip(BaseModel):
    ''' When you have the core, before sealing it in the core liner, you can take a chip of it
    chip as in potato chip    
    '''
    chip_id: int = Field(description="The id of the core chip", example=1)
    registered_by: str = Field(
        ..., description="The user who registered the core chip")
    well_name: str = Field(
        ..., description="The name of the well", example="DEL-GT-01")
    core_chip_number: int = Field(
        ..., description="The predefined name of the core chip", example=50)
    from_top_bottom: Literal['Top', 'Bottom'] = Field(
        ..., description="Whether the core chip was taken from the top or the bottom of the core", example="Top")
    core_chip_name: str = Field(
        ..., description="The name of the core chip that is generated based on well_name, \n\
                          core_number, core_section_number, core_chip_number and from_top_bottom",
        # If a core chip top is preceding a core chip bottom then the core chip should be like bellow
        # There will never be at the same time DELGT01-C1-53-CHT53 and DELGT01-C1-53-CHB53                 
        examples= { "example_top":"DELGT01-C1-53-CHT53", "example_bottom": "DELGT01-C1-53-CHB54" })
    core_chip_depth: float = Field(
        ..., description="The depth of the core chip in meters", example=100.00)
    collection_date: datetime = Field(
        ..., description="The date when the core chip was collected", example="2023-01-01 12:00:00")
    lithology: str = Field(
        ..., description="The lithology of the core chip", example="Sandstone")
    remarks: str = Field(
        ..., description="The remarks of the core chip", example="Sample core chip")
    
    # Optional fields
    debris: bool = Field(
        default=None,
        description="Whether the core chip is a debris or not", example=True)
    formation: str = Field(
        default=None,
        description="The formation of the core chip", example="Sandstone")
    
    
    # Repeated from a base model to be defined
    # core_number
    # core_section_number
    # core_section_name
    # drilling mud
    # registration time

