from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_yellow_cards  # Import the get_yellow_cards function from database.py

class ActionMatchYellowCards(Action):
    def name(self) -> Text:
        return "action_match_yellow_cards"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        if team1 and team2:
            yellow_cards = get_yellow_cards(team1.lower(), team2.lower())  # Sarı kartları al
            if yellow_cards:
                response = f"The players who received yellow cards in the match between {team1} and {team2} are: {', '.join(yellow_cards)}."
            else:
                response = f"I couldn't find any yellow card information for the match between {team1} and {team2}."
        else:
            response = "I couldn't identify the teams you're asking about. Could you please provide the team names?"

        dispatcher.utter_message(text=response)
        return []
