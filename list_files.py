import os
Path='sample_data'
FileName='output.txt'
file_list=[f for f in os.listdir(Path) if f.endswith('.csv')]
with open(FileName, "w") as file:
    for f in file_list:
        file.write(f+"\n")