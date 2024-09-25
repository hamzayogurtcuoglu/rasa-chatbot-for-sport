from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_match_info  # Skor almak için uygun fonksiyonu import et

class ActionMatchScore(Action):
    def name(self) -> Text:
        return "action_match_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Kullanıcı mesajını al
        user_message = tracker.latest_message.get('text', '')
        
        # Mesajı kelimelere ayır
        words = user_message.split()
        
        # "and" kelimesinin indekslerini bul
        and_indices = [i for i, word in enumerate(words) if word.lower() == 'and']
        print(and_indices)
        if and_indices:
            # "and" kelimesinin öncesindeki ve sonrasındaki kelimeleri takım isimleri olarak al
            team1 = ' '.join(words[max(0, and_indices[0]-1):and_indices[0]])
            team2 = ' '.join(words[and_indices[0]+1:and_indices[0]+2])
            
            # Takım skorunu al
            info = get_match_info(team1, team2)  # Bu fonksiyonu kendi veri tabanı fonksiyonuna göre güncelle
            if info:
                team1_score, team2_score, _, _ = info
                response = (f"The current score between {team1} and {team2} is {team1_score} - {team2_score}.\n")
            else:
                response = f"I couldn't find any score information for the match between {team1} and {team2}."
        else:
            response = "I couldn't identify the teams you're asking about. Could you please provide the team names separated by 'and'?"
        
        dispatcher.utter_message(text=response)
        return []
