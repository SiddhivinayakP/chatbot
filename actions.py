# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionSayDoctor(Action):

    def name(self) -> Text:
        return "action_say_doctor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doctor_name = tracker.get_slot("doctor_name")
        if not doctor_name:
            dispatcher.utter_message(text = "I don't know your doctor choice")
        else:
            dispatcher.utter_message(text = f"Your Doctor choice is {doctor_name}")
        return []

class ActionSayTimings(Action):

    def name(self) -> Text:
        return "action_say_timings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        timings = tracker.get_slot("timings")
        if not timings:
            dispatcher.utter_message(text = "I don't know your time choice")
        else:
            dispatcher.utter_message(text = f"Your time choice is {timings}")
        return []

class ActionSayUserName(Action):

    def name(self) -> Text:
        return "action_say_user_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        user_name = tracker.get_slot("user_name")
        if not user_name:
            dispatcher.utter_message(text = "I don't know your name.")
        else:
            dispatcher.utter_message(text = f"Your name is {user_name}.")
        return []

class ActionSayUserAge(Action):

    def name(self) -> Text:
        return "action_say_user_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        user_age = tracker.get_slot("user_age")
        if not user_age:
            dispatcher.utter_message(text = "I don't know your age.")
        else:
            dispatcher.utter_message(text = f"Your name is {user_age}.")
        return []
