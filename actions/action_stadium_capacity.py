from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from database import get_capacity  # Import the function to fetch stadium capacity from the database

class ActionStadiumCapacity(Action):
    def name(self) -> Text:
        # Return the name of the action for Rasa to recognize
        return "action_stadium_capacity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Retrieve the stadium name from the slot
        stadium = tracker.get_slot("stadium")
        
        # Check if the stadium name is provided
        if stadium:
            # Fetch the stadium capacity using the provided stadium name
            capacity = get_capacity(stadium.lower())
            if capacity is not None:
                # Format the response with the stadium capacity
                response = f"The capacity of {stadium} is {capacity}."
            else:
                # Inform the user if the capacity information is not available
                response = f"I'm sorry, but I couldn't find the capacity information for {stadium}."
        else:
            # Prompt the user for the missing stadium name
            response = "I couldn't identify the stadium you're asking about. Please provide the stadium name."

        # Send the response back to the user
        dispatcher.utter_message(text=response)
        return []
