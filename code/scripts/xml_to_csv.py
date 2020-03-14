
import os
import pandas as pd
from bs4 import BeautifulSoup



files = os.listdir('../XML/')


dataframe = []

for file in files:

    if not file.startswith('.'): # This was breaking when it got to .DS_Store, so this was added to ignore hidden files
        
        print(file)
        
        infile = open("../XML/"+file,"r") # Opens the file
        contents = infile.read() # Reads the file
        soup = BeautifulSoup(contents,'xml') # BeautifulSoup's the file

        names = []
        for i in range(len(soup.find_all('name'))): # This loop goes through and finds the boxes I dres, and puts them into a dictionary
            coords = {'type' : soup.find_all('name')[i].text,
                      'xmin' : soup.find_all('xmin')[i].text,
                      'xmax' : soup.find_all('xmax')[i].text,
                      'ymin' : soup.find_all('ymin')[i].text,
                      'ymax' : soup.find_all('ymax')[i].text,
                      'photo' : file}

            names.append(coords)
        dataframe.append(pd.DataFrame(names)) # Makes one big happy DataFrame


df = pd.concat(dataframe)

df.to_csv('../data/imagesmarked.csv', index = False) # Saves as a CSV
