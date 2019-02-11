# Analysis of Strokes Gained and Club Head Speed on the PGA Tour
_Author: Hunter Henninger_

## Problem Statement

In the unpredictable game of golf, Strokes Gained has become the most accurate and meaningful way to measure player efficiency and performance since it began being tracked 2004. The Strokes Gained statistic is broken up into four parts: Off the Tee, Approach the Green, Around the Green and Putting. The sum of all four categories gives a players Total Strokes Gained for a given golf tournament. It essentially compares each stroke a player takes to the rest of the Tour based on distance remaining to the hole. &quot;Strokes Gained recognizes that sinking a 20-foot putt represents a better performance than sinking a three-foot putt, even though they both count as a single stroke on the scorecard&quot; (Mark Broadie, developer of Strokes Gained). Additionally, Club Head Speed, another relatively new statistic, began being recorded in 2007 using certain radar technology. Club Head Speed measures the speed at which the club impacts the ball in miles per hour only on Par 4 and Par 5 tee shots where a radar measurement was taken.

Many young golfers with swing speeds well above the Tour average (roughly 113-114mph) are experiencing major success on the PGA Tour in recent years. This study aims to capture statistical evidence of the impact of Club Head Speed on Total Strokes Gained.

## Summary Overview

This study aims to capture statistical evidence of the impact of Club Head Speed on Total Strokes Gained. Through a process of wrangling, cleaning, manipulating, and modeling an extensive dataset of PGA metrics, this analysis numerically illustrates the disadvantage of having a slower Club Head Speed.

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
|**runtime**|*float*|Duration of the movie in minutes|
|**spoken_languages**|*object*|A list of spoken languages in the movie|
|**tagline**|*object*|The tagline of the movie|
|**title**|*object*|The Official Title of the movie|
|**vote_average**|*float*|The average voting rating of the movie, as counted by TMDB|
|**vote_count**|*float*|The number of votes, as counted by TMDB|
|**keywords**|*object*|The movie plot keywords|
|**cast**|*object*|Names of the cast of the movie|
|**crew**|*object*|Names of the crew of the movie|

## Conclusion

With a Club Head Speed above 115mph, professional golfers experience success because of their ability to decrease their distance to the hole on every shot on their way to the hole. They do not have to rely on making the "clutch" putts as much as a player with a slower swing speed. A faster Club Head Speed helps players gain enough strokes off the tee and in the fairway that making chips and ten foot putts is less important.

### Next Steps

Collecting more data would make the model more accurate and coefficients more precise. Create some way for a competitive amateur golfer to compare themselves to PGA players with similar Club Head Speeds and discover ways that they can improve their game.

#### Players Excluded: 

Justin Rose, Francesco Molinari, Sergio Garcia, Keegan Bradley, Gary Woodland, Eddie Pepperell, Kiradech Aphibarnrat, Kevin Kisner, Ian Poulter, Adam Scott, Matt Wallace, Lucas Bjerregaard, Emiliano Grillo, Shugo Imahira, Alexander Björk, Si Woo Kim, Lee Westwood, Pat Perez, Zach Johnson, Adrian Otaegui, Shaun Norris, Thomas Pieters, Haotong Li, Thorbjorn Oleson, Dylan Frittelli, Tom Lewis, Satoshi Kodaira, Matthew Fitzpatrick, Tyrrell Hatton
