## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
* website
  - utter_web

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## information
* inform
 - utter_ask_location

## details
* inform{"location":"india"}
 - slot{"location":"india"}
 - action_weather

 ## Generated Story 3320800183399695936
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "italy"}
    - slot{"location": "italy"}
    - action_weather
    - slot{"location": "italy"}
* goodbye
    - utter_goodbye
    - export
## Generated Story -3351152636827275381
* greet
    - utter_greet
* inform{"location": "London"}
    - slot{"location": "London"}
    - action_weather
* website
    - utter_web
* goodbye
    - utter_goodbye
    - export
## Generated Story 8921121480760034253
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location":"London"}
    - slot{"location": "London"}
    - action_weather
* website
    - utter_web
* goodbye
    - utter_goodbye
    - export
## Generated Story -5208991511085841103
    - slot{"location": "London"}
    - action_weather
* goodbye
    - utter_goodbye
    - export
## Generated Story -5208991511085841103
    - slot{"location": "London"}
    - action_weather
* goodbye
    - utter_goodbye
    - export
## story_001
* greet
   - utter_greet
* inform
   - utter_ask_location
* inform{"location":"London"}
   - slot{"location": "London"}
   - action_weather
* website
    - utter_web
* goodbye
   - utter_goodbye
## story_002
* greet
   - utter_greet
* inform{"location":"Paris"}
   - slot{"location": "Paris"}
   - action_weather
* goodbye
   - utter_goodbye 
## story_003
* greet
   - utter_greet
* website
    - utter_web
* inform
   - utter_ask_location
* inform{"location":"Vilnius"}
   - slot{"location": "Vilnius"}
   - action_weather
* goodbye
   - utter_goodbye
## story_004
* greet
   - utter_greet
* inform{"location":"Italy"}
   - slot{"location": "Italy"}
   - action_weather
* website
    - utter_web
* goodbye
   - utter_goodbye 
## story_005
* greet
   - utter_greet
* inform
   - utter_ask_location
* inform{"location":"Lithuania"}
   - slot{"location": "Lithuania"}
   - action_weather
* goodbye
   - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform
    - action_weather
* goodbye{"goodbye": "thanks"}
    - utter_goodbye
* greet
    - utter_greet
* inform
    - utter_ask_location
