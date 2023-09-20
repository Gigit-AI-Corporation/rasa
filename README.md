```shell
rasa run actions
rasa interactive
```

- Use rasa interactive to test new flows
- manually run rasa train if not reflecting new changes sometimes
- use rasa shell to test convo

openai flow:
What can you help with?

activate form by triggering intent: "ask me anything" or variations in that intent

# Dependency for spaCy

```bash
pip3 install 'rasa[spacy]'
python3 -m spacy download en_core_web_md
```

## Unintall uvloop for bug in Rasa interactive

When chatting with bot to trigger external reminder and get Error: EXTERNAL_reminder error Future exception was never retrieved future: <Future finished exception=BlockingIOError(35, 'write could not complete without blocking', 0)>

```bash
pip uninstall uvloop
```

TODO:

1. edit external trigger to activate a reminder instead of custom action

- scheduled reminders queue

2. this reminder waits for 4 seconds, then activates custom action to print response

# send external trigger

1. get ID from bot chat
2. edit name of trigger (EXTERNAL\_<trigger_name> and entities involved for slots + actions)

```bash
curl -H "Content-Type: application/json" -X POST -d \
'{"name": "EXTERNAL_dry_plant", "entities": {"plant": "Orchid"}}' \
"http://localhost:5005/conversations/<CONVERSATION_ID_FROM_BOT>/trigger_intent?output_channel=latest"
```

**_callback server only used for recieving messages from CURL like when posting External Events_**


# Flow for triggering external reminder to call custom action
* make sure uvloop installed for callback server
```shell
python callback_server.py
rasa run actions
rasa run --enable-api
curl -XPOST http://localhost:5005/webhooks/callback/webhook \
   -d '{"sender": "tester", "message": "remind me to call Brands!"}' \
   -H "Content-type: application/json"
```

no chat through chat, but sending message to bot via webhook in curl request abd *message* param in JSON payload