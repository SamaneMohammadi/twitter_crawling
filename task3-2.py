import tweepy

consumer_key = "ySucU57MnOdP0Fdv8cW6b1H7O"
consumer_secret = "RFCkT4057pyXlMBJowRP0B01sApHNmrG4NpjftmWI2bVEUm8sw"
access_token ="1006278565749510146-FsCR9PNCGfcOoHNMeb04rWgstDpksG"
access_token_secret = "55kysx1tgAbN3foJjbJIv0xVj1QtDmxUX0t3dJ1rKoQ43"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

file = open("location.txt", "w")

print("***********collect tweets that originate from the geographic region around South Bend*************")


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        file.write("{}\n---------------------------------------------------------------------\n".format(status.text.encode('utf-8')))
        print("{}\n-----------------------------------------------------------------------\n".format(status.text.encode('utf-8')))


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(locations=[-86.33,41.63,-86.20,41.74])