import requests
from bs4 import BeautifulSoup

def getF1():
    URL = "https://www.formula1.com/en/results.html/2023/drivers.html"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('table', class_="resultsarchive-table")

    name_unref = []
    score_unref = []

    for result in results:
        name_unref = result.find_all('span')
        score_unref = result.find_all('td', {'class': 'dark bold'})

    name = []
    score = []

    for x in name_unref:
        name.append(x.text)

    for x in score_unref:
        score.append(x.text)

    full_name = []
    for x in range(0, len(name), 3):
        full_name.append(name[x] + ' ' + name[x+1])
    return full_name, score





