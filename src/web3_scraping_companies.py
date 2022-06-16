import requests
from bs4 import BeautifulSoup

companies = []
urls = [
    "https://web3.career/dev+remote-jobs",
    "https://web3.career/",
    "https://web3.career/?page=2",
    "https://web3.career/?page=3",
    "https://web3.career/?page=4",
    "https://web3.career/?page=5",
    "https://web3.career/?page=6",
    "https://web3.career/?page=7",
    "https://web3.career/?page=8",
    "https://web3.career/?page=9",
    "https://web3.career/?page=10",
    "https://web3.career/?page=11",
    "https://web3.career/?page=12",
    "https://web3.career/?page=13",
    "https://web3.career/?page=14",
    "https://web3.career/?page=15",
    "https://web3.career/?page=16",
    "https://web3.career/?page=17",
    "https://web3.career/?page=18",
    "https://web3.career/?page=19",
]


for url in urls: 

    print("--------------------")
    print("Scraping Companies from: " + url)
    req = requests.get(url)

    if req.status_code == 200:
        print("Successfully Scrapped")
    else:
        print("Failed")
        exit()

    soup = BeautifulSoup(req.text, 'html.parser')
    job_table = soup.find("table", class_ = "table table-borderless")

    for jobs in job_table.find_all('tbody'):
        rows = jobs.find_all('tr')
        
        for row in rows:
            company = row.find('div', class_ = "mt-auto d-block d-md-flex").text.strip()
            
            if company not in companies:
                companies.append(company)

with open('data/web3_companies_smart_contracts.txt', 'w') as file_handler:
    for company in companies:
        file_handler.write("{}\n".format(company))