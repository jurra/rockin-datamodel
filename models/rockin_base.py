from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Literal, List

class RockinBase(BaseModel):
    # Automatically generated
    registration_date: datetime  = Field(
        ..., description="The time when the core was registered in the database",
        example="2020-01-01:12:00:00")

    # Next one would be DEL-GT-02
    well: str = Field(
        ..., description="The name of the well", example="DEL-GT-01")
    # Automatically generated
    registered_by: str = Field(
        ..., description="The user who registered the core")
    
    collection_date: datetime = Field(
        ..., description="The date when the core was collected", example="2020-01-01:12:00:00")
    
    remarks: str = Field(
        ..., description="The remarks of the section of a meter sample", example="Sample core")
    
    drilling_mud: Literal['Water-based mud', 'Oil-based mud']  = Field(
        default=None, description="The drilling mud used for the perforation of the core", example="Water-based mud")

    lithology: str  = Field(
        default=None, description="The lithology of the core", example="Sandstone")

    # THE FOLLOWING FIELDS MIGHT NOT BE INHERITED BY ALL THE CLASSES
    # Instead only for corechip, core and core catcher

    # String this comes from a list of predefined core values from 'C1' till 'C9' this has nothing to do with units of sections from 1 to 9 is just a coincidence for now
    core_number: str = Field(
        ..., description="The predefined name of the core from C1 to C9", example="C2")

    planned_core_number: str = Field(
        ..., description="The predefined name of the core from C1 to C9", example="C2")

    core_section_number: int = Field(
        ..., description="The counter for all 1 meter sections of the core", example=53)

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

