from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_info  # Skor almak için uygun fonksiyonu import et

class ActionMatchScore(Action):
    def name(self) -> Text:
        return "action_match_scorers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        team1 = tracker.get_slot("team1")
        team2 = tracker.get_slot("team2")
        
        if team1 and team2:
            
            # Takım skorunu al
            score_info = get_match_info(team1.lower(), team2.lower())
            if score_info:
                team1_score, team2_score, scorers_team1, scorers_team2 = score_info
                response = (f"The current score between {team1} and {team2} is {team1_score} - {team2_score}.\n"
                            f"Scorers for {team1}: {scorers_team1}.\n"
                            f"Scorers for {team2}: {scorers_team2}.")
            else:
                response = f"I couldn't find any score information for the match between {team1} and {team2}."
        else:
            response = "I couldn't identify the teams you're asking about. Could you please provide the team names separated by 'and'?"
        
        dispatcher.utter_message(text=response)
        return []
