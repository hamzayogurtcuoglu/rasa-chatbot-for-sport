from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_info  # Import the function to fetch match information from the database

class ActionMatchScore(Action):
    def name(self) -> Text:
        # This method returns the name of the action, so Rasa can recognize it
        return "action_match_scorers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Retrieve the team names stored in the slots
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")
        
        # Check if both team names are provided
        if team1 and team2:
            # Fetch the match information for the two teams
            score_info = get_match_info(team1.lower(), team2.lower())
            if score_info:
                # Unpack the relevant information from the returned data
                team1_score, team2_score, scorers_team1, scorers_team2 = score_info
                
                # Format the response to include scores and scorers for both teams
                response = (f"The current score between {team1} and {team2} is {team1_score} - {team2_score}.\n"
                            f"Scorers for {team1}: {', '.join(scorers_team1)}.\n"
                            f"Scorers for {team2}: {', '.join(scorers_team2)}.")
            else:
                # Inform the user if no score information is available
                response = f"I'm sorry, but I couldn't find any score information for the match between {team1} and {team2}."
        else:
            # Prompt the user for the missing team names
            response = "I couldn't identify the teams you're asking about."
        
        # Send the response back to the user
        dispatcher.utter_message(text=response)
        return []
