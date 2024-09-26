from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_weather  # Import the function to fetch weather information from the database

class ActionMatchWeather(Action):
    def name(self) -> Text:
        # Return the name of the action for Rasa to recognize
        return "action_match_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Retrieve team names from the slots
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")

        # Check if both team names are provided
        if team1 and team2:
            # Fetch the weather information for the match
            weather = get_match_weather(team1.lower(), team2.lower())
            if weather:
                # Format the response to include the weather information
                response = f"The weather for the match between {team1} and {team2} is: {weather}."
            else:
                # Inform the user if no weather information is available
                response = f"I'm sorry, but I couldn't find the weather information for the match between {team1} and {team2}."
        else:
            # Prompt the user for the missing team names
            response = "I couldn't identify the teams you're asking about. Please provide both team names."

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        return []
