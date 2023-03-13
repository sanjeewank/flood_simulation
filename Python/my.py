import numpy as np

alllist=[]

with open("data.txt", "r") as file:
    for line in file:
        line1 = line.split(" ")
        line1.pop()
        float_list = [float(x) for x in line1]
        int_list = [int(x) for x in float_list]
        alllist.append(int_list)
        
flat_list = [item for sublist in alllist for item in sublist]
min_value = min(flat_list)
max_value = max(flat_list)

scale_factor = (999 - 100) / (max_value - min_value)

scaled_list = [[int(np.round((x - min_value) * scale_factor + 100)) for x in sublist] for sublist in alllist]

file=open("output.txt", "a")
for list in scaled_list:
    for num in list:
        strnum=str(num)
        file.write(strnum +" ")
    file.write("\n")
    
        
        
        
            
            