from core.models import *

#Returns only Sector and Position code, ie: A4
def get_sector_and_position_code(base_station_id):
    sector = base_station_id[6] #(A)lpha, (B)eta, (C)Gamma 
    position = base_station_id[9] #1,2,3,4
    sector_and_position = sector + position
    print("Sector + Position", sector_and_position )
    return sector_and_position

# Turn Sector and Position Code into human readable position, ie: Alpha Position 4
def get_ret_position(sector_and_position): 
    ret_position = { 
        'A1' : 'Alpha Position 1', 
        'A2' : 'Alpha Position 2', 
        'A3' : 'Alpha Position 3', 
        'A4' : 'Alpha Position 4', 
    } 
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return ret_position.get(sector_and_position, "no match") 

#this method returns simply A, B, or C 
def get_eutran_prefix(base_station_id):
    prefix = base_station_id[6] #A,B, or C
    return prefix

def get_band(base_station_id):
    band = base_station_id[10]
    return band
   
def get_technology(base_station_id):
    technology = base_station_id[11]
    return technology

def get_operating_band(band, technology):
    if technology == 'N':
        operating_band = '--' 
        return operating_band

    else:
        operating_band = { 
            '2' : '2100', 
            '3' : '2300', 
            '6' : '2100',
            '7' : '700', 
            '8' : '850',  
            '9' : '1900', 
            'A' : '2100', 
            'B' : '1900', 
            'C' : '2100 / 2300', 
            'D' : '1900 / 2100', 
            'E' : '2300', 
            'F' : '1900 / 2300', 
            'G' : '1900 / 2100', 
            'H' : '2100 /2300', 
            'I' : '1900 / 2300', 
            'J' : '1900 / 2100 / 2300', 
            'K' : '700 / 850', 
            'M' : '1900 / 2100 / 2300', 
            'P' : 'FNET', 
            'Q' : '700', 
            'R' : '700 / 850', 
            'S' : '700 / 850', 
            'T' : 'FNET', 
            'U' : 'FNET / 700 / 850', 
            'W' : 'FNET', 
            'X' : 'FNET', 
            'Y' : '700 / 850', 
            'Z' : 'FNET / 850', 
        } 
    return operating_band.get(band, "no match")

#This Updates or Creates Technology objects when Rets are creates, Update so no duplicates! 
def update_or_create_technology_object(operating_band, tech_parent_ref):
    technology = Technology.objects.update_or_create(
        parent_ref_number = tech_parent_ref,
        technology_operating_band = operating_band
    )
    #technology.save()
    return technology


#Sets the Eutran Cell ID for RETS when a technology Cell_ID is updated
def set_eutran_cell_id(operating_band, cell_id, prefix):
    eutran_cell_id = { 
        '9' : cell_id+'_7'+prefix+'_1;'+cell_id+'_8'+prefix, 
        '8' : '1900', 
        'P' : 'FNET', 
    } 
    return eutran_cell_id.get(operating_band, "no matching bands") 

#Sets Ret Sub Unit value based off of Eutran Cell ID value
def set_ret_sub_unit(base_station_id, eutran_cell_id):
    ret_sub_unit = base_station_id + '__' + eutran_cell_id
    return ret_sub_unit



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