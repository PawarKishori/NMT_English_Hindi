#Get count og total number of non-empty lines in text file under a given folder

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
