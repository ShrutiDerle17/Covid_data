# Project 1: Data Visualization of Covid analysis with csv file

# In this project, you will be working with a CSV file that contains data about the Covid-19 cases in a certain region. The CSV file will have columns for the date, the number of new cases, the number of deaths, and the number of recovered cases. 

# Your task is to read the data from the CSV file and create a dictionary for each day, with the date as the key and the other data as values. Then, you will create a list of these dictionaries. 

# You will then use this data to calculate and print the total number of cases, deaths, and recoveries. You will also calculate the average number of new cases per day. 

# Finally, you will use the random module to select a random day from the data and print the data for that day.

# Estimated time to complete: 60 minutes


# covid_data.csv:
# ```
# date,new_cases,deaths,recovered
# 2020-01-01,0,0,0
# 2020-01-02,0,0,0
# 2020-01-03,1,0,0
# 2020-01-04,0,0,0
# 2020-01-05,3,0,0
# 2020-01-06,0,0,1
# 2020-01-07,2,0,0
# 2020-01-08,1,0,0
# 2020-01-09,0,0,1
# 2020-01-10,1,0,0

#import required modules
import csv
import random
import copy

#step2: create a dictionary template
template = { 
    "date":"",
    "new.cases":0,
    "deaths":0,
    "recoverd":0
}

data = []

#step 3: open the csv file and read the data

with open ('Project1/covid_data.csv', 'r') as file:
    reader = csv.reader(file) 
    next(reader) #Skip the header row 
    for row in reader:
        day_data = copy.deepcopy(template)
        day_data["date"] = row[0]
        day_data["new_cases"] = int(row[1])
        day_data["deaths"] = int(row[2])
        day_data["recoverd"] = int(row[3])
        data.append(day_data)

#print(data)

#total_cases = sum(day["new_cases"]) for day in data
total_cases = 0

for day in data:
    total_cases += day["new_cases"]  #total_cases = sum(day["new_cases"] for day in data)

print(total_cases)

total_deaths = sum(day["deaths"] for day in data)

print(total_deaths)

average = total_cases / len(data)

print(average)


random_day = random.choice(data)
print(random_day['date'])
print(random_day['new_cases'])





