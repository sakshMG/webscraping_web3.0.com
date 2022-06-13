import requests
from bs4 import BeautifulSoup

companies = []

# urls = [
#     "https://web3.career/dev+remote-jobs",
#     "https://web3.career/",
#     "https://web3.career/?page=2",
#     "https://web3.career/?page=3",
#     "https://web3.career/?page=4",
#     "https://web3.career/?page=5",
#     "https://web3.career/?page=6",
#     "https://web3.career/?page=7",
#     "https://web3.career/?page=8",
#     "https://web3.career/?page=9",
#     "https://web3.career/?page=10",
#     "https://web3.career/?page=11",
#     "https://web3.career/?page=12",
#     "https://web3.career/?page=13",
#     "https://web3.career/?page=14",
#     "https://web3.career/?page=15",
#     "https://web3.career/?page=16",
#     "https://web3.career/?page=17",
#     "https://web3.career/?page=18",
#     "https://web3.career/?page=19",
# ]

# urls = ["https://web3.career/smart-contract-jobs"]

for url in urls: 

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    job_table = soup.find("table", class_ = "table table-borderless")

    for jobs in job_table.find_all('tbody'):
        rows = jobs.find_all('tr')
        for row in rows:
            company = row.find('div', class_ = "mt-auto d-block d-md-flex").text.strip()
            
            if company not in companies:
                companies.append(company)


with open('web3_companies.txt', 'w') as file_handler:
    for company in companies:
        file_handler.write("{}\n".format(company))