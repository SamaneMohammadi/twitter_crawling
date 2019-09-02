import tweepy

consumer_key = "ySucU57MnOdP0Fdv8cW6b1H7O"
consumer_secret = "RFCkT4057pyXlMBJowRP0B01sApHNmrG4NpjftmWI2bVEUm8sw"
access_token ="1006278565749510146-FsCR9PNCGfcOoHNMeb04rWgstDpksG"
access_token_secret = "55kysx1tgAbN3foJjbJIv0xVj1QtDmxUX0t3dJ1rKoQ43"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

file = open("keyword(count).txt","w")

keyword = ["Indiana","weather"]
for key in keyword:
    tweets = api.search(q =key ,count = 50)

for i in range(0,50):
    file.write("{} : {}\n--------------------------------------------------------------------------\n".format(i,tweets[i].text.encode('utf-8')))
    print("{} : {}\n-------------------------------------------------------------------------\n".format(i,tweets[i].text.encode('utf-8')))

