from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal
from .rockin_base import RockinBase

class MicroCore(RockinBase):
    ''' A MicroCore entity aims to describes:
            small cylider of rock extracted during drilling at the same time the cuttings are collected
    '''
    # Override core_number, core_section_number, core_section_name
    # This is needed as these values are not applicable for micro cores
    core_number: str = None
    core_section_number: str = None
    core_section_name: str = None
    
    micro_core_number: int = Field(
        ..., description="The predefined name of the micro core", example=50)
    
    micro_core_name: str = Field(
        ..., description="The name of the micro core that is generated based on well_name", 
        examples= { "example":"DELGT01-MC-1"})
    
    # Optional fields
    drilling_method: Literal ["Rotary", "Motor", "Both"] = Field(
        default=None,
        description="The method used for drilling", example="Rotary")
    drilling_bit: str = Field(
        default=None,
        description="The bit used for drilling")