# webScraper
This is my first python project. The objective is to scrape data from property developer site to compile 
sales data for use in another application. 

obos_webscrapers_bs4.py
My first attempt was using Beautiful Soup and Request library. This failed as the table was not included in the page source code. 
(Assuming this means the page is server side redered but this is a little out of my knowledge base)

obos_webscraper_silenium.py
Second attempt using selenium to load the page and the scrape with Beautifull soup. This worked. 
The code takes a list of building URLs urlsList_Obos.csv  in project for sale as input and outputs a csv  

obos_scrapeddata_processing.py
Cleaning and formatting the data to prepare it for adding to the final database. 
Additionally adds project ID to units for sale, this is for external function. Uses perloProjectIDs.csv as input.

obos_data_mergetomaster.py
Adds data scraped to a master data sheet called masterData_Obos.csv which is the final output of the project.
Uses cleanedFileList.txt & filesAddedToMasterList.txt as inputs. 

Limitation
1. No real error catching.
2. Requires manual sequential running of scraping, then processing, then combining.
3. Can only run once a day (Need to add time to allow for more than once per day.)
