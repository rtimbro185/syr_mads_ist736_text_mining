**Author:** Ryan Timbrook <br>
**Project:** IST 736 Text Mining - Final Project <br>
**Topic:** Public Sentiment Toward NFL Team, Coach, Player - Can public opinion aid in predicting the accuracy of weekly NFL Fantasy Football Player's fantasy projection scores? <br>
**Date:** 12/8/2019 <br>

**Programming Languages:** Python - Anaconda 3 <br>
**APIs**: Twitter Premium Search, Twitter Standard Streaming <br>
**Machine Learning Algorithms:** <br>
	* Classifiers: Multinomial Naive Bayes (MNB), Support Vector Machine (SVM)<br>
**Machine Learning Packages:** sklearn.svm.LinearSVC, sklearn.naive_bayes.MultinomialNB <br>
**Other Notable Packages:** nltk, pandas, numpy, sklearn.feature_extraction.text.CountVectorizer, sklearn.feature_extraction.text.TfidfVectorizer <br>


# Project Requirements:
1. Project Format The objective of the project is to use the main skills taught in this class to solve a real text mining problem. Students should work individually or form a group of up to three students to finish the project. 
 
 2. Choose text mining problem and data set For this project, you must choose your own dataset.  It can be one that you created yourself or found from other resources. Some rules/tips about choosing data sets:    
 	a. Do not choose the data sets that we have analyzed in class, such as the Kaggle Sentiment data, movie review data, etc.   
 	b. The data set should contain at least 100 examples.  
 	c. Choose a data set that does not require excessive preprocessing. 

![Project Requirements Details](./00-Requirements/project-instructions.pdf)
--------------------------------------------------------------------------

# 1. 	Introduction
The NFL was already a lucrative business before Fantasy football took off, now you can't turn on a news program without hearing about Fantasy stats and which service provider like yahoo fantasy sports, cbs fantasy sports, and espn fantasy sports has better predictive modeling and real-time feedback on player's performance. According to Gallup, Football still overwhelmingly dominates American enthusiasm, with 37% calling it their favorite sport compared to its closest rival basketball at 11%; baseball is at 9%, after decades of declining stature. (Norman, 2018) NFL revenue grew an estimated $900 million to $14 billion in 2017; in 2018, it generated about $15 billion. (Soshnick & Novy-Williams, 2019) The league announced in January that it's aiming to boost its annual revenue to $25 billion by 2027. (Florio, 2010) Fantasy football and the spread of legalized sports betting across the U.S. promises to lock in fans and keep them focused on the game. (Houghton, Nowlin, & Walker, 2019)

Data Science aims to be at the heart of how fantasy players and those gambling on teams make their choices. IBM announced this 2019 season, "Fantasy Insights with Watson." "ESPN Fantasy Insights draws upon the latest in machine learning techniques to turn unstructured data into valuable insights. Nearly 10 million players rely on the combined resources of Watson Discovery and Watson OpenScale running on the IBM Cloud to give them a competitive edge." (ESPN Fantasy Insights with Watson, n.d.)

Football sports fans generate a large amount of Twitter tweets which reflect their opinions and feelings about what is happening not only during a game, but also throughout the week as the team prepares for the next game. The  aim of this research is to use text mining techniques on public news and media web sites like Twitter to collect and examine the sentiment conveyed through these sources, aggregate data relating to NFL teams, players, and coach, to determine if public sentiment alone is a predictor of Player Fantasy Football performance stats.

For example, if Deshaun Watson's Fantasy Football stats forecast for NFL season week 6 is 85 points leading into that week’s game, can the public opinion for that week of negative, neutral, or positive predict if he will achieve that points threshold or not. Thereby giving a player of Fantasy Football an edge in choosing to either keep Deshaun Watson as his or her starting quarterback or bench him for someone else.

## 1.1	Purpose
Identify public sentiment toward NFL teams, and its players that could help fans choose teams and players to play in their fantasy leagues. 
## 1.2	Scope
Gather public data using text mining techniques on:
* Public opinion toward NFL teams, coaches, and players.
* Reduce data gathering to one of each for initial POC.
* Data is in time-series format from the first week of the NFL 2019 session to current schedule week
* Players weekly Fantasy Football performance stat forecasts on a daily time scale.
* Perform sentiment analysis modeling ML techniques on data set to determine model prediction accuracies.
* Perform unsupervised topic modeling ML techniques on document text to gain insights into public opinion and primary opinion drivers.
* Evaluate weekly sentiment trends aligning with Fantasy Football performance stats forecasts.

### See ![Project Report](./05-Report/Final_Project_Timbrook_Ryan.pdf) for details.

### Code:<br>
All code for this project is found in the 03-Build directory. The ML flow was completed in jupyter notebooks with python files used for importing additional custom functions.

### Primary component steps
#### Step 1:<br>
* Text Mining - Obtaining the data sets <br>
Mining Twitter for tweets on specific NFL characters.<br>
	* [Player](./03-Build/text_mine_sentiment_players/search_twitter_nfl_player_premium.ipynb)<br>
	* [Coach](./03-Build/text_mine_sentiment_coaches/search_twitter_nfl_coach_premium.ipynb)<br>
	* [Team](./03-Build/text_mine_sentiment_teams/search_twitter_nfl_team_premium.ipynb)<br>

#### Step 2:<br>
* [Data Engineering](./03-Build/data_engineering_pipeline/) - Cleaning and Formating the data sets<br>
	* Various cleaning and text data transformation steps were taken. See the ![Project Report](./05-Report/Final_Project_Timbrook_Ryan.pdf) for complete details.
		* Code:
			* [Merge Labeled NFL Tweets](./03-Build/data_engineering_pipeline/nfl_sentiment_analysis_data_merge_master.ipynb)
			* [Merge NFL Tweets Data Sets](./03-Build/data_engineering_pipeline/merge_datasets_to_master.ipynb)
			* [Format Raw Tweets](./03-Build/data_engineering_pipeline/format_raw_twitter_data.ipynb)
			* [Data Model Raw Tweets](./03-Build/data_engineering_pipeline/process_raw_twitter_data_from_file.ipynb)
	
#### Step 3:<br>
* [Classification Modeling](./03-Build/classification_modeling/) - Experimentation with selecting the best modeling algorithm for this task.<br>
	* Code: <br>
		* [Primary Classification Modeling Experimentation - MNB and SVM](./03-Build/classification_modeling/classification_modeling_mnb_svm.ipynb) <br>
		* [Vedar Sentiment Classification](./03-Build/classification_modeling/classify_train_nfl_master.ipynb) <br>
		* [Create Training Test Data Sets](./03-Build/classification_modeling/create_train_test_nfl_master.ipynb) <br>

