# pip install chatterbot
from chatterbot import chatbot
from chatterbot.trainers import ListTrainer
 
#creating a new chatbot
chatbot = Chatbot('chatcode')
trainer = ListTrainer(chatbot)
trainer.train(['Thank YOU!'])
 
# getting a response from the chatbot
response = chatbot.get_response("hi, your code is awesome")
print(response)