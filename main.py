"""
This script takes the name of an ifc-model as input. It returns a report consisting of the total number of each structural
elenemnt and the number of elements wheras the material is not defined.

Due to timelimits, it is chosen to make a simplified script where the aim is to present the idea and proove a point. It is 
for now based on some assumptions, where the thought is to improve the script in a further work. First, it is assumed that 
the ifc-model only consist of structural elements. This is based on the fact that this scrip/tool is, for now, only predicted 
to be used by structural engineers as a "self check" tool. Next up, it is assumed that if an element is defined with its 
material, the material is defined in "ObjectType". This would be improved in a future work.

The thought of this tool is to make the quality check less time consuming. For a future work, the script would be improved by
classify by id in general, like ccs, cci and bim7a. As well, it would be improved by having a quality check for more information
data in the structural model. It could also be cool to illustrate the model, with an highlight of the elements where something 
is missing. The improvement could consist of making the tool cooparate with other programs, and make it as an open source.
"""

# Import neccessary packages
import ifcopenshell
import ifcopenshell.geom


#filename = 'Example_Structure.ifc'
filename = input('Please input the name of an IFC-file (E.g. Example_Structure.ifc): ')

ifc = ifcopenshell.open(filename)

walls = ifc.by_type('IfcWall')
beams = ifc.by_type('IfcBeam')
columns = ifc.by_type('IfcColumn')
slabs = ifc.by_type('IfcSlab')

tot = len(walls)+len(beams)+len(columns)+len(slabs)
print('\n')
print('--------------------------------- REPORT ----------------------------------')
print('IFC-File:', str(filename))
print(' ')
print('The total number of elements is', tot, 'wheras the number of each element is:')
print(' ')
print('Beams:', len(beams), '          Columns:', len(columns), '          Slabs:', len(slabs), '          Walls:', len(walls))
print('\n')

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(' ')
print('Number of elements missing material definition:')
print(' ')

numb_error_beams = 0
for beam in beams:
    beamObject = str(beam.ObjectType).lower()
    
    # Locates material
    if 'concrete' in beamObject:
        continue
    elif 'wwod' in beamObject:
        continue
    elif 'timber' in beamObject:
        continue
    elif 'steel' in beamObject:
        continue
    else:
        numb_error_beams += 1


numb_error_columns = 0
for column in columns:
    columnObject = str(column.ObjectType).lower()
    
    # Locates material
    if 'concrete' in columnObject:
        continue
    elif 'wwod' in columnObject:
        continue
    elif 'timber' in columnObject:
        continue
    elif 'steel' in columnObject:
        continue
    else:
        numb_error_columns += 1


numb_error_slabs = 0
for slab in slabs:
    slabObject = str(slab.ObjectType).lower()
    
    # Locates material
    if 'concrete' in slabObject:
        continue
    elif 'wwod' in slabObject:
        continue
    elif 'timber' in slabObject:
        continue
    elif 'steel' in slabObject:
        continue
    else:
        numb_error_slabs += 1


numb_error_walls = 0
for wall in walls:
    wallObject = str(wall.ObjectType).lower()
    
    # Locates material
    if 'concrete' in wallObject:
        continue
    elif 'wwod' in wallObject:
        continue
    elif 'timber' in wallObject:
        continue
    elif 'steel' in wallObject:
        continue
    else:
        numb_error_walls += 1


print('> Beams:', numb_error_walls, '          Columns:', numb_error_columns,'          Slabs:', numb_error_slabs, '          Walls:', numb_error_walls,'<')

print('')
print('---------------------------------------------------------------------------')
print('\n')



