#1. Given input file for which duplicate has to be found
#2. Loop theough all the files and folders in the root folder
#3. If it is a file. Read the first non-empty text of the file column
#4. Write this text to a text file along with file name tab separated
#5. If it is a folder loop through all the files and folder a d repeat step 3,4,5 until all the folders/files have been traversed

import os
import pandas as pd
from pandas_ods_reader import read_ods

#Set the name of the file in the given variable for which duplicate has to be found

OUTPUT_TEXT_FILENAME = "./output.txt"
ROOT_FOLDER = "G:\Isha\PythonProject\ManuallyValidatedFiles\ManuallyValidatedFiles"
#ROOT_FOLDER = "G:\Isha\PythonProject\may3_files\may3_files"
xls_tsv_ods= ""
HAS_HEADER = "None"
total_count = 0

def get_files(folder):
    line_count = 0
    total_count = 0
    for dirpath,subdirectories,files in os.walk(folder):
        for file in files:
            openfile = open(dirpath + "\\" + file, "r", encoding="utf8")
            line_count = 0
            if ('eng' in file):
                for line in openfile:
                    if line != "\n":
                        line_count += 1
                print(dirpath + '\\' + file)
                print(line_count)
                total_count = total_count + line_count
            openfile.close()
        print(total_count)


get_files(ROOT_FOLDER)
