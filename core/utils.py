from core.models import *
import string

#Returns only Sector and Position code, ie: A4
def get_sector_and_position_code(base_station_id):
    sector = base_station_id[6] #(A)lpha, (B)eta, (C)Gamma , (D)Delta
    position = base_station_id[9] #1,2,3,4
    sector_and_position = sector + position
    print("Sector + Position", sector_and_position )
    return sector_and_position

#returns the USID 
def get_usid(station_id):
    usid = station_id[0:5]
    return usid

#Returns Relative Antenna Position
def get_relative_antenna_position(station_id):
    relative_antenna_position = station_id[9]
    return relative_antenna_position

# Turn Sector and Position Code into human readable position, ie: Alpha Position 4
def get_ret_position(sector_and_position): 
    ret_position = { 
        'A1' : 'Alpha Position 1', 
        'A2' : 'Alpha Position 2', 
        'A3' : 'Alpha Position 3', 
        'A4' : 'Alpha Position 4',
        'B1' : 'Beta Position 1', 
        'B2' : 'Beta Position 2', 
        'B3' : 'Beta Position 3', 
        'B4' : 'Beta Position 4',
        'C1' : 'Gamma Position 1', 
        'C2' : 'Gamma Position 2', 
        'C3' : 'Gamma Position 3', 
        'C4' : 'Gamma Position 4',
        'D1' : 'Delta Position 1', 
        'D2' : 'Delta Position 2', 
        'D3' : 'Delta Position 3', 
        'D4' : 'Delta Position 4',   
    } 
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return ret_position.get(sector_and_position, "no position match") 

def get_tilt_range(tilt_range):
    adjust = tilt_range.replace(",", "  -")
    line = adjust.translate(str.maketrans('', '','MaxTilt:'))
    return line

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
    #operating band = reference for matching 
    #cell id = leading reference
    #prefix = A,B,C

    eutran_cell_id = { 
        '2' : cell_id+'_2'+prefix+'_1',  
        '3' : cell_id+'_3'+prefix+'_1', 
        '6' : cell_id+'_2'+prefix+'_1', 
        '7' : cell_id+'_7'+prefix+'_1', 
        '8' : cell_id+'_8'+prefix+'_1', 
        '9' : cell_id+'_9'+prefix+'_1',  
        'A' : cell_id+'_2'+prefix+'_1;'+cell_id+'_2'+prefix+'_2', 
        'B' : cell_id+'_9'+prefix+'_1;'+cell_id+'_2'+prefix+'_2', 
        'C' : cell_id+'_2'+prefix+'_1;'+cell_id+'_2'+prefix+'_2;'+cell_id+'_3'+prefix+'_1', 
        'D' : cell_id+'_9'+prefix+'_1;'+cell_id+'_2'+prefix+'_1', 
        'E' : cell_id+'_2'+prefix+'_2;'+cell_id+'_3'+prefix+'_1',
        'F' : cell_id+'_9'+prefix+'_1;'+cell_id+'_3'+prefix+'_1',
        'G' : cell_id+'_9'+prefix+'_1;'+cell_id+'_2'+prefix+'_1;'+cell_id+'_2'+prefix+'_2',
        'H' : cell_id+'_2'+prefix+'_1;'+cell_id+'_3'+prefix+'_1',
        'I' : cell_id+'_9'+prefix+'_1;'+cell_id+'_2'+prefix+'_2;'+cell_id+'_3'+prefix+'_1',
        'J' : cell_id+'_9'+prefix+'_1;'+cell_id+'_2'+prefix+'_1;'+cell_id+'_3'+prefix+'_1',
        'K' : cell_id+'_7'+prefix+'_1;'+cell_id+'_8'+prefix+'_1', 
        'M' : cell_id+'_9'+prefix+'_1;'+cell_id+'_2'+prefix+'_1;'+cell_id+'_3'+prefix+'_1', 
        'P' : cell_id+'_7'+prefix+'_2_F',  
        'Q' : cell_id+'_7'+prefix+'_2_E', 
        'R' : cell_id+'_7'+prefix+'_1;'+cell_id+'_7'+prefix+'_2_F;'+cell_id+'_8'+prefix+'_1', 
        'S' : cell_id+'_7'+prefix+'_1;'+cell_id+'_8'+prefix+'_1;'+cell_id+'_7'+prefix+'_2_E',
        'T' : cell_id+'_7'+prefix+'_1;'+cell_id+'_7'+prefix+'_2_F;'+cell_id+'_7'+prefix+'_1_E',
        'U' : cell_id+'_7'+prefix+'_1;'+cell_id+'_7'+prefix+'_2_F;'+cell_id+'_7'+prefix+'_1_E;'+cell_id+'_8'+prefix+'_1',
        'W' : cell_id+'_7'+prefix+'_E;__'+cell_id+'_7'+prefix+'_2_F', 
        'X' : cell_id+'_7'+prefix+'_1;'+cell_id+'_7'+prefix+'_2_F', 
        'Y' : cell_id+'_7'+prefix+'_2_E;'+cell_id+'_8'+prefix+'_1',  
        'Z' : cell_id+'_7'+prefix+'_2_F;'+cell_id+'_8'+prefix+'_1', 
    } 
    return eutran_cell_id.get(operating_band, "no matching bands") 

#Sets Ret Sub Unit value based off of Eutran Cell ID value
def set_ret_sub_unit(base_station_id, eutran_cell_id):
    ret_sub_unit = base_station_id + '__' + eutran_cell_id
    return ret_sub_unit



