from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_capacity  # Import the get_city function from database.py

class ActionMatchLocation(Action):
    def name(self) -> Text:
        return "action_stadium_capacity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        stadium = tracker.get_slot("stadium")
        
        if stadium:
            # Take the words before and after "and" as team names

            capacity = get_capacity(stadium.lower())
            response = f"The stadium capacity is {capacity}."
        else:
            response = "I couldn't identify the stadium you're asking about."
        
        dispatcher.utter_message(text=response)
        return []