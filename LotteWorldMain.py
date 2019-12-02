import twitterscraper

print("hello world");
from twitterscraper import query_tweets
import datetime as dt

cnt = 0;
if __name__ == '__main__':
    for tweet in query_tweets('내일 롯데월드', begindate=dt.date(2019,7,1), enddate=dt.date(2019,7,2)): #enddate 포함 안함
        cnt = cnt + 1;
        print(tweet.timestamp) #작성시간
        print(tweet.text)      #트윗내용

    print("총 개수 : ", cnt);

    cnt = 0;
    for tweet in query_tweets('내일 롯데월드', begindate=dt.date(2019,10,31), enddate=dt.date(2019,11,1)):
        cnt = cnt + 1;
        print(tweet.timestamp) #작성시간
        print(tweet.text)      #트윗내용

    print("총 개수 : ", cnt);