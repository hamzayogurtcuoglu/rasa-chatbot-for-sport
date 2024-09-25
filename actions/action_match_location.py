from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_city, get_stadium  # Import the get_city function from database.py

class ActionMatchLocation(Action):
    def name(self) -> Text:
        return "action_match_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        # Split the message into words        
        
        if team1 and team2:
            # Take the words before and after "and" as team names
            city1 = get_city(team1.lower())
            stadium = get_stadium(team1.lower())
            response = f"The match between {team1} and {team2} is taking place at {stadium}, located in {city1}."
        else:
            response = "I couldn't identify the teams you're asking about. Could you please provide the team names separated by 'and'?"
        
        dispatcher.utter_message(text=response)
        return []