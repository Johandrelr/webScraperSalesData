# Process/ clean data scraped from Obos Websites

import pandas as pd
import json

# Import new scraped data & list of projectIDs
fileName = input('Enter file name:\n' + '(file needs to be in "CSV Output" folder \nDO NOT INCLUDE FILE TYPE)\n')
df = pd.read_csv('CSV Output\\' + fileName +'.csv') # import output from scrape
dfProjectIDs = pd.read_csv('CSV Input\\perloProjectIDs.csv') # import projectIDs

# Clean Data
# Hard to read column heading, remove 'Klikk for å sortere synkende eller stigende'
df.columns = df.columns.str.replace('Klikk for å sortere synkende eller stigende','')
df.columns = df.columns.str.replace(' ','') # Remove spaces to reduce bugs


# Create an empty data frame in the format we want to export at the end
dfAssemble = pd.DataFrame(columns = ['Project Name', 'Building Name', 'Unit Name', 'Sales Status', 'Sales Phase'])

# There are 2 columns with Project & Phase names in them, combine and then split the projectName and salesStage into seperate columns
df['salesStageName'] = df['salesStageName'].combine_first(df['Unnamed:23'])
df['projectName'] = df['salesStageName'].str.split(', ').str[0]
df['salesPhase'] = df['salesStageName'].str.split(', ').str[1]

# Add Cleaned columns to output data frame
dfAssemble['Project Name'] = df['projectName']
dfAssemble['Sales Phase'] = df['salesPhase']
dfAssemble['Building Name'] = df['BuildingName']
dfAssemble['Unit Name'] = df['Bolignr.']
dfAssemble['Sales Status'] = 'For Sale'
dfAssemble['Date-Time'] = pd.Timestamp.today().strftime('%Y-%m-%d %H:%M')

# Incorrect project name from scrape "Humla borettslag" change to "Vollebekk - Humla"
dfAssemble['Project Name'] = dfAssemble['Project Name'].replace('Humla borettslag','Vollebekk - Humla')
dfAssemble['Project Name'] = dfAssemble['Project Name'].replace('Ulvenkroken','Ulven T')

# Add project IDs to assemble dataframe
dfAssemble = dfAssemble.merge(dfProjectIDs, how='left')

# Export to CSV
newFileName = 'obosCleanedData' + '_'+str(pd.Timestamp.today().strftime('%Y-%m-%d'))+'.csv'
dfAssemble.to_csv('CSV Output\\' + newFileName, index=False)

# Get list of cleaned files
with open('CSV Output\\cleanedFileList.txt','r') as f:
    cleanedFileList = json.loads(f.read())

# Add new file name to data frame
cleanedFileList.append(newFileName)

# Add new file name to list
with open('CSV Output\\cleanedFileList.txt','w') as f:
    f.write(json.dumps(cleanedFileList))
