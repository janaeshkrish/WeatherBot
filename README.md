# Weather Bot
## Overview

Chatbot which helps the user to answer the weather status for any of the location.The chatbot is build using RASA framework.Rasa is a chatbot framework to consider for more ambitious projects. Unlike many bot frameworks, Rasa is also open source. A developer community provides NLU training models, bot prototypes, and guidance.

![rasa](https://rasa.com/static/686aee8071dd209f198d500b1164e350/4828e/rasa.png)

## Dependencies
- tensorflow
- rasa >= 1.8
- VScode(IDE)
- weather API (https://openweathermap.org/)

## Steps
1) Train the model by running:
> rasa train nlu
2) Once the model is trained, test the model:
> rasa shell nlu
3) Start the custom action server by running:
> rasa run actions
4) Open a new terminal and start the app by running:
> rasa run -m models --enable-api --cors "*" --debug
5) Talk to the chatbot once it's loaded after running open index.html file and start typing....

![rasa](/output.gif)

