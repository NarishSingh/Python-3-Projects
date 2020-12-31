# Webscraper workshop
# Date created: 12/30/20
# Last Modified: 12/30/20
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs  # a parsing library to clean up our request response

states = ["New-York", "New-Jersey", "Connecticut"]
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York'


def main() -> None:
    page = rq.get(URL)
    # print(page)
    # print(page.content)

    soup = bs(page.content, 'html.parser')
    # print(soup.prettify())  # makes it look like an html file in console
    # Can grab the first of
    # print(soup.title)  # can take divs
    # print(soup.p)  # can take html elements
    # print(soup.section)
    # print(soup.section.children)  # list of children divs

    # grab all divs from page soup
    # ps = soup.find_all('p')
    # for p in ps:
    #     print(p)

    job_list = []

    # GET ALL JOBS FROM URL
    results = soup.find('div', id='ResultsContainer')
    jobs = results.find_all('section', class_='card-content')
    for job in jobs:
        title = job.find('h2', class_='title')
        company = job.find('div', class_='company')
        location = job.find('div', class_='location')
        if None in (title, company, location):
            continue  # if field is null, this will ensure it doesn't screw our data

        a_tag = title.find('a')
        link = a_tag['href']

        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print(link)

        # GET DETAILS FROM SPECIFIC JOB PAGE - salary
        details = rq.get(link)
        detail_soup = bs(details.content, 'html.parser')
        money_divs = detail_soup.find_all(
            'div', class_='col-md-12 col-8 ta-md-l ta-r font-semibold')
        money_div = None
        salary = None
        for div in money_divs:
            if div['name'] == 'value_salary':
                money_div = div
                salary = money_div.text.strip()

        print(salary)
        print()

        job_list.append([title.text.strip(), company.text.strip(), location.text.strip(), salary, link])

    # MAKE INTO A DB
    jobs_df = pd.DataFrame(columns=['Title', 'Company', 'Location', 'Salary', 'Link'], data=job_list)
    jobs_df.to_csv("jobs.csv")


main()
