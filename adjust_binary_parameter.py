#This is a script to replace the T2 binary option with ELL1, for compatability with PINT. 
import os
import sys 
import glob 
import numpy as np 

def replace_binary_line(file_path, old_line, new_line):
    print(file_path)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() == old_line:
                print(f"replacing {old_line} with {new_line} in {file_path}")
                file.write(new_line + '\n')
            else:
                file.write(line)



all_par_files = glob.glob("IPTA_Challenge1_*/Challenge_Data/Dataset*/*.par")



# # Line to replace
old_line = 'BINARY         T2'
new_line = 'BINARY         ELL1'

for f in all_par_files:
    replace_binary_line(f, old_line, new_line)

