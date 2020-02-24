import csv
import itertools

with open('ret.txtrpt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(":") for line in stripped if line)
    # lines = (line for line in stripped if line)
    
    grouped = itertools.izip(*[lines] * 1)

    with open('extracted.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('weq'))
        writer.writerows(grouped)




# with open('ret.txtrpt') as f:
#     for i in range(100):
#         print(f.readline())
    

# f.closed    
    
        

    