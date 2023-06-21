from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal, List

from rockin.pydantic_models.rockin_base import RockinBase
from core_chip import CoreChip


class Core(RockinBase):
    id: int = Field(description="The id of the core", example=1)

    core_type: Literal['Core', 'Core catcher'] = Field(
        ..., description="The type of the core", example="Core")
    
    top_depth: float = Field(
        ..., description="The top depth of the section of a meter sample", example=100.00)
    bottom_depth: float = Field(
        ..., description="The bottom depth of the section of a meter sample", example=110.00)

    # Optional fields
    core_section_length: float  = Field(
        default=None, description="The length of the section of a meter sample", example=10.00)
    core_recovery: float  = Field(
        default=None, description="The recovery of the material in the core liner", example=100.00)
    core_diameter: float  = Field(
        default=None, description="The diameter of the core in inches", example=5.00)
    coring_method: Literal['Motor', 'Rotary', 'Both']  = Field(
        default=None, description="The method used for coring", example="Rotary")
    coreliner: str  = Field(
        default=None, description="The material used for the core liner", example="Plastic")
    formation: str  = Field(
        default=None, description="The geological formation where the core was extracted from", example="Sandstone")
    core_status: Literal['Preserved', 'Opened']  = Field(
        default=None, description="The status of the core", example="Available")
    preservation: Literal['Refrigerated at 4 degrees Celsius', 'Core rack at room temperature']  = Field(
        default=None, description="The preservation method used for the core", example="Frozen")
    core_weight: float  = Field(
        default=None, description="The weight of the core in kilograms", example=50.00)
    ct_scanned: bool  = Field(
        default=None, description="Whether the core was CT scanned or not", example=True)
    gamma_ray: bool  = Field(
        default=None, description="Whether the core was gamma ray scanned or not", example=False)
    radiation: float  = Field(
        default=None, description="The radiation of the core in Bq units", example=0.01)
    # This should automatically be captured by the system    
    core_chips = List[CoreChip]

    class Config:
        arbitrary_types_allowed = True