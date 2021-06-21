#Go through all files..if english, write in a consolidate english file..same for hindi
#Read the english and hindi consolidated text files to dataframe.
#Use train_test_split function to get the test and train dataset

import os
from turtle import width

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

root_folder = "G:\Isha\PythonProject\ManuallyValidatedFiles\ManuallyValidatedFiles-V2-16Jun"
OUTPUT_ENG_TEXT_FILENAME = "./eng_consolidated_file.txt"
OUTPUT_HINDI_TEXT_FILENAME = "./hindi_consolidated_file.txt"
data_eng = []
data_hindi = []

def write_consolidated_file(folder):
    eng_lines = 0
    hindi_lines=0
    firsttime_hindi = 1
    firsttime_eng = 1

    for dirpath,subdirectories,files in os.walk(folder):
        for file in files:
            #print(dirpath + '//' + file)
            openfile = open(dirpath + '//' + file, mode='r',encoding='utf-8',errors='replace')
            all_text = openfile.read()
            openfile.close()
            #print(all_text.count('\n'))
            #with open(file, "r", encoding="utf-8") as myfile:
            if ('eng' in file):
                if (firsttime_eng == 1):
                    f_eng = open(OUTPUT_ENG_TEXT_FILENAME, "w", encoding='utf-8')
                    firsttime_eng = 0
                else:
                    f_eng = open(OUTPUT_ENG_TEXT_FILENAME, "a", encoding='utf-8')
                    firsttime_eng = 0
                f_eng.write(all_text)
                f_eng.close()
                eng_lines = eng_lines + all_text.count('\n')
            else:
                if (firsttime_hindi == 1):
                    f_hindi = open(OUTPUT_HINDI_TEXT_FILENAME, "w", encoding='utf-8')
                    firsttime_hindi = 0
                else:
                    f_hindi = open(OUTPUT_HINDI_TEXT_FILENAME, "a", encoding='utf-8')
                    firsttime_hindi = 0
                f_hindi.write(all_text)
                f_hindi.close()
                hindi_lines = hindi_lines + all_text.count('\n')
                if (eng_lines!=hindi_lines):
                    print("Lines different")
    print('eng_lines',eng_lines)
    print('hindi_lines', hindi_lines)

def read_file_to_dataframe():
    #eng_dataframe = pd.read_fwf(OUTPUT_ENG_TEXT_FILENAME,width=None)
    with open(OUTPUT_ENG_TEXT_FILENAME, "r", encoding="utf-8") as myfile:
        data_eng.append(myfile.readlines())
    eng_dataframe = pd.DataFrame(data_eng).T

    #hindi_dataframe = pd.read_fwf(OUTPUT_HINDI_TEXT_FILENAME, width=None)
    with open(OUTPUT_HINDI_TEXT_FILENAME, "r", encoding="utf-8") as myfile_hindi:
        data_hindi.append(myfile_hindi.readlines())
    hindi_dataframe = pd.DataFrame(data_hindi).T

    print('eng_dataframe', eng_dataframe.shape)
    print('hindi_dataframe', hindi_dataframe.shape)
    #print(eng_dataframe.head,hindi_dataframe.head)
    return eng_dataframe,hindi_dataframe


root_folder = input("Enter the root folder where english, hindi files are kept: ")
write_consolidated_file(root_folder)
eng_dataframe,hindi_dataframe = read_file_to_dataframe()

X_train, X_test, y_train, y_test = train_test_split(eng_dataframe, hindi_dataframe, test_size=0.33)
print(X_train.shape,X_test.shape,y_train.shape, y_test.shape)
