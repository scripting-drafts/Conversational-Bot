# Reddit-Deep-Learning
Reddit scraping with PRAW, visualization with Graphviz and training with pyTorch.


# Basic tuning for data modeling, RNN and the Chatbot.

line 561 -> Comment if the training has to start from a checkpoint.*1  
line 562 -> Checkpoint from which the training has to continue.  
line 563 - 565 -> Uncomment if the training has to start from a checkpoint.*1  
line 606 -> Seconds it takes to show the Loss and iteration number on terminal.  
line 607 -> Size of each part in which the model is divided.  
line 605 -> Number of the last iteration the Chatbot will listen to.*2  


*1 Or if the training is complete and you want to run the Chatbot.  
*2 Set to a previous than lastest iteration to check if the data got corrupted.

To run the Chatbot uncomment the last lines of the code below # CHAT # and skip the training.
