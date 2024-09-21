from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_city  # Import the get_city function from database.py

class ActionMatchLocation(Action):
    def name(self) -> Text:
        return "action_match_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the entire user message
        user_message = tracker.latest_message.get('text', '')
        
        # Split the message into words
        words = user_message.split()
        
        # Find the indices of "and" in the message
        and_indices = [i for i, word in enumerate(words) if word.lower() == 'and']
        
        
        if and_indices:
            # Take the words before and after "and" as team names
            team1 = ' '.join(words[max(0, and_indices[0]-1):and_indices[0]])
            team2 = ' '.join(words[and_indices[0]+1:and_indices[0]+2])
            city1 = get_city(team1)
            response = f"The match between {team1} and {team2} is taking place at {city1}."
        else:
            response = "I couldn't identify the teams you're asking about. Could you please provide the team names separated by 'and'?"
        
        dispatcher.utter_message(text=response)
        return []