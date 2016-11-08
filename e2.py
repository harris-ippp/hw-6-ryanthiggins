#this opens the previous file so that we can plug it into the link and gather the election data
from bs4 import BeautifulSoup
import sys
import requests

election_years = []
election_ids = []

for line in open("ELECTION_ID"):
    codes = line.split()[-1]
    full_url = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(codes)
    req = requests.get(full_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    soup = str(soup)

    year = line.split()[0]
    file_name = year + ".csv"
    with open(file_name, "w") as out:
        out.write(soup)


#with open("ELECTION_ID", 'r') as f:
#    for line in f:
#        info = line.split()
#        year = line.split()[0]
#        codes = line.split()[1]
#
#        year = election_years.append(info[0])
#        election_ids.append(info[1])
#
#download_site = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"


#for codes in election_ids:
#        full_url = download_site.format(codes)
#        req = requests.get(full_url)
#        soup = BeautifulSoup(req.text, 'lxml')
#        file_name = year + ".csv"
#        with open(file_name, "w") as out:
#            out.write(req.text)
