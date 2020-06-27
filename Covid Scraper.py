import requests
import sys
from bs4 import BeautifulSoup
from tkinter import *

root = Tk()

root.title("Covid Scraper")
root.configure(width=200, height=300, background="#581845")
wasShown = False

def on_click():
    if choice.get() == "1":
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

        casesLabel = Label(text=f"[!] Total Covid-19 Cases: {cases}", background="#581845")
        deathsLabel = Label(text=f"[!] Total Covid-19 Deaths: {deaths}", background="#581845")
        #print(f"[!] Total Covid-19 Active Cases: {aCases}")
        recoveriesLabel = Label(text=f"[!] Total Covid-19 Recoveries: {recoveries}", background="#581845")

        casesLabel.pack()
        deathsLabel.pack()
        recoveriesLabel.pack()

    elif choice.get() == "2":
        countryChoice = Entry(root, text="Input the country you want to search: ")
        countryChoice.pack()

        if len(countryChoice.get()) == 0:
            pass

        else:
            countryString = countryChoice.get()

            country = requests.get(f"https://www.ovulation-calculators.com/coronavirus/{countryChoice.get()}")

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

                confirmedCaLabel = Label(root, text=f"[!] Total Covid-19 Cases in {countryString.upper()}: {confirmedCa}", background="#581845")
                confirmedDeLabel = Label(root, text=f"[!] Total Covid-19 Deaths in {countryString.upper()}: {confirmedDe}", background="#581845")
                recoveredLabel = Label(root, text=f"[!] Total Covid-19 Recoveries in {countryString.upper()}: {recovered}", background="#581845")

                confirmedCaLabel.pack()
                confirmedDeLabel.pack()
                recoveredLabel.pack()

choice = StringVar()
worldWideRadio = Radiobutton(root, text="Worldwide Search", value="1", variable = choice, background="#581845")
countryRadio = Radiobutton(root, text="Search by Country", value="2", variable = choice, background="#581845")
worldWideRadio.pack()
countryRadio.pack()

goButton = Button(root, text="Search", command=on_click, background="#581845")
goButton.pack()

valuesList = []

root.minsize(width=600, height=400)
root.maxsize(width=600, height=400)

root.mainloop()