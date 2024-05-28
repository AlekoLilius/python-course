import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_table(url):
    """Fetches the table of the site from the given url"""
    try:
        response = requests.get(url)

        # check if request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.find_all('table')
        else:
            raise Exception(f'Request failed with status code {response.status_code}')
    except Exception as e:
        print(e)

def fetch_mpg():
    """Fetches mpg data from https://www.fleetnews.co.uk/news/real-world-tests-reveal-cars-with-best-and-worse-mpg-fuel-economy"""
    tbody = fetch_table('https://www.fleetnews.co.uk/news/real-world-tests-reveal-cars-with-best-and-worse-mpg-fuel-economy')

    table_data, rows = {}, []
    for table in tbody: # loop through all tables
        rows += table.find_all('tr')[1:] # find all rows in each table and save everything except title row
    
    for row in rows: # loop through all rows
        cols = row.find_all('td') # find all columns in each row

        # add data to table
        table_data[cols[0].text.strip().lower()] = float(cols[1].text.strip().replace('mpg', ''))

    export = json.dumps(table_data)

    with open(os.path.realpath('final_project/web_files/cars_mpg.json'), 'w') as f:
        f.write(export)

def fetch_maintenance():
    """Fetches maintenance data from https://caredge.com/ranks/maintenance"""
    tbody = fetch_table('https://caredge.com/ranks/maintenance')

    table_data, rows = {}, []
    for table in tbody: # loop through all tables
        rows += table.find_all('tr')[1:] # find all rows in each table and save everything except title row
    
    for row in rows: # loop through all rows
        cols = row.find_all('td') # find all columns in each row

        # add data to table
        table_data[cols[1].text.strip()] = int(cols[2].text.strip().replace('$', '').replace(',', ''))

    export = json.dumps(table_data)

    with open(os.path.realpath('final_project/web_files/cars_maintenance.json'), 'w') as f:
        f.write(export)

