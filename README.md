# Analysis of Strokes Gained and Club Head Speed on the PGA Tour
_Author: Hunter Henninger_

## Problem Statement

Driving distance on the PGA Tour continues to increase as many young, athletic golfers with swing speeds well above the Tour average (roughly 113-114mph) are experiencing major success on the PGA Tour in recent years. As the popular style of golf shifts towards hitting the ball as far as possible, this study seeks to capture statistical evidence of the impact of Club Head Speed on Total Strokes Gained. Because of physical strength or flexibility limitations, golfers often reach a maximum swing speed.

## Summary Overview

Through a process of wrangling, cleaning, manipulating, and modeling an extensive dataset of PGA metrics, this analysis clarifies the disadvantages of having a slower Club Head Speed.

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
Description of Strokes Gained [here](https://www.pgatour.com/news/2016/05/31/strokes-gained-defined.html)

## Conclusion

With a Club Head Speed above 115mph, professional golfers experience success because of their ability to decrease their distance to the hole on every shot on their way to the hole. They do not have to rely on making the "clutch" putts as much as a player with a slower swing speed. A faster Club Head Speed helps players gain enough strokes off the tee and in the fairway that making chips and ten foot putts is less important.

### Next Steps

As I continue my research over time I plan to:
- Collect more data to make the model more accurate and coefficients more precise. 
- Create a way for a competitive amateur golfer to compare themselves to PGA players with similar Club Head Speeds and discover ways that they can improve their game.
- With new technologies like TrackMan, there are measurements of golf swings that are not included in the ShotLink database. The ability to obtain that data is unclear at the time but there is an immense amount of research to be done on those statistics. 

#### Top players excluded because of missing data: 

Justin Rose, Francesco Molinari, Sergio Garcia, Keegan Bradley, Gary Woodland, Eddie Pepperell, Kiradech Aphibarnrat, Kevin Kisner, Ian Poulter, Adam Scott, Matt Wallace, Lucas Bjerregaard, Emiliano Grillo, Shugo Imahira, Alexander Björk, Si Woo Kim, Lee Westwood, Pat Perez, Zach Johnson, Adrian Otaegui, Shaun Norris, Thomas Pieters, Haotong Li, Thorbjorn Oleson, Dylan Frittelli, Tom Lewis, Satoshi Kodaira, Matthew Fitzpatrick, Tyrrell Hatton
