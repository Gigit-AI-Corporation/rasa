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

TODO: 
1. edit external trigger to activate a reminder instead of custom action
  * scheduled reminders queue 
2. this reminder waits for 4 seconds, then activates custom action to print response