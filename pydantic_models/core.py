from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal
from core_chip import CoreChip


class Core(BaseModel):
    id: int = Field(description="The id of the core", example=1)

    core_type: Literal['Core', 'Core catcher'] = Field(
        ..., description="The type of the core", example="Core")
    
    # Automatically generated
    registered_by: str = Field(
        ..., description="The user who registered the core")

    # Automatically generated
    registration_time: date  = Field(
        ...,default=None, description="The time when the core was registered in the database")

    # Next one would be DEL-GT-02
    well_name: str = Field(
        ..., description="The name of the well", example="DEL-GT-01")

    # String this comes from a list of predefined core values from 'C1' till 'C9' this has nothing to do with units of sections from 1 to 9 is just a coincidence for now
    core_number: str = Field(
        ..., description="The predefined name of the core from C1 to C9", example="C2")
    
    core_section_number: int = Field(
        ..., description="The counter for all 1 meter sections of the core", example=1)

    # Automatically generated based on the well name, the core number and the core section number
    core_section_name: str = Field(
        # Notice in the examples that one is for Core and the other for Core catcher
        # See that in both examples they follow a sequential relationship and is consistent with the 
        # core_number and core_section_number sequence
        # The catcher type adds a suffix of CC to the core number
        # There cannot be a core catcher without the preceding core
        # TODO: How can we enforce the relationship between core and core catcher considering the above?
            # A way to do it is to check that there is a preciding core based on the core number
            # If there is no core number that matches the core number selected for the catcher then
            # the system should not allow the user to register the core catcher and throw an error
        # core catcher number is core number plus 1 this needs to be handdled by the system
        ..., description="The name of the section based on the well name, the core number and the core section number, see that CC has a sequential relationship with the core number and core section number", 
        examples= {"example_core":"DELGT01-C1-53", "example_core_catcher": "DELGT01-C1-53-CC54"})

    top_depth: float = Field(
        ..., description="The top depth of the section of a meter sample", example=100.00)
    bottom_depth: float = Field(
        ..., description="The bottom depth of the section of a meter sample", example=110.00)
    remarks: str = Field(
        ..., description="The remarks of the section of a meter sample", example="Sample core")

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
    drilling_mud: Literal[' Water-based mud', 'Oil-based mud']  = Field(
        default=None, description="The drilling mud used for the perforation of the core", example="Water-based mud")
    formation: str  = Field(
        default=None, description="The geological formation where the core was extracted from", example="Sandstone")
    lithology: str  = Field(
        default=None, description="The lithology of the core", example="Sandstone")
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
    core_chips = List[CoreChips]

external_core = {
    "id": 1,
    "registered_by": "user1",
    "core_type": "Core",
    "well_name": "DEL-GT-01",
    "core_number": "C2",
    "core_section_number": 1,
    "core_section_name": "DELGT01-C1-53",
    "top_depth": 303.5,
    "bottom_depth": 304.5,
    "remarks": "The core fell and the core-liner is damaged",
    "core_section_length": 1.0,
    "core_recovery": 0.8,
    "core_diameter": 4,
    "coring_method": "Motor",
    "coreliner": "Alluminium",
    "drilling_mud": "Water-based mud",
    "formation": "Sandstone",
    "lithology": "Sandstone",
    "core_status": "Preserved",
    "preservation": "Refrigerated at 4 degrees Celsius",
    "core_weight": 10.5,
    "ct_scanned": True,
    "gamma_ray": False,
    "radiation": 0.01,
    "registration_time": "2020-01-01"
}

core = Core(**external_core)