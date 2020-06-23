import requests
import sys
from bs4 import BeautifulSoup

while True:
    choice = input("1. Worldwide Search\n2. Country Search\nChoice: ")

    valuesList = []

    if choice == "1":
        print("Please wait...\n")
        total = requests.get("https://www.ovulation-calculators.com/coronavirus/")
        totalSrc = total.content
        soup = BeautifulSoup(totalSrc, "html.parser")

        for value in soup.find_all("a", href="#main_table_countries"):
            valuesList.append(value.text)

        for value in valuesList:
            if "cases" in value:
                cases = valuesList[0]
                cases = cases.replace("cases", "")

            elif "deaths" in value:
                deaths = valuesList[1]
                deaths = deaths.replace("deaths", "")

            # elif "active_cases" in value:
            #     print("hit")
            #     aCases = str(valuesList[2])
            #     aCases = aCases.replace("active_cases", "")

            else:
                recoveries = valuesList[3]
                recoveries = recoveries.replace("recoveries", "")

        print(f"[!] Total Covid-19 Cases: {cases}")
        print(f"[!] Total Covid-19 Deaths: {deaths}")
        #print(f"[!] Total Covid-19 Active Cases: {aCases}")
        print(f"[!] Total Covid-19 Recoveries: {recoveries}\n")

    elif choice == "2":
        countryChoice = input("Input country: ")
        print("Please wait...\n")
        country = requests.get(f"https://www.ovulation-calculators.com/coronavirus/{countryChoice.lower()}")

        countrySrc = country.content
        soup = BeautifulSoup(countrySrc, "html.parser")

        div = soup.find("div", {"class": "col-sm-6"})
        
        for value in div.find_all("tr"):
            valuesList.append(value.text)
        
        valuesList.pop(0)
        valuesList.pop(0)
        valuesList.pop(1)
        valuesList.pop(2)
        valuesList.pop(3)
        valuesList.pop(3)
        valuesList.pop(3)
        valuesList.pop(3)

        if valuesList[0] == " Confirmed coronavirus cases ":
            print("No country found.")

        else:
            confirmedCa = str(valuesList[0])
            confirmedCa = confirmedCa.replace(" Confirmed coronavirus cases ", "")
            confirmedDe = str(valuesList[1])
            confirmedDe = confirmedDe.replace(" Confirmed deaths ", "")
            recovered = str(valuesList[2])
            recovered = recovered.replace(" Recovered patients ", "")

            print(f"[!] Total Covid-19 Cases in {countryChoice.upper()}: {confirmedCa}")
            print(f"[!] Total Covid-19 Deaths in {countryChoice.upper()}: {confirmedDe}")
            print(f"[!] Total Covid-19 Recoveries in {countryChoice.upper()}: {recovered}\n")