import subprocess

from bs4 import BeautifulSoup
from config import Configs
import pandas as pd
import requests
import re


class Covid:
    def __init__(self, covid_type, user_response=None):
        self.covid_type = covid_type
        self.user_response = user_response

    @staticmethod
    def getNumbers(str):
        array = re.findall(r'[0-9]+', str)
        return array

    @staticmethod
    def concatonator(a_list):
        result = ""
        for x in a_list:
            result += str(x)

        return "{:,d}".format(int(result))

    def decodeHelper(self):
        if self.user_response == "" or None:
            return "Please enter an appropriate response."
        else:
            proc = subprocess.Popen(self.user_response.content, shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
            stdout_value = (proc.stdout.read() + proc.stderr.read()).decode("utf-8")

            return stdout_value.split(" ")[2].replace(":", "")

    def grabCovidHtml(self):
        covid_list = []

        html_content = requests.get(Configs.COVID_URL).text
        html_response = BeautifulSoup(html_content, "lxml")

        if self.covid_type == "main":

            for x in html_response.find_all("div", attrs={"class": "maincounter-number"}):
                covid_list.append(str(x))

            return covid_list
        elif self.covid_type == "country":
            df = pd.read_html(html_content)[0][["Country,Other", "TotalCases", "TotalDeaths", "TotalRecovered"]]
            print(df)
            print(self.decodeHelper())
            return df.loc[df["Country,Other"] == self.decodeHelper()]

    def grabCountryInfectionCount(self):

        if self.user_response is None:
            return "No input offered, try again"
        else:
            df = self.grabCovidHtml()
            return df.set_index("Country,Other").to_dict()

    def grabTotalConfirmed(self):
        covid_list = self.grabCovidHtml()

        return Covid.concatonator(Covid.getNumbers(covid_list[0]))

    def grabTotalDead(self):
        covid_list = self.grabCovidHtml()

        return Covid.concatonator(Covid.getNumbers(covid_list[1]))

    def grabTotalRecovered(self):
        covid_list = self.grabCovidHtml()

        return Covid.concatonator(Covid.getNumbers(covid_list[2]))