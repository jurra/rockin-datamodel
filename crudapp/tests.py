from django.test import TestCase
import pytest

# Create your tests here.
# Task fixture well
@pytest.fixture
def valid_well_data():
    well = Well(
        well_name = 'well1',
        # For now this is good enough
        # date should be added
        # Location should
    )

    return well

@pytest.fixture
def invalid_well_data():
    pass

@pytest.fixture
def valid_core_data():
    '''
    A section is of one meter always
    A core alltogether can be 100 meters long more or less
    Tubes are collected in sections of 9 meters long
    Several cores of 100 m can be extracted from one well

    About the enttity core
        Each core is 9 meters long, its a cilinder of soil sample
        Each core is divided in 9 sections of 1 meter long
    
    ATRIBUTES UP TO REMARKS ARE REQUIRED:
    well_name: type string
        This is the name of the well it should be a dropdown menu, there are only two wells

    core_number: type string
        This are predefined names from C1 to C9, this has nothing to do with the sections of the core
        User enters the core number, this is a dropdown menu
        
    core_sec_name:
        This is the name of the section, it is a combination of the well name, the core number and the section number
    
    core_sec_number:
        What does this attribute describes?

        About the core_sec_number:
            At moment the person manually inputs the number of the section
    top_depth: type float
        This is the top depth of the section of a meter sample
    bottom_depth: type float
        This is the bottom depth of the section of a meter sample
    remarks: type string
        This is a string of remarks of the section of a meter sample
    -------

    ATRIBUTES FROM CORE_SEC_LENGTH TO END ARE OPTIONAL:
    core_sec_length: type float
        This is the length of the section of a meter sample, they are expected to be 1 meter long
        but in case of a broken core the length can be less than 1 meter
    core_recovery: type float
        When you open the tube you can observe how much material is in the core liner, 
        but the material inside the case is the recovery and is measured in meters
    core_diameter: float
        This should be standard and constant and should inherited from the well adopted standard
        This diameter is in inches
    coring_method: string
        For this we have 3 options as a dorpdown list
        1. Motor, 2.Rotary, 3.Both
    core_liner: string
        liners can be built out of different materials, i.e. alluminium, plastic, steel, etc
        For our case we are using alluminium
    drilling_mud: string
        This is the drilling mud used for the perforation of the core
        There are two options: 1. Water-based mud, 2. Oil-based mud
    formation: string
        This is the geological formation where the core was extracted from
    lithology: string
        This is the lithology of the core
    core_status: string
        Option dropdwon list: 1. Preserved, 2. Opened
    preservation: string
        There two options:
            1. Refrigerated at 4 degrees Celsius
            2. Core rack at room temperature
    core_weight: float
        This is the weight of the core in kilograms
    ct_scanned: boolean
        This is a boolean value, True or False
    gamma_ray: boolean
        This is a boolean value, True or False
    radiation: float
        This is the radiation of the core in Bq units
    registration_time: datetime
        This is the time when the core was registered in the database
        This should automatically be captured by the system
    '''
    core = Core(
        # id is automatically generated
        
        # Automatically generated
        registered_by = 'user1', 
        
        well_name = 'DEL-GT-01', # Next one would be DEL-GT-02
        
        core_number = 'C2', # String this comes from a list of predefined core values from 'C1' till 'C9' this has nothing to do with units of sections from 1 to 9 is just a coincidence for now
        core_sec_number = 1, # this is the counter for all 1 meter sections of the core
        
        # Automatically generated based on the well name, the core number and the core section number
        core_sec_name = 'DELGT01-C1-53', # This section name,
        
        # Default value is the date in which user is registering the core but it can be changed
        collection_date = '2020-01-01',
        # In this case of planned_core_number it was planned to be C1 but it was extracted as C2....
        planned_core_number = 'C1', # This is the same as core_number during perforation C2 might not be extracted but thats the name in plan
        top_depth = 303.5,
        bottom_depth = 304.5,
        remarks = 'The core fell and the core-liner is damaged', 

        # Next attributes are optional and can be captured after perforation
        # Automatically calculated from top_depth and bottom_depth
        core_sec_length = 1.0, # This is automatically calculated from top_depth and bottom_depth
        core_recovery = 0.8, # meters
        core_diameter = 4, # inches
        coring_method = 'Motor', # Motor, Rotary, Both
        core_liner = 'Alluminium', # Alluminium, Plastic, Steel, etc
        drilling_mud = 'Water-based mud', # Water-based mud, Oil-based mud
        formation = 'Sandstone', # Sandstone, Limestone, etc
        lithology = 'Sandstone', # Sandstone, Limestone, etc
        core_status = 'Preserved', # Preserved, Opened
        preservation = 'Refrigerated at 4 degrees Celsius', # Refrigerated at 4 degrees Celsius, Core rack at room temperature
        core_weight = 10.5, # kg
        ct_scanned = False, # True or False
        gamma_ray = False, 
        radiation = 30.8, # Bq

        # This should be automatic
        registration_time = '2020-01-01 12:00:00',
    )
    return core

@pytest.fixture
def invalid_core_data():
    core = Core(
        registered_by = 'user1',
        well_name = 'well1',
        core_number = 1, # invalid because is an integer

@pytest.fixture
def valid_cuttings_data():
    pass

@pytest.fixture
def invalid_cuttings_data():
    pass

@pytest.fixture
def valid_core_catcher_data():
    pass

@pytest.fixture
def invalid_core_catcher_data():
    pass

@pytest.fixture
def valid_core_chip_data():
    pass

@pytest.fixture
def invalid_core_chip_data():
    pass

@pytest.fixture
def valid_micro_core_data():
    pass

@pytest.fixture
def invalid_micro_core_data():
    pass
