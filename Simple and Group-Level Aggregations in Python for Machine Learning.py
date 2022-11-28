# Tim Tarver
# This script is to demonstrate how to display Simple and Group-Level
# Aggregations for Machine Learning

# Data set best seen in Jupyter Notebooks; one method per cell. 

import pandas

# Constructor method for parameters.

def __init__(self, washers):

    self.washers = washers

    return washers

# First, lets read data from the given csv file called washers.csv
# and print out the information.

def read_and_print_info():

    washers = pandas.read_csv("washers.csv")
    washers.info()
    washers.head()
    return washers

# Secondly, we want to summarize certain characteristics using a Simple Aggregation

def summary_of_data():

    washers = pandas.read_csv("washers.csv")

    # The line below gives us the summary of number of non-missing values,
    # number of unique non-missing values, most commonly occuring value, and
    # frequency of the most commonly occuring value.
    washers[['BrandName']].describe()

    # The line below gives us the number of values with statistical measures.
    washers[['Volume']].describe()

    # The line below gives us how many time the brand name showed
    # up in the csv file.
    washers[['BrandName']].value_counts()

    # The line below summarizes which brand is bought and used the most.
    washers[['BrandName']].value_counts(normalize = True)

    # The line below tells us the mean of the calculated Volume above.
    washers[['Volume']].mean()
    
    return washers

# ----------------------------------------------------------------------------------
# Now on to the Group-Level Aggregations!
# First, lets group the Brand names by volume only.

def brand_names_by_volume():

    washers = pandas.read_csv("washers.csv")
    washers.groupby('BrandName')[['Volume']].mean()
    return washers

# Next, lets group the Brand names by least to greatest volume.

def brand_names_by_orderly_volume():

    washers = pandas.read_csv("washers.csv")
    washers.groupby('BrandName')[['Volume']].mean().sort_values(by = 'Volume')
    return washers

# Finally, lets group the Brand names by Mean, Median, Smallest
# and Largest Values using the agg() function for aggregation.

def brand_name_statistics():

    washers = pandas.read_csv("washers.csv")
    washers.groupby('BrandName')[['Volume']].agg(['mean', 'median', 'min', 'max'])
    return washers

    
    

    
# By the way, it's best to have one print line per cell (Jupyter Notebooks)

print(read_and_print_info())
print(summary_of_data())
print(brand_names_by_volume())
print(brand_names_by_orderly_volume())
print(brand_name_statistics())
