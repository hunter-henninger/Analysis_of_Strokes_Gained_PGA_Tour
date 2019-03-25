# Analysis of Strokes Gained and Club Head Speed on the PGA Tour
_Author: Hunter Henninger_

## Problem Statement

Driving distance on the PGA Tour continues to increase as many young, athletic golfers with swing speeds well above the Tour average (roughly 113-114mph) are experiencing major success on the PGA Tour in recent years. As the popular style of golf shifts towards hitting the ball as far as possible, this study seeks to capture statistical evidence of the impact of Club Head Speed on Total Strokes Gained. The analysis
provides a comparison of golfers with different swing speeds and identifies factors that affect their performance the most.

## Summary Overview

The analysis is broken up into six clean notebooks as clear steps are taken to achieve the main goal. It starts by wrangling, cleaning, and manipulating a dataset of PGA Tour metrics. The data is explored through visualizations of distributions and patterns to demonstrate key relationships between Strokes Gained and other metrics. Through a process of model selection and tuning, two production models are fit: one for golfers with slower swing speeds and the other for golfers with faster swing speeds. A comparison of explanatory power and coefficients leads to clear recommandations for golfers with slow swing speeds to improve Strokes Gained.

## The Data
|Feature|Type|Description|
|---|---|---|
|**sg:_off-the-tee**|*float*|The distance a player hits the ball off the tee on Par 4 and Par 5's measured against a statistical baseline used for the entire Tour|
|**sg:_approach-the-green**|*float*|The number of approach shots a player takes from specific distances on each hole measured against a statistical baseline. This includes Par 3 tee shots|
|**sg:_around-the-green**|*float*|The number of shots a player takes within 30 yards of the edge of the green measured against a statistical baseline|
|**sg:_putting**|*float*|The number of puts a player takes on a green measured against a statistical baseline|
|**driving_distance**|*float*|The average number of yards per measured drive (2 per round)|
|**longest_drives**|*float*|The longest drive for that player's entire year|
|**driving_accuracy_percentage**|*float*|The percentage of time a tee shot comes to rest in the fairway|
|**distance_from_edge_of_fairway**|*float*|The average distance in feet and inches from the edge of the fairway when the player misses the fairway|
|**left/right_rough_tendency**|*float*|The percentage of time a tee shot comes to rest in the left/right rough|
|**club_head_speed**|*float*|The speed at which the club impacts the ball (mph)|
|**greens_in_regulation_percentage**|*float*|The percentage of time the player was able to hit the green in regulation (1st stroke on a Par 3, 2nd stroke on a Par 4, 3rd stroke on a Par 5)|
|**going_for_the_green**|*float*|The percent of time a player shoots for the green on the first of a Par 4 or the second shot of a Par 5|
|**proximity_to_hole**|*float*|The average distance from the hole a player's ball is after their approach shot in inches|
|**left/right_rough_proximity**|*float*|The average distance remaining to the hole for all approach shots hit from the left/right rough in inches|
|**fairway_proximity**|*float*|The average distance remaining to the hole for all approach shots hit from the fairway (including tee shots on Par 3s)|
|**approaches_from_**|*float*|The average remaining distance to the hole for all approach shots hit from specified distance|
|**sand_save_percentage**|*float*|The percent of time a player was able to get the ball in the hole in two shots or less from a greenside bunker|
|**proximity_to_hole_from_sand**|*float*|The average remaining distance to the hole after hitting the ball onto the putting surface from a bunker around the green|
|**scrambling**|*float*|The percent of time a player misses the green in regulation but still makes par or better|
|**scrambling_from_**|*float*|The percent of time a player misses the green in regulation but still makes par or better when the birdie stroke is taken the specified distance|
|**putting_average**|*float*|The average number of putts per green in regulation|
|**one_putt_percentage**|*float*|The percent of time a player makes it in one putt after getting on the green|
|**3-putt_avoidance**|*float*|The percent of time three or more putts were taken|
|**putts_per_round**|*float*|The average number of putts per round played|
|**putting_from_**|*float*|The percentage of time the player makes the putt from the specified distance|
|**approach_putt_performance**|*float*|Average distance to the hole after the first putt (inches)|
|**birdie_or_better_conversion_percentage**|*float*|The percent of time a player makes birdie or better after hitting the green in regulation|
<br><br>
Description of Strokes Gained metric [here](https://www.pgatour.com/news/2016/05/31/strokes-gained-defined.html)

## Results and Conclusion

In the game of golf, especially at a competitive level, players are constantly looking for ways to  maximize Strokes Gained. Before going into this study, it was known that increasing Club Head Speed makes the sport easier and the regression analysis proves it. The method used to explore the relationship between Strokes Gained and Club Head Speed essentially breaks golfers into two categories: slower or faster swing speeds. 
<br><br>
With a Club Head Speed above 115mph, professional golfers experience success because of their ability to decrease distance to the hole on every stroke. It allows for more room for error on and around the green, arguably the most difficult aspect of the game. The study suggests for players with slower swing speeds, chipping and putting with excellence is key to remaining competitive as average driving distance continues to rise. 

### Next Steps

As I continue my research over time I plan to:
- Collect more data to make the model more accurate and increase the precision of the coefficients. Specifically, include players not in the Top 100 in the world.
- Create a platform for competitive amateur golfers to compare themselves to PGA players with similar swing speeds and discover ways to improve their game.
- With new technologies like TrackMan, there are measurements of golf swings that are not included in the ShotLink database. I am excited to extend my research.

<br><br>
<br><br>
#### Top players excluded because of missing data: 

Justin Rose, Francesco Molinari, Sergio Garcia, Keegan Bradley, Gary Woodland, Eddie Pepperell, Kiradech Aphibarnrat, Kevin Kisner, Ian Poulter, Adam Scott, Matt Wallace, Lucas Bjerregaard, Emiliano Grillo, Shugo Imahira, Alexander Björk, Si Woo Kim, Lee Westwood, Pat Perez, Zach Johnson, Adrian Otaegui, Shaun Norris, Thomas Pieters, Haotong Li, Thorbjorn Oleson, Dylan Frittelli, Tom Lewis, Satoshi Kodaira, Matthew Fitzpatrick, Tyrrell Hatton
