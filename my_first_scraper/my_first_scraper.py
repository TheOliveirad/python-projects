import requests
from bs4 import BeautifulSoup


def request_github_trending(url):
    response = requests.get(url)
    return response


def extract(page):
    soup = BeautifulSoup(page.text, "html.parser")
    repository_rows = soup.find_all('article', class_="Box-row")
    return repository_rows


def transform(html_repos):
    result_list = []

    for row in html_repos:
        
        row_link = row.find('h1', class_='h3 lh-condensed').find('a')

        names_list = row_link['href'].strip('/').split('/')
        developer_name = names_list[0]
        repo_name = names_list[1]

        stars_tag = row.find('a', href=lambda href: href and '/stargazers' in href)
        nbr_stars = stars_tag.get_text(strip=True)

        result_list.append({
            'developer': developer_name,
            'repository_name': repo_name,
            'nbr_stars': nbr_stars
        })

    return result_list


def format(result_list):
    columns = ["Developer", "Repository Name", "Number of Stars"]
    rows = []

    csv_output = ",".join(columns) + '\n'

    for row in result_list:
        row_data = [row['developer'], row['repository_name'], row['nbr_stars']]
        rows.append(",".join(row_data))

    csv_output += "\n".join(rows) + '\n'
    return csv_output
  

GITHUB_URL = 'https://storage.googleapis.com/qwasar-public/track-ds/trending_14_06_2022'
page = request_github_trending(GITHUB_URL)
rows_list = extract(page)
dict_list = transform(rows_list)
format(dict_list)