from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_referee  # Import the get_match_referee function from database.py

class ActionMatchReferee(Action):
    def name(self) -> Text:
        return "action_match_referee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        if team1 and team2:
            referee = get_match_referee(team1.lower(), team2.lower())
            if referee:
                response = f"The referee for the match between {team1} and {team2} is {referee}."
            else:
                response = f"I couldn't find the referee information for the match between {team1} and {team2}."
        else:
            response = "I couldn't identify the teams you're asking about. Could you please provide the team names?"

        dispatcher.utter_message(text=response)
        return []
