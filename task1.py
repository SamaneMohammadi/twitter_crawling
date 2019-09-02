import tweepy
consumer_key = "ySucU57MnOdP0Fdv8cW6b1H7O"
consumer_secret = "RFCkT4057pyXlMBJowRP0B01sApHNmrG4NpjftmWI2bVEUm8sw"
access_token ="1006278565749510146-FsCR9PNCGfcOoHNMeb04rWgstDpksG"
access_token_secret = "55kysx1tgAbN3foJjbJIv0xVj1QtDmxUX0t3dJ1rKoQ43"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("------------------------------First user profile information------------------------------")
print("")
user_first = api.get_user("34373370")
print('Screen Name : {}\n----------------------------------------\n'.format(user_first.screen_name))
print('User Name : {}\n----------------------------------------\n'.format(user_first.name))
print('User Location : {}\n----------------------------------------\n'.format(user_first.location))
print('Bio : {}\n----------------------------------------\n'.format(user_first.description))
print('The Number of Followers : {}\n----------------------------------------\n'.format(str(user_first.followers_count)))
print('The Number of Friends : {}\n----------------------------------------\n'.format(str(user_first.friends_count)))
print('The Number of Statuses : {}\n----------------------------------------\n'.format(str(user_first.statuses_count)))
print('The User URL : {}\n----------------------------------------\n'.format(user_first.url))

print("------------------------------Second user profile information------------------------------")
print("")
user_second = api.get_user("26257166")
print('Screen Name : {}\n----------------------------------------\n'.format(user_second.screen_name))
print('User Name : {}\n----------------------------------------\n'.format(user_second.name))
print('User Location : {}\n----------------------------------------\n'.format(user_second.location))
print('Bio : {}\n----------------------------------------\n'.format(user_second.description.encode('utf-8')))
print('The Number of Followers : {}\n----------------------------------------\n'.format(str(user_second.followers_count)))
print('The Number of Friends : {}\n----------------------------------------\n'.format(str(user_second.friends_count)))
print('The Number of Statuses : {}\n----------------------------------------\n'.format(str(user_second.statuses_count)))
print('The User URL : {}\n----------------------------------------\n'.format(user_second.url))

print("------------------------------Third user profile information------------------------------")
print("")
user_Third = api.get_user("12579252")
print('Screen Name : {}\n----------------------------------------\n'.format(user_Third.screen_name))
print('User Name : {}\n----------------------------------------\n'.format(user_Third.name))
print('User Location : {}\n----------------------------------------\n'.format(user_Third.location))
print('Bio : {}\n----------------------------------------\n'.format(user_Third.description))
print('The Number of Followers : {}\n----------------------------------------\n'.format(str(user_Third.followers_count)))
print('The Number of Friends : {}\n----------------------------------------\n'.format(str(user_Third.friends_count)))
print('The Number of Statuses : {}\n----------------------------------------\n'.format(str(user_Third.statuses_count)))
print('The User URL : {}\n----------------------------------------\n'.format(user_Third.url))
print("")
print("-----------------------------------------End-------------------------------------------------")