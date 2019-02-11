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
|**belongs_to_collection**|*int*|Binary column that indicates if the movie belongs to collection|
|**budget**|*float*|The budget of the movie in dollars|
|**genres**|*object*|A list of all the genres associated with the movie|
|**homepage**|*int*|Binary column that indicates if the movie has a homepage|
|**overview**|*object*|A brief overview of the movie|
|**popularity**|*float*|The Popularity Score assigned by TMDB|
|**production_companies**|*object*|A list of production companies involved with the making of the movie|
|**production_countries**|*object*|A list of countries where the movie was shot|
|**release_date**|*datetime*|Release Date of the movie|
|**revenue**|*float*|The total revenue of the movie in US dollars|
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
