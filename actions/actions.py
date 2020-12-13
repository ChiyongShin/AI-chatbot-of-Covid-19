# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pymysql
import webbrowser
a1 = ""
t1 = ""
p1 = 0
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionCoronaInformation(Action):

    def name(self) -> Text:
        return "action_corona_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        print(entities)
        iurl = ""
        conn = pymysql.connect(host="localhost", user="root", password="root", db="db")
        curs = conn.cursor()
        sql1 = ""
        for e in entities:
            if e['entity'] == 'corona_info':
                name = e['value']
                global a1
                global p1
                if name == "definition of corona":
                    a1 = 1
                    p1 = 1
                if name == "corona disease classification":
                    a1 = 2
                    p1 = 1
                if name == "corona pathogen":
                    a1 = 3
                    p1 = 1
                if name == "corona radio path":
                    a1 = 4
                    p1 = 1
                if name == "corona incubation period":
                    a1 = 5
                    p1 = 1
                if name == "diagnosis criteria for corona":
                    a1 = 6
                    p1 = 1
                if name == "symptoms of corona":
                    a1 = 7
                    p1 = 1
                if name == "corona treatment":
                    a1 = 8
                    p1 = 1
                if name == "what is corona":
                    a1 = 9
                    p1 = 1
                if name == "corona type":
                    a1 = 10
                    p1 = 1
                if name == "corona form":
                    a1 = 11
                    p1 = 1
                if name == "i want to know the human infection corona":
                    a1 = 12
                    p1 = 1
                if name == "corona genus":
                    a1 = 13
                    p1 = 1
                if name == "human infection corona virus":
                    a1 = 14
                    p1 = 1

        if (a1 == 1):
            sql1 = "select def from info_corona_db"
        elif (a1 == 2):
            sql1 = "select disease_classification from info_corona_db"
        elif (a1 == 3):
            sql1 = "select pathogen from info_corona_db"
        elif (a1 == 4):
            sql1 = "select radio_path from info_corona_db"
        elif (a1 == 5):
            sql1 = "select incubation_period from info_corona_db"
        elif (a1 == 6):
            sql1 = "select diagnostic_stand from info_corona_db"
        elif (a1 == 7):
            sql1 = "select symptom from info_corona_db"
        elif (a1 == 8):
            sql1 = "select remedial_treatment from info_corona_db"
        elif (a1 == 9):
            sql1 = "select definition from virus_corona_db"
        elif (a1 == 10):
            sql1 = "select classification from virus_corona_db"
        elif (a1 == 11):
            sql1 = "select form from virus_corona_db"
        elif (a1 == 12):
            sql1 = "select human_infection from virus_corona_db"
        elif (a1 == 13):
            sql1 = "select genus from virustable_corona_db"
        elif (a1 == 14):
            sql1 = "select humancorona from virustable_corona_db"

        if sql1 == "":
            sql1 = "SELECT DEAD FROM city_corona_db"
        curs.execute(sql1)
        result = curs.fetchall()
        conn.close()
        result = str(result).replace("(", "")
        result = str(result).replace(")", "")
        if p1==1:
            dispatcher.utter_message("{}".format(result))
        return []

class ActionCoronabrowser(Action):

    def name(self) -> Text:
        return "action_corona_browser"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        iurl1 = "https://i.imgur.com/eRQK3LR.png"
        webbrowser.open(iurl1)
        return []