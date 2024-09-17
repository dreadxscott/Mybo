#a program for getting data out of a csv and into a pandas dataframe
import pandas as pd
import tabulate

#a function read the contents of our data file into a pandas dataframe
def csvReader(filepath, sep = ','):
    #create a dataframe from the datafile
    df = pd.read_csv(filepath, sep=sep)

    #Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    #get column names and iterate through them to replace null values
    column_names = df.columns
    for column in column_names:
        df[column] = df[column].fillna('')
    
    #set number of points for each to three
    df['points'] = 3
    print(df.to_markdown())
    return df



filepath1 = r"C:\Users\colli\Python\Mybo\yukidaruma_wordbank_data.txt"
filepath2 = r"C:\Users\colli\Python\Mybo\yukidaruma_sentencebank_data.txt"

words = csvReader(filepath1)

for row in words.iterrows():
    if row[1]['katakana']: print(row[1]['katakana'])