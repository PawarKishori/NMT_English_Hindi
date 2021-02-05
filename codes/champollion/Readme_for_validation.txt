Sentence Alignment Validation Task
################################################################################################
The Sheet contains following Columns:

Column B: Sentence Alignment using Champollion (sentences)
		English sentences <=> Hindi Translation sentences (Using Champollion tool)
Column C: Sentence Alignment using Champollion (sentence_ids)
		English sentence ids <=> Hindi Translation sentences ids
		Both column B and C contains same information, one contains sentences and one contains the sentence ids.
Column D: Champollion_Correctness [1(if correct)/0(incorrect) ]
		This column to be filled, it's value is either 1 (if alignment content is correct) and 0 (if align. content is incorrect)
Column E: Corrected_Alignment
		If D is 0 then write the correct alignment in the similar format as of in C. if D is 1 just type NA in E.
Column F: BSA Predictions
		English sentence ids <=> Hindi Translation sentences ids (Using BSA tool)
Column G: BSA MAtching with Champollion or not
		This column to be filled, it's value is either 1 (if alignment content is present in column C) and 0 (if alignment content is not present in column C)
Column H: obsevation in BSA
Column I: Observations in Champollion
		For both H, mention any patterns of errors in alignment tool's output and write your comments.


Expected Outcome:
1) D, E, G, H,I These columns need to be filled.
2) Average time taken to validate sentence alignment (eg. X time for 10 mins)
