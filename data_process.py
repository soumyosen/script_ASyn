import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

columns = ['Residue', 'N', 'C', 'CA', 'CB', 'CG', 'CD', 'CE', 'CZ', 'N_other']
expdf = pd.read_csv("expdata_mod2.dat", names=columns)
#print expdf

######### For each atom type create a separate dataframe ############################################
def extract_col_rename(df, col1, col2):
	df1 = df[[col1, col2]]
	df1.columns = [col1, 'Chemical_shift']
	df1['Atom_name'] = col2
	return df1

expdf_N = extract_col_rename(expdf, 'Residue', 'N')
expdf_C = extract_col_rename(expdf, 'Residue', 'C')
expdf_CA = extract_col_rename(expdf, 'Residue', 'CA')
expdf_CB = extract_col_rename(expdf, 'Residue', 'CB')
expdf_CG = extract_col_rename(expdf, 'Residue', 'CG')
expdf_CD = extract_col_rename(expdf, 'Residue', 'CD')
expdf_CE = extract_col_rename(expdf, 'Residue', 'CE')
expdf_CZ = extract_col_rename(expdf, 'Residue', 'CZ')
expdf_N_other = extract_col_rename(expdf, 'Residue', 'N_other')
#print expdf_N
######################################################################################################


########## Merging all the dataframes corresponding to each atom type ################################
dataframes = [expdf_N, expdf_C, expdf_CA, expdf_CB, expdf_CG, expdf_CD, expdf_CE, expdf_CZ, expdf_N_other]
combined_frame = pd.concat(dataframes, ignore_index=True)
#print combined_frame
######################################################################################################


########## Remove all the Nan and then separate out the name of amino acid and the resid in two diff cols
clean_frame = combined_frame.dropna(axis=0, how='any')
clean_frame['Amino_acid'], clean_frame['Resid'] = clean_frame['Residue'].str.split(':').str
#print clean_frame

clean_frame1 = clean_frame[['Amino_acid', 'Resid', 'Atom_name', 'Chemical_shift']].reset_index(drop=True)
#print clean_frame1
######################################################################################################


########## Removing those atoms which don't have unambiguous chemical shift
def check_two_shift(numarray):
	length = len(numarray)
	listrow = []
	for i in range(length):
		l = str(numarray[i]).split('/')
		lengthlist = len(l)
		if lengthlist > 1:
			listrow.append(i)
	
	return listrow


rows_with_2chemshift = check_two_shift(clean_frame1['Chemical_shift'])
#print rows_with_2chemshift
clean_frame2 = clean_frame1.drop(clean_frame1.index[rows_with_2chemshift]).reset_index(drop=True)
#print clean_frame2.dtypes
####################################################################################################


########### Change the atom type of other nitrogen of ASN65 and GLN79
clean_frame2.loc[192, 'Atom_name'] = "ND2"
clean_frame2.loc[193, 'Atom_name'] = "NE2"
#print clean_frame2
####################################################################################################

########## Sorting the table based on resid ########################################################
clean_frame3 = clean_frame2.sort_values(by=['Resid']).reset_index(drop=True)
#print clean_frame3	
####################################################################################################

######### Save data into a file
clean_frame3.to_csv("expdata_clean.csv", sep=" ", index=False)
####################################################################################################
