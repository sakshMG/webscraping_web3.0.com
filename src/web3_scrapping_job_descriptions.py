from operator import delitem
import requests
import csv 
from bs4 import BeautifulSoup


data = {
    "companies" : [],
    "description" : []
}

BASE_URL = "https://web3.career"

'''
Append urls to this list 
e.g urls = ["url1", "url2", ...] 
'''
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
    data['description'].append(content)
    data['companies'].append(company)
    
    return 

'''
Write the desired file name  
'''
def writing_descriptions():
    with open('data/web3_descriptions_smartjobs.csv', 'w', newline='') as file_handler:
        writer = csv.writer(file_handler)
    
        writer.writerow(['Index', 'Company', 'Job Description'])
        for index, (company, descriptions) in enumerate(zip(data["companies"], data['description'])):
            writer.writerow([index, company, descriptions])

if __name__ == "__main__":
    extract_companies()
    writing_descriptions()
