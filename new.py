import json
import csv

# Turn one TXT file into JSON RET object 
filename = '4.txt'
commands = {}
with open(filename) as fh:
    for line in fh:
        command, description = line.strip().split(':', 1)
        commands[command] = description.strip()

# Define the title of the JSON document 
with open('1.txt', 'r') as title:
    myvar = title.readline()
    myvar = myvar.strip()
    myvar = myvar.replace("\\","/") 

# Add the title to the JSON object with extra formatting and dump into JSON File 
with open('result.json', 'w') as fp:
    fp.write("{" + "\n" + '"' + myvar + '":['  )
    json.dump(commands, fp, indent=2, sort_keys=True)
    fp.write("\n" + "]" + "\n" + "}" )


######   Write JSON to CSV file     ######

#Opening JSON file and loading the data 
#into the variable data 
with open('retjson.json') as json_file: 
    data = json.load(json_file) 
  
employee_data = data['emp_details'] 
  
# now we will open a file for writing 
data_file = open('data_file.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0
  
for emp in employee_data: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = emp.keys() 
        csv_writer.writerow(header) 
        count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(emp.values()) 
  
data_file.close() 



#print(my_dict)