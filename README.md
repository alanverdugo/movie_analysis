Analysing movie rating data from an IMDB.com dataset using Python, Pandas and Matplotlib
====================================================

Since the dawn of cinema, the quality and enjoyment produced by motion pictures has been a complicated and controversial subject. An entire sub-industry has been created to review, criticize, recommend, analyze, categorize and rate movies. This, added to the subjective nature of each individual likes and dislikes has resulted in mixed experiences and expectations for the public. Some movies that are regarded as timeless classics by some people are seen as boring or even as bad movies by other people. The passing of time and the recent heavy use of special effects and CGI in movies also affect how the movies will be regarded in a few years, when those special effects look outdated.

However, we may find a general trend of increased satisfaction or dissatisfaction if we analyze a large number of movie ratings.

Research question
-----------------
Since many critics refer to their favorite period as the best era that cinema has to offer (or alternatively, that the movie quality is in decline), we will attempt to answer the following question:

**Has the perceived quality of movies increased or decreased over time?**

For any answer we may find, we will demonstrate and provide a reason behind it in the form of data and its visualizations.

Findings
--------
Using the [IMDB.com](http://www.imdb.com/) dataset, I analyzed 45,844 movies and 26,024,290 ratings for said movies. The oldest movie in the dataset was launched in 1874 and the newest in 2017.

I grouped the movies by launch year and calculated the average rating for the movies launched in every year. Doing this, I wanted to get an idea of the overall quality of the movies trough time.

While the technical aspect of motion pictures have obviously advanced thanks to new technology, it was not clear if this also improved the overall quality of the movie. In the next slide I present a chart of the relation between launch year and average rating for the movies launched in each year.

Some interesting facts I got from this analysis:

 - The initial period (from 1874 to around 1915) is chaotic and experimental. A film could be under a minute long. There was little to no cinematic technique, the film was usually black and white and it was without sound.
 - In the 1920s, begins a process of normalization. Movies are more popular and attainable. The public seem to have learned what to expect from directors and actors by this time. The primary steps in the commercialization of sound cinema were taken in the mid-to late 1920s, this could have helped to this normalization.
 - 2014 was a relatively disastrous year for cinema. The average rating for this year is 2.95. (The lowest since 1917, which is still part of the “experimental period”). The causes for this are beyond this analysis, but I will remind the reader that in 2014 we got movies like *Transformers: Age of extinction* and *Left behind* which has a 2% score in [rottentomatoes.com](https://www.rottentomatoes.com/)
 - In an scale from 0 to 5, The average tends to be slightly above 3. There is no noticeable increment or decrement from this average in the last century. So, to answer the research question, we cannot said that the quality of cinema has increased nor decreased substantially.

References
----------

 1. History of film. (2017, November 26). In Wikipedia, The Free Encyclopedia. Retrieved 04:03, November 29, 2017, from https://en.wikipedia.org/w/index.php?title=History_of_film&oldid=812220038
 2. Sound film. (2017, November 28). In Wikipedia, The Free Encyclopedia. Retrieved 04:04, November 29, 2017, from https://en.wikipedia.org/w/index.php?title=Sound_film&oldid=812587250
