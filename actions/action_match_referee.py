from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_referee  # Import the function to fetch referee information from the database

class ActionMatchReferee(Action):
    def name(self) -> Text:
        # This method returns the name of the action, so Rasa can recognize it
        return "action_match_referee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Retrieve the team names stored in the slots
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        # Check if both team names are provided
        if team1 and team2:
            # Fetch the referee information for the match between the two teams
            referee = get_match_referee(team1.lower(), team2.lower())
            if referee:
                # If referee information is found, format the response
                response = f"The referee for the match between {team1} and {team2} is {referee}."
            else:
                # If no referee information is found, inform the user
                response = f"I'm sorry, but I couldn't find the referee information for the match between {team1} and {team2}."
        else:
            # If team names are missing, prompt the user for correct input
            response = "I couldn't identify the teams you're asking about. Please provide both team names."

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        return []
