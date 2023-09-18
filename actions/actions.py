# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import requests


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Get user message from Rasa tracker
        user_message = tracker.latest_message.get("text")
        print("latest user message:", user_message)

        # def get_chatgpt_response(self, message):
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json",
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "Act as a customer support representative. You help to solve user queries",
                },
                {"role": "user", "content": "You: " + user_message},
            ],
            "max_tokens": 100,
        }
        response = requests.post(url, headers=headers, json=data)
        # response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 200:
            chatgpt_response = response.json()
            print("chatgpt_response:", chatgpt_response)
            message = chatgpt_response["choices"][0]["message"]["content"]
            print("message:", message)
            dispatcher.utter_message(template="utter_message", message=str(message))
        else:
            # Handle error
            return "Sorry, I couldn't generate a response at the moment. Please try again later."

            # Revert user message which led to fallback.
        return [UserUtteranceReverted()]


class ActionSayShirtSize(Action):
    def name(self) -> Text:
        return "action_say_shirt_size"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        shirt_size = tracker.get_slot("shirt_size")
        if not shirt_size:
            dispatcher.utter_message(text="I don't know your shirt size.")
        else:
            dispatcher.utter_message(text=f"Your shirt size is {shirt_size}!")
        return []
