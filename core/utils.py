from core.models import *

#Returns only Sector and Position code, ie: A4
def get_sector_and_position_code(base_station_id):
    sector = base_station_id[6] #Alpha, Beta, Gamma 
    position = base_station_id[9] #1,2,3,4
    sector_and_position = sector + position
    print("Sector + Position", sector_and_position )
    return sector_and_position

# Turn Sector and Position Code into human readable position, ie: Alpha Position 4
def get_ret_position(sector_and_position): 
    ret_position = { 
        'A4' : 'Alpha Position 4', 
        1: "one", 
        2: "two", 
    } 
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return ret_position.get(sector_and_position, "no match") 

def get_band(base_station_id):
    band = base_station_id[10]
    return band
   
def get_technology(base_station_id):
    technology = base_station_id[11]
    return technology

def get_operating_band(band): 
    operating_band = { 
        'K' : '700/850', 
        '9' : '1900', 
        'P' : 'FNET', 
    } 
    return operating_band.get(band, "no match") 


def update_or_create_technology_object(operating_band, tech_parent_ref):
    technology = Technology.objects.update_or_create(
        parent_ref_number = tech_parent_ref,
        technology_operating_band = operating_band
    )
    #technology.save()
    return technology


# Create or Update 
# obj, created = Person.objects.update_or_create(
#     first_name='John', last_name='Lennon',
#     defaults={'first_name': 'Bob'},
# )


# Update RET implentation:

# ret = ret.objects.all()

# if method == POST:
#     technology = Something to get the specific technology 
#       Need to set the Foreign Keys to each otheer 
#     technology_cell_id = user input on this specfic form 
#     technolgy_cell_id.save()

#     for ret in rets:
#         if ret.operating_band == tecnology.operating_band:
#             ret.cell_id = technology_cell_id 
#             ret.save() or update   
#         else: 
#             pass