from models.core import Core
from models.core_chip import CoreChip
from models.well import Well
from models.cuttings import Cuttings
from models.micro_core import MicroCore

# Create some Core objects
core1 = Core(id=1, core_type="Core", top_depth=100.0, bottom_depth=110.0)
core2 = Core(id=2, core_type="Core catcher", top_depth=110.0, bottom_depth=120.0)
core3 = Core(id=3, core_type="Core", top_depth=120.0, bottom_depth=130.0)

# Add some CoreChip objects to core1
corechip1 = CoreChip(id=1, chip_type="Whole round", section_number=1)
corechip2 = CoreChip(id=2, chip_type="Half round", section_number=2)
core1.core_chips.append(corechip1)
core1.core_chips.append(corechip2)

# Create a Well object and add the Core objects to it
well = Well(id=1, well_name="DEL-GT-01", cores=[core1, core2, core3])

# Print out the Well object and its attributes
print(well)
print(well.id)
print(well.well_name)

# Print out the Core objects and their attributes
for core in well.cores:
    print(core)
    print(core.id)
    print(core.core_type)
    print(core.top_depth)
    print(core.bottom_depth)
    print(core.core_chips)