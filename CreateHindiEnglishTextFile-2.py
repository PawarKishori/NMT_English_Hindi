#ReadMe
#1. Read an xls from aligned folder
#2. If the Xls has data in column G "AlignedText", start reading the column row by row
#3. Split the text data for delimiter ###. This is the delimiter for a single eng-hindi pair
#4. Split each eng-hindi pair for delimiter <=>.
#5 Write english sentence appended with a new line to xlsfilename_english.txt
#6. Write hindi sentence appended with a new line to xlsfilename_hindi.txt
#-----------------------------------------------------------------------------------#
import pandas as pd
import re
import os

ALIGNED_XLS_FOLDER = "./Aligned/"
HINDIENGLISH_TEXTFILES_FOLDER = "./HindiEnglishTextFiles/"
ENG_PATTERN_TOREPLACE = "\d+\)"
HINDI_PATTERN_TOREPLACE = "\d+\]"

def read_hindi_eng_text(txt):
    eng_hindi_pairs = str(txt).split("###")
    eng_sentences = []
    hindi_sentences = []

    for pair in eng_hindi_pairs:
        if(len(pair.split("<=>"))!=2):
            return eng_sentences,hindi_sentences
        eng_sentences.append(pair.split("<=>")[0])
        hindi_sentences.append(pair.split("<=>")[1])

    return eng_sentences,hindi_sentences

for filename in os.listdir(ALIGNED_XLS_FOLDER):
    sentence_data = pd.read_excel(ALIGNED_XLS_FOLDER + filename)
    #sentence_data = pd.read_excel(ALIGNED_XLS_FOLDER + "/E18_aligned.xlsx")
    col6_data = sentence_data.iloc[:, 6].values.tolist()
    col7_error_data = sentence_data.iloc[:, 7].values.tolist()

    split_up = os.path.splitext(filename)
    hindi_filename = split_up[0] + "_hindi.txt"
    eng_filename = split_up[0] + "_eng.txt"

    f_eng = open(HINDIENGLISH_TEXTFILES_FOLDER + eng_filename,"w",encoding='utf-8')
    f_hindi = open(HINDIENGLISH_TEXTFILES_FOLDER + hindi_filename,"w",encoding='utf-8')

    for index,txt in enumerate(col6_data):
        if ("ERROR" in str(col7_error_data[index])):
            continue
        if(len(str(txt).strip())==0):
            continue
        eng_sentence, hindi_sentence  = read_hindi_eng_text(txt)

        #if (len(eng_sentence)>0):
        for txt in eng_sentence:
            final_eng_sentence = re.sub(ENG_PATTERN_TOREPLACE,"",txt)
            f_eng.write(final_eng_sentence.strip() + "\n")


        #if (len(hindi_sentence) > 0):
        for txt in hindi_sentence:
            final_hindi_sentence = re.sub(HINDI_PATTERN_TOREPLACE,"",txt)
            f_hindi.write(final_hindi_sentence.strip() + "\n")

    f_eng.close()
    f_hindi.close()