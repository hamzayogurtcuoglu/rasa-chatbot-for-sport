from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_red_cards  # Import the function to fetch red card information from the database

class ActionMatchRedCards(Action):
    def name(self) -> Text:
        # This method returns the name of the action, so Rasa can recognize it
        return "action_match_red_cards"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Retrieve the team names stored in the slots
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        # Check if both team names are provided
        if team1 and team2:
            # Fetch red card information for the match between the two teams
            red_cards = get_match_red_cards(team1.lower(), team2.lower())
            if red_cards:
                # If red cards exist, format the response to list them
                response = f"In the match between {team1} and {team2}, the following red cards were issued: {', '.join(red_cards)}."
            else:
                # If no red cards were issued, inform the user
                response = f"There were no red cards issued in the match between {team1} and {team2}."
        else:
            # If team names are missing, prompt the user for correct input
            response = "I couldn't identify the teams you're asking about. Please provide both team names."

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        return []
