# Welcome to My First Scraper
***


## Task
This project focuses on fetching and processing the top 25 trending repositories from Github. It utilizes Python libraries requests and 
beautifulsoup4 to request, extract, transform, and format the trending repository data into a CSV format.


## Description
1. request_github_trending

Makes an HTTP request to Github's trending repositories page and returns the raw HTML response.
Prototype: def request_github_trending(url: str) -> requests.Response

2. extract

Extracts repository rows from the HTML response using BeautifulSoup and returns them for further processing.
Prototype: def extract(page: requests.Response) -> list

3. transform

Transforms the extracted repository rows into a structured array of dictionaries.
Prototype: def transform(html_repos: list) -> list

4. format

Formats the structured data into a CSV string.
Prototype: def format(repositories_data: list) -> str


## Installation
Follow these steps to install and run the project:
1. Install requests library
```pip install requests```
2. Install BeautifulSoup
```pip install beautifulsoup4```
3. Clone the repository:
```git clone https://git.us.qwasar.io/my_first_scraper_173761_xatejy/my_first_scraper.git```
4. Navigate to the project directory
```cd my_first_scraper.git```
5. Ensure Python is installed on your machine.


## Usage
To launch the project run the script:
```python my_first_scraper.py```


### The Core Team
Pashko Yevheniia
https://git.us.qwasar.io/pashko_y

Diogo Oliveira

Pablo Samuel