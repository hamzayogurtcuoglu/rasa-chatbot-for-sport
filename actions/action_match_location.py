from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_city, get_stadium  # Import the functions to fetch city and stadium info from the database

class ActionMatchLocation(Action):
    def name(self) -> Text:
        # This method returns the name of the action, so Rasa can recognize it
        return "action_match_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Fetch the team names stored in the slots
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        # Check if both team names are available
        if team1 and team2:
            # Retrieve city and stadium information for team1 using helper functions
            city1 = get_city(team1.lower())  # Fetch the city where team1 is based
            stadium = get_stadium(team1.lower())  # Fetch the stadium where team1 plays
            
            # Correcting the response to clarify which stadium belongs to which team
            response = f"The match between {team1} and {team2} will be held at {stadium}, located in {city1}."
        else:
            # If one or both team names are missing, ask the user to provide them
            response = "I couldn't identify the teams you're asking about."
        
        # Send the response to the user
        dispatcher.utter_message(text=response)
        return []
