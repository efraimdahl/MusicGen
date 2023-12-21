################################################
###     Baroque Data Extraction Pipeline     ###
################################################


By performing this conversion and extraction pipeline, you will obtain two folders named 'json' and 'notes' containing all converted json files and extracted 
notes (CSV and Numpy files) from a given Baroque dataset.


1. Use 'get_names.py' with an additional argument referring to the folder path of any of the Baroque datasets (large trainset, testset, and testset_twopart):

python get_names.py PATH_TO_DATASET

This extracts all midi file names from the mentioned folder path. The namelist is saved in 'midi-names.txt'.


2. Use 'convert_sod.py' in the command-line as follows:

python convert_sod.py -n 'midi-names.txt' -i PATH_TO_DATASET -o 'json/'

This converts all midi files found in PATH_TO_DATASET to json files. All files are stored in the 'json' folder. Moreover, the names of all extracted 
json files are stored in 'json-names.txt'.


3. Use 'extract.py' in the command-line as follows:

python extract.py -n 'json-names.txt' -i 'json/' -o 'notes/'

This extracts all notes from the aforementioned json files. Every json file is extracted and saved as a CSV file and Numpy file. 
