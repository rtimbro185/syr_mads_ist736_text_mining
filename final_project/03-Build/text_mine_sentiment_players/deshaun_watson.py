#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:21:27 2019

@author: davidmadsen
"""

import datetime
import os
import pandas as pd

path = os.path.join ('..','Texans_fantasy_point_labels.csv' )

scores = pd.read_csv(path)
scores['Date'] = pd.to_datetime(scores['Date'], format='%m/%d/%y %I:%M %p')

path = os.path.join('..',
                    'text_mine_sentiment_players',
                    'search_result_tweet_text_data.csv')

texans_tweets = pd.read_csv(path)

texans_tweets['created_at'] = pd.to_datetime(texans_tweets['created_at'],
             format = '%a %b %d %H:%M:%S %z %Y')

path = os.path.join ('..', 
                     'text_mine_sentiment_players',
                     'player_articles_texans.tsv')

texans_articles = pd.read_csv(path, sep='\t')
texans_articles['published_at'] = pd.to_datetime(
        texans_articles['published_at'],
        format = '%Y-%m-%dT%H:%M:%SZ')
texans_articles_labeled = []

score_columns = scores.columns

score_dates = scores['Date'].tolist()


for row in texans_articles.itertuples():
    # some of the player names came in with a stray leading space
    player_name = row[3].lstrip()
    # just skip players for whom we don't have labels
    if player_name not in score_columns:
        continue
    columns_index = score_columns.tolist().index(player_name)
    print(columns_index)
    for score_row in scores.itertuples():
        if score_row[1] > row[7]:
            print(row[7], score_row[1])
            article_dict = {
                    'published_at':row[7],
                    'player_name':player_name,
                    'title':row[4],
                    'description':row[5],
                    'label':score_row[columns_index + 1]}
            texans_articles_labeled.append(article_dict)    
            break
            
texans_pd = pd.DataFrame(texans_articles_labeled)     
    