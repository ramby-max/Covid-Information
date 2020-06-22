import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ovulation-calculators.com/coronavirus/")

src = r.content

soup = BeautifulSoup(src, "html.parser")

valuesList = []

for value in soup.find_all("a", href="#main_table_countries"):
    valuesList.append(value.text)

print(f"[!] Total Covid-19 Cases: {valuesList[0]}\n")
print(f"[!] Total Covid-19 Deaths: {valuesList[1]}\n")
print(f"[!] Total Covid-19 Active Cases: {valuesList[2]}\n")
print(f"[!] Total Covid-19 Recoveries: {valuesList[3]}\n")