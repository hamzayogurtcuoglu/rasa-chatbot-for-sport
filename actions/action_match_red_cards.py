from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_red_cards  # Import the get_match_red_cards function from database.py

class ActionMatchRedCards(Action):
    def name(self) -> Text:
        return "action_match_red_cards"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        if team1 and team2:
            red_cards = get_match_red_cards(team1.lower(), team2.lower())
            if red_cards:
                response = f"In the match between {team1} and {team2}, the following red cards were issued: {red_cards}."
            else:
                response = f"There were no red cards in the match between {team1} and {team2}."
        else:
            response = "I couldn't identify the teams you're asking about. Could you please provide the team names?"

        dispatcher.utter_message(text=response)
        return []
