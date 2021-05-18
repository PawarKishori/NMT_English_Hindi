#ReadMe
#For each file in xlsx/tsv/ods format:

#get_formatted_complete_text_dataframe:
#Read the complete file for (1) columnwise data (2) textdata in string format such that each row text separated by "<=>>".
#Perform basic validation like file has at least 4 columns etc.
#Name the columns in the file for further operations

#get dictionary for text
# Get the complete text from teh above method. (This is complete text of column1, rowwise separated by "<=>" )
# Create hindi, english dictionary for this text.
# The dictionary contains sentence id as key, and corresponding sentence as text

#get_processed_dataframe:
#Read the column2,3.
# - If column 3 is 1, get the text from column1 as aligned text.
# - If column 3 is 0, then read column 2, and create alignedtext from the eng, hindi dictionary.
#Add this alignedtext as a new column in the dataframe.

#Write the processed complete dataframe to a new xls in specified folder.
#The new file has the same name as parent file appended with "_aligned"
#Perform the same process for all files in the data folder

#----------------------------------------------------------------------------------------------------#

import numpy as np
import pandas as pd
import re
import os
from pandas_ods_reader import read_ods

def get_hindi_eng_dictionary(full_str):
    eng_dict = {}
    hindi_dict = {}

    eng_list = []
    hindi_list = []
    eng_flg = 1  # this flag is used for sentences with missing id.

    eng_hindi_pairs = full_str.split("<=>")
    for pair in eng_hindi_pairs:
        eng_hindi_sentences = pair.split("##")
        for sentence in eng_hindi_sentences:
            sentence = sentence.strip()

            if (sentence == "omitted"):
                continue

            if re.search('^\d+\)', sentence):
                id = re.findall('^\d+\)', sentence)[0]
                txt = sentence[len(id):len(sentence)]
                # end sentence, put in eng dict
                eng_dict[int(id.strip(')'))] = txt
                eng_flg = 1
            elif re.search('^\d+\]', sentence):
                id = re.findall('^\d+\]', sentence)[0]
                txt = sentence[len(id):len(sentence)]
                # end sentence, put in eng dict
                hindi_dict[int(id.strip(']'))] = txt
                eng_flg = 0
            else:  # this means the sentence does not have an id,
                # if (is_english(sentence)):
                if eng_flg == 1:
                    key = int(list(eng_dict.keys())[-1]) + 1
                    eng_dict[key + 1] = sentence
                else:
                    key = int(list(hindi_dict.keys())[-1]) + 1
                    hindi_dict[key + 1] = sentence

    return eng_dict,hindi_dict

def get_modified_text_from_dict(_final_alignment):
    #_final_alignment = "119=82;120,121=83, "
    _final_text = ""
    detail_error_text = ""
    alignments = _final_alignment.split(';')

    # run the loop for each pair of alignment eg. 3,4=4,5;5=6
    for i in alignments:
        if (len(i) == 0):
            continue

        _ehSentenceID = i.split('=')
        if (len(_ehSentenceID) != 2):
            detail_error_text = ERROR_TEXT + "Invalid sentence Id"
            return _final_text, detail_error_text
        _eng_Id = _ehSentenceID[0]
        _hin_Id = _ehSentenceID[1]

        # Below variables contain comma separated ids of eng and hindi sentences respectively
        _eng_individual_id = _eng_Id.split(',')  # eg. 3,4
        _hin_individual_id = _hin_Id.split(',')  # eg. 4,5

        _eng_text = ""
        _hin_text = ""

        # the flag is set if any of the eng or hindi ids do not exist in the text. The pair of eng-hindi ids is dropped in such case
        _id_missing_error_flg = 0
        _id_invalid_error_flg = 0

        for l in _eng_individual_id:  # eng sentences for the comma separated eng ids are concatinated
            #l = l.strip().strip(',')
            if (len(l)==0):
                continue
            try:
                _id = int(l)
            except:
                _id_invalid_error_flg = 1
                continue
            try:
                _eng_text = _eng_text + str(_id) + ")" + eng_dict_global[_id]
            except KeyError:
                _id_missing_error_flg = 1

        for l in _hin_individual_id:  # eng sentences for the comma separated eng ids are concatinated
            #l = l.strip().strip(',')
            if (len(l)==0):
                continue
            try:
                _id = int(l)
            except:
                _id_invalid_error_flg = 1
                continue
            try:
                _hin_text = _hin_text + str(_id) + "]" + hindi_dict_global[_id]
            except KeyError:
                _id_missing_error_flg = 1

        eng_hindi_pair = _eng_text + "<=>" + _hin_text

        if (len(_final_text)==0):
            _final_text = eng_hindi_pair
        else:
            _final_text = _final_text + "###" + eng_hindi_pair

        if (_id_missing_error_flg == 1):
            detail_error_text = ERROR_TEXT + "Some of the sentence ids not found "
        if (_id_invalid_error_flg == 1):
            detail_error_text = ERROR_TEXT + "Some of the ids are invalid "

    return _final_text, detail_error_text

#
# Assumption: Text cell contains text in order of english first and then hindi
# A new hindi sentence starts with a delimiter <=> while a new english senetence has a delimiter ##
#Below method returns the final correct pairs of english, hindi sentences and "ERROR" text if there is any error in processing
#Input: the correct alignment for a row eg. 3=4;4=5,6
def get_modified_text(_final_alignment):
    # print(full_text_str)
    # print("\n---------------------\n")
    _final_text = ""
    detail_error_text = ""
    alignments = _final_alignment.split(';')

    # run the loop for each pair of alignment eg. 3,4=4,5;5=6
    for i in alignments:
        if (len(i)==0):
            continue

        _ehSentenceID = i.split('=')
        if (len(_ehSentenceID) != 2):
            detail_error_text = ERROR_TEXT + "Invalid sentence Id"
            return _final_text,detail_error_text
        _eng_Id = _ehSentenceID[0]
        _hin_Id = _ehSentenceID[1]

        # Below variables contain comma separated ids of eng and hindi sentences respectively
        _eng_individual_id = _eng_Id.split(',')  # eg. 3,4
        _hin_individual_id = _hin_Id.split(',')  # eg. 4,5

        _eng_text = ""
        _hin_text = ""

        # the flag is set if any of the eng or hindi ids do not exist in the text. The pair of eng-hindi ids is dropped in such case
        _hin_error_flg = 0
        _eng_error_flg = 0

        for l in _eng_individual_id:  # eng sentences for the comma separated eng ids are concatinated
            #if l is not integer, move to the next id
            try:
                i = int(l)
            except ValueError:
                continue

            _id_pos = full_text_str.find(l.strip() + ')')

            if (_id_pos < 0):  # if id not found set the error flag and skip the remaining steps for the loop
                _eng_error_flg = 1
                continue
            # _id_pos_end_eng = full_text_str.index("##",_id_pos)
            # _id_pos_end_hin = full_text_str.index("<=>",_id_pos)
            _id_pos_end_eng = full_text_str.find("##",
                                                 _id_pos)  # Find index of first numbered english sentence after the current eng sentence
            _id_pos_end_hin = full_text_str.find("<=>",
                                                 _id_pos)  # Find index of first numbered hindi sentence after the current eng sentence

            if (_id_pos_end_eng < 0 & _id_pos_end_hin < 0):  # this means that current sentence is the last in the text.
                _id_pos_end = len(full_text_str) - 1
            elif _id_pos_end_eng < 0:  # Take the position of first hindi or eng sentence, whichever occurs first after the current english sentence
                _id_pos_end = _id_pos_end_hin
            elif _id_pos_end_hin < 0:
                _id_pos_end = _id_pos_end_eng
            else:
                _id_pos_end = _id_pos_end_eng if _id_pos_end_eng < _id_pos_end_hin else _id_pos_end_hin

                # if(_id_pos_end > 0):
            # _eng_text = _eng_text + full_text_str[_id_pos:_id_pos_end]
            # print('_id_pos',_id_pos)
            # print('_id_pos_end',_id_pos_end)
            # else
            _eng_text = _eng_text + full_text_str[
                                    _id_pos:_id_pos_end]  # Extract the current eng sentence from the whole text
            # print('_eng_text',_eng_text)

        for l in _hin_individual_id:  # hindi sentences for the comma separated hindi ids are concatinated
            # if l is not integer, move to the next id
            try:
                i = int(l)
            except ValueError:
                continue

            _id_pos = full_text_str.find(l.strip() + ']')

            if (_id_pos < 0):  # if id not found or error flag is already set and skip the remaining steps for the loop
                _hin_error_flg = 1
                continue
            # _id_pos_end_eng = full_text_str.index("##",_id_pos)
            # _id_pos_end_hin = full_text_str.index("<=>",_id_pos)
            _id_pos_end_eng = full_text_str.find("##", _id_pos)
            _id_pos_end_hin = full_text_str.find("<=>", _id_pos)
            #print('_id_pos_end_eng', _id_pos_end_eng)
            #print('_id_pos_end_hin', _id_pos_end_hin)
            if _id_pos_end_eng < 0 & _id_pos_end_hin < 0:  # this means that current sentence is the last in the text.
                _id_pos_end = len(full_text_str) - 1
            elif _id_pos_end_eng < 0:  # Take the position of first hindi or eng sentence, whichever occurs first after the current english sentence
                _id_pos_end = _id_pos_end_hin
            elif _id_pos_end_hin < 0:
                _id_pos_end = _id_pos_end_eng
            else:
                _id_pos_end = _id_pos_end_eng if _id_pos_end_eng < _id_pos_end_hin else _id_pos_end_hin

            _hin_text = _hin_text + full_text_str[_id_pos:_id_pos_end]
            #print('_hin_text', _hin_text)
            #print('_eng_text', _eng_text)
        eng_hindi_pair = _eng_text + "<=>" + _hin_text
        # print ("eng_hindi_pair",eng_hindi_pair)
        # print("\n---------------------\n")

        if (len(_final_text)==0):
            _final_text = eng_hindi_pair
        else:
            _final_text = _final_text + "###" + eng_hindi_pair

        if (_eng_error_flg == 1 or _hin_error_flg == 1):
            detail_error_text = ERROR_TEXT + "Some of the sentence ids not found "

        # print("_final_text end of loop")
        # print(_final_text)
        # print("\n---------------------\n")
    return _final_text,detail_error_text

#Below method reads the first column of the input file, formats the text , reads the complete dataframe-
# - remove text within {}
#Input: file name in xls/csv format
#Output: formatted text, dataframe for the input file
def get_formatted_complete_text_dataframe(filename):
    cols = [0, 1, 2, 3, ]
    if (xls_tsv_ods == "100"):
        sentence_data = pd.read_excel(INPUT_DATA_DIRECTORY + "/" + filename,header=None)
        col_num = len(sentence_data.columns)
    elif (xls_tsv_ods == "010"):
        sentence_data = pd.read_csv(INPUT_DATA_DIRECTORY + "/" + filename,sep='\t',header=None)
        col_num = len(sentence_data.columns)
    elif (xls_tsv_ods == "001"):
        sentence_data = read_ods(INPUT_DATA_DIRECTORY + "/" + filename,1,headers=False)
        col_num = len(sentence_data.columns)
    else:
        raise Exception("Unknown file format:" + filename)
        return


    if (col_num<4):
        print("File having less than 4 columns:" + filename)
        return None,None

    #Sometimes col_num is coming as >4 even if it is not a user processed file
    col3_data = sentence_data.iloc[:, 2].values.tolist()
    col4_data = sentence_data.iloc[:, 3].values.tolist()

    correct_no_columns = 0
    for i in range(len(col3_data)):
        if (len(str(col3_data[i]).strip())>0 or len(str(col4_data[i]).strip())>0 ):
            correct_no_columns = 1
            break

    if (correct_no_columns==0):
        print("File having less than 4 columns:" + filename)
        return None,None

    while col_num<6:    #This code is required to add 2 more columns Exception, ExceptionDetails because some of the colunteers are not updating these columns
        sentence_data[col_num] = np.nan
        col_num+=1

    #Add headers to dataframe
    sentence_data.columns = ['Text', 'Alignment', 'Correction', 'FinalAlignment', 'Exception','ExceptionDetails']
    # Read all text from column 1 into a string
    full_text_list = sentence_data.iloc[:, 0].values.tolist()

    for i in range(len(full_text_list)):
        full_text_list[i] = str(full_text_list[i])

    #full_text_str_raw = "##".join(full_text_list)
    full_text_str_raw = "<=>".join(full_text_list)

    # Remove all the content which is enclosed in {}
    full_text_str = re.sub(pattern_to_replace, "", full_text_str_raw)

    return full_text_str,sentence_data

#Below method reads the dataframe, row by row,and creates a new dataframe by appending new columns
#Input: dataframe of input file in xls/csv
#output: new dataframe with finalalignment and error column
def get_processed_dataframe(_complete_dataframe):
    new_alignment_column = []
    error_text_column = []
    for i in _complete_dataframe.index:
        # print('i is',i)
        _text = _complete_dataframe.iloc[i, 0]
        _correct = _complete_dataframe.iloc[i, 2]
        _final_alignment = _complete_dataframe.iloc[i, 3]
        pattern_alignment_1case = "^(\d,)*\d=(\d,)*\d$" #2,3,4=5,6,7 or 3=4
        pattern_alignment_2case = "^((\d,)*\d=(\d,)*\d;)*((\d,)*\d=(\d,)*\d);*$"  #2,3=4,5;4,5,6=1,2;
        if (str(_correct) == "1" or _correct == 1  ):
            # sentence_data_updated.insert(3,"column1",_text)
            _text = re.sub(pattern_to_replace, "", _text)
            _text = re.sub("##", "", _text)
            new_alignment_column.append(_text)
            error_text_column.append("")
        elif (str(_correct) == "0" or _correct == 0):
            _acceptable_chars = ['-','"-"',"'-'",'nan']
            if ((str(_final_alignment).strip() in _acceptable_chars)  or len(str(_final_alignment).strip()) == 0 or type(_final_alignment)==type(None)):
                new_alignment_column.append("")
                error_text_column.append("")
                continue
            elif (type(_final_alignment) != str or len(_final_alignment) < 3):
                new_alignment_column.append("")
                error_text_column.append(ERROR_TEXT + "final alignment not in correct format")
                continue

            #new_text,error_text = get_modified_text(_final_alignment)
            new_text, error_text = get_modified_text_from_dict(_final_alignment)
            new_alignment_column.append(new_text)
            error_text_column.append(error_text)
        else:
            new_alignment_column.append("")
            error_text_column.append(ERROR_TEXT + "Correction column not in correct format")

    # Append the new column to dataframe and write to excel
    processed_df = _complete_dataframe.assign(AlignedText=new_alignment_column,ErrorText=error_text_column)
    return processed_df


INPUT_DATA_DIRECTORY = "./Data"
OUTPUT_DATA_DIRECTORY = "./Aligned"
ERROR_TEXT ="ERROR: "
FILES_NOT_PROCESSED_ERROR = "Below files could not be processed-"
files_not_processed_names = ""
full_text_str = ""
eng_dict_global = {}
hindi_dict_global = {}

xls_tsv_ods= ""
pattern_to_replace = "{[^{]*}"

for filename in os.listdir(INPUT_DATA_DIRECTORY):
    if (filename.endswith(".xlsx")):
        xls_tsv_ods= "100"
    elif (filename.endswith(".tsv")):
        xls_tsv_ods = "010"
    elif (filename.endswith(".ods")):
        xls_tsv_ods = "001"
    else :
        print("Unknown file format:", filename)
        files_not_processed_names += "\n Unknown file format:" + filename
        continue
    #Read the file data in a dataframe
    full_text_str,sentence_data = get_formatted_complete_text_dataframe(filename)
    if (type(full_text_str) == type(None) or type(sentence_data) == type(None)):
        files_not_processed_names += "\n Insufficient data:" + filename
        continue

    print("Currently processing..." + filename)

    # Get dictionary
    eng_dict_global, hindi_dict_global = get_hindi_eng_dictionary(full_text_str)
    print(" -hindi, eng dictionary created")
    #Format the dataframe to get a processed frame
    processed_df = get_processed_dataframe(sentence_data)

    print(" -processed dataframe")

    #Write the processed dataframe to a new file
    split_up = os.path.splitext(filename)
    newfilename = split_up[0] + "_aligned" + '.xlsx'
    newfile_fullname = OUTPUT_DATA_DIRECTORY + '/' + newfilename
    processed_df.to_excel(newfile_fullname, index=False)

    print(" -xls file created")

#Print error/success statements at the end
if (len(files_not_processed_names)>0):
    print(FILES_NOT_PROCESSED_ERROR,files_not_processed_names)
