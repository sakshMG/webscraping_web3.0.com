import requests
from bs4 import BeautifulSoup

companies = []
description = []

BASE_URL = "https://web3.career"

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

urls = ["https://web3.career/smart-contract-jobs"]

def extract_companies():

    for url in urls: 

        print("Scraping URLs from: " + url)
        print("--------------------")
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        job_table = soup.find("table", class_ = "table table-borderless")

        for jobs in job_table.find_all('tbody'):
            rows = jobs.find_all('tr')
            
            for row in rows:

                company = row.find('div', class_ = "mt-auto d-block d-md-flex").text.strip()
                
                if company not in companies:
                    companies.append(company)

                lins_class = row.find('div', class_ = "mb-auto align-middle job-title-mobile")
                for link in lins_class.find_all('a'):
                    extract_job_description(link.get('href'), company)

def extract_job_description(link, company):

    url = BASE_URL + str(link)
    
    req = requests.get(url)

    if req.status_code == 200: 
        print("\tSuccessfully Scrapped Descriptions : " + url)
    else: 
        print("\tFailed")
        return
    
    soup = BeautifulSoup(req.text, 'html.parser')
    content = soup.find("div", class_ = "text-dark-grey-text p-2 p-md-0").text.strip()

    description.append(content) 
    return 

def writing_descriptions():
    with open('data/web3_descriptions_smartjobs.txt', 'w') as file_handler:
        for descriptions in description:
            file_handler.write("{}".format(descriptions))

if __name__ == "__main__":
    extract_companies()
    writing_descriptions()
