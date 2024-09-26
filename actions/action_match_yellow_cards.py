from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_yellow_cards  # Import the function to fetch yellow card information from the database

class ActionMatchYellowCards(Action):
    def name(self) -> Text:
        # Return the name of the action for Rasa to recognize
        return "action_match_yellow_cards"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Retrieve team names from the slots
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        # Check if both team names are provided
        if team1 and team2:
            # Fetch the yellow card information for the match
            yellow_cards = get_match_yellow_cards(team1.lower(), team2.lower())
            if yellow_cards:
                # Format the response to include the list of players who received yellow cards
                response = (f"The players who received yellow cards in the match between "
                            f"{team1} and {team2} are: {', '.join(yellow_cards)}.")
            else:
                # Inform the user if no yellow card information is available
                response = (f"I'm sorry, but I couldn't find any yellow card information "
                            f"for the match between {team1} and {team2}.")
        else:
            # Prompt the user for the missing team names
            response = "I couldn't identify the teams you're asking about. Please provide both team names."

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        return []
