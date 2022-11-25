# This will be used to combine outputs of the scrape into one file

import pandas as pd
import json

masterData = pd.read_csv('CSV Output\\masterData_Obos.csv')


# Get list of files already added
with open('CSV Output\\filesAddedToMasterList.txt','r') as f:
    filesAddedToMasterList = json.loads(f.read())
dfFilesAddedToMasterList = pd.DataFrame(filesAddedToMasterList, columns= ['name'])

# Get list of all files/ cleaned data
with open('CSV Output\\cleanedFileList.txt','r') as f:
    cleanedFileList = json.loads(f.read())
dfCleanedFileList = pd.DataFrame(cleanedFileList, columns=['name'])

# Find names of files not yet added to master
dfFileToBeAdded = pd.concat([dfCleanedFileList, dfFilesAddedToMasterList]).drop_duplicates(keep=False)

# Orginal index is kept when concat functions is used, which effects the range functions used below
# Dataframe index needs to be reset after concat function is used
dfFileToBeAdded = dfFileToBeAdded.reset_index(drop= True)

# Add data from new files to master
for i in range(len(dfFileToBeAdded)):
    location = 'CSV Output\\' + dfFileToBeAdded.loc[i]['name']
    df1 = pd.read_csv(location)
    masterData = pd.concat([masterData, df1],ignore_index=True)
    
    # Add file name to list
    filesAddedToMasterList.append(dfFileToBeAdded.loc[i]['name'])
    

# Export master data csv
masterData.to_csv('CSV Output\\masterData_Obos.csv', index= False)

# Update added file list
with open('CSV Output\\filesAddedToMasterList.txt','w') as f:
        f.write(json.dumps(filesAddedToMasterList))