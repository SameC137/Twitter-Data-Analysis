import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor
from clean_tweets_dataframe import Clean_Tweets

_, tweet_list = read_json("data/covid19.json")



class TestTweetDfClean(unittest.TestCase):
    def setUp(self) -> pd.DataFrame:
        self.extractor = TweetDfExtractor(tweet_list[:5])
        self.df= self.extractor.get_tweet_df() 
        self.clean_tweets=Clean_Tweets(self.df)

    def test_drop_unwanted_column(self):
        
        unwantedDropped=self.clean_tweets.drop_unwanted_column(self.df)
        self.assertEqual(len(unwantedDropped[unwantedDropped['retweet_count'] == 'retweet_count' ].index) , 0)
       
    def test_drop_duplicate(self ):
        data=self.clean_tweets.drop_duplicate(self.df)
        self.assertEqual(data.duplicated(subset=["original_text"],keep="last").sum().astype(int) , 0)
       
    def test_convert_to_datetime(self):
        data=self.clean_tweets.convert_to_datetime(self.df)
        self.assertEqual(str(data["created_at"].dtype), "datetime64[ns, UTC]")
    
    def test_convert_to_numbers(self):
        
        data=self.clean_tweets.convert_to_numbers(self.df)
        self.assertTrue(str(data["subjectivity"].dtype)=="int64" or str(data["subjectivity"].dtype)=="float64"   ) 
    def test_remove_non_english_tweets(self):
        
        data=self.clean_tweets.drop_duplicate(self.df)
        self.assertEqual(len(data[data['lang'] != 'en'].index) , 0)


if __name__ == '__main__':
	unittest.main()