from bs4 import BeautifulSoup
import sys
import requests

office_id = {"President" : 1, "Senator" : 6, "Representative": 5}
search_site = "http://historical.elections.virginia.gov/elections/search/show_details:1/office_id:{}/stage:{}"
full_url = search_site.format(office_id['President'], 'General')

election_ids = []
election_years = []

req = requests.get(full_url)
soup = BeautifulSoup(req.text, 'lxml')

soup.find_all('tr', 'election_item')

#need to loop over all to get all the election IDs

for election in soup.find_all('tr', 'election_item'):
    identity = (election['id']).split('-')[-1]
    election_ids.append(identity)
    year = election.find('td', 'year first').text
    election_years.append(year)
#print(election_years)
#print(election_ids)

#open and close files
#options for the second argument are 'w' 'r' or 'a'/ write, read and append)
with open("ELECTION_ID", 'w') as f:
    for i in range(len(election_ids)):
        line = " ".join([election_years[i], election_ids[i]])
        f.write(line + "\n")
