from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_weather  # Import the get_match_weather function from database.py

class ActionMatchWeather(Action):
    def name(self) -> Text:
        return "action_match_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        if team1 and team2:
            weather = get_match_weather(team1.lower(), team2.lower())
            if weather:
                response = f"The weather for the match between {team1} and {team2} is {weather}."
            else:
                response = f"I couldn't find the weather information for the match between {team1} and {team2}."
        else:
            response = "I couldn't identify the teams you're asking about. Could you please provide the team names?"

        dispatcher.utter_message(text=response)
        return []
