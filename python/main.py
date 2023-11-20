# imports and modules
# import csv
from bs4 import BeautifulSoup
import requests

# page requests and query get
#query = input("please enter the search words : ")
page = requests.get(f"https://devdocs.io/css/")


def main(urlpage):
    src = urlpage.content

    soup = BeautifulSoup(src, "lxml")

    # prefer_results_get[]
    results = soup.find_all("div", {'class': '_page_mdn'})
    print(results)


main(page)
