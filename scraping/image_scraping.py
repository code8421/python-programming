import requests
from bs4 import BeautifulSoup


github_user = input('Input GitHub User : ')
url = f'https://github.com/{github_user}'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)
