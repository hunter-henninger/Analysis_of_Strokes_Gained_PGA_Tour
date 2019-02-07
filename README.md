# How Club Head Speed Affects Your Golf Game


### Strokes gained acts as a measure of success no matter what type of golf is being played. The goal on each hole is to get the ball in the hole in the fewest number of strokes possible. 




#### leftout players due to minimal data: Justin Rose, Francesco Molinari, Sergio Garcia, Keegan Bradley, Gary Woodland, Eddie Pepperell, Kiradech Aphibarnrat, Kevin Kisner, Ian Poulter, Adam Scott, Matt Wallace, Lucas Bjerregaard, Emiliano Grillo, Shugo Imahira, Alexander Björk, Si Woo Kim, Lee Westwood, Pat Perez, Zach Johnson, Adrian Otaegui, Shaun Norris, Thomas Pieters, Haotong Li, Thorbjorn Oleson, Dylan Frittelli, Tom Lewis, Satoshi Kodaira, Matthew Fitzpatrick, Tyrrell Hatton


### Approach:
   - Run basic model on columns with no null values.
   - Start tacking on columns in attempt to improve model performance.
   - Once a certain explanatory power is reached, separate model into two based on club head speed.
   - Run fast model on all players and slow model on all players to do an analysis on specific players that perform against the odds.



#### Do you have data fully in hand and if not, what blockers are you facing?
Yes, I have all my data. 50 players in the PGA Tour and every tournament they have played. 

#### Have you done a full EDA on all of your data?
There are a lot of visualizations that I want to do. I plan on having a notebook of mostly plots showing interesting stats that highlight club head speed specifically.

#### Have you begun the modeling process? How accurate are your predictions so far?
I have not begun modeling yet and that is due to my null values. Once the features of interest do not contain nulls I can run a lasso/ridge on total strokes gained.

#### What blockers are you facing, including processing power, data acquisition, modeling difficulties, data cleaning, etc.? How can we help you overcome those challenges?
The biggest blocker I am facing are null values. Null values that are not missing at random actually. This is just a matter of making decisions about each column. Either excluding it from the model or create dummy variables for null or not null.

#### Have you changed topics since your lightning talk? Since you submitted your Problem Statement and EDA? If so, do you have the necessary data in hand (and the requisite EDA completed) to continue moving forward?
No, not really. I just have spent so much time getting the data and cleaning it that I haven’t had the chance to really think about the model(s) that I want to run.

#### What is your timeline for the next week and a half? What do you have to get done versus what would you like to get done?
I have to clean the data to the point that I can use it in modeling and then begin the modeling process so that I can start to get an idea of how I can best answer the problem statement. 

#### What topics do you want to discuss during your 1:1?
I have been talking about null values too much so I don’t want to dwell on that. I am going to take multiple approaches to the missing data and comparing those models to find the best one. 

How do I make data private on github?




### make sure to make data private
