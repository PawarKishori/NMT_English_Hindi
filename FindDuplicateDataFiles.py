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
ROOT_FOLDER = "G:\Isha\PythonProject\may3_files\may3_files"
xls_tsv_ods= ""
HAS_HEADER = "None"

def get_files(folder):
    for dirpath,subdirectories,files in os.walk(folder):
        for file in files:
            print(os.path.abspath(file),file)
            read_write_file(dirpath + "\\" + file,"0")


def read_write_file(file,write_file):
    if (file.endswith(".xlsx")):
        sentence_data = pd.read_excel(file, header = None)
        col_num = len(sentence_data.columns)
    elif (file.endswith(".tsv")):
        sentence_data = pd.read_csv(file, sep='\t', header = None)
        col_num = len(sentence_data.columns)
    elif (file.endswith(".ods")):
        sentence_data = read_ods(file, 1, headers = None)
        col_num = len(sentence_data.columns)
    else:
        print("Unknown file format:" + file)
        #raise Exception("Unknown file format:" + file)
        return

    first_text = sentence_data.iloc[0, 0]
    loop = 0
    while (type(first_text) != str or len(first_text)==0):
        loop = loop + 1
        first_text = sentence_data.iloc[loop, 0]

    if (write_file == "1"):
        file_write = open(OUTPUT_TEXT_FILENAME, "w", encoding='utf-8')
    else:
        file_write = open(OUTPUT_TEXT_FILENAME, "a", encoding='utf-8')

    file_write.write(file + "\t" + first_text.strip() + "\n")
    file_write.close()

input_file_name = "G:\Isha\PythonProject\ManualCheckDonePassed\Pragyaansh\E64_aligned_duplicate.xlsx"

read_write_file(input_file_name,"1")
get_files(ROOT_FOLDER)
