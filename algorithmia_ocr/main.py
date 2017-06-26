import requests
from config import key

URL="https://www.googleapis.com/customsearch/v1?q=lolcat&cx=016367925189187468689%3Aghvlq4-mi7e&searchType=image&key="+key
r=requests.get(URL)
print(r.text)
