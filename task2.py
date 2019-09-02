import tweepy
consumer_key = "ySucU57MnOdP0Fdv8cW6b1H7O"
consumer_secret = "RFCkT4057pyXlMBJowRP0B01sApHNmrG4NpjftmWI2bVEUm8sw"
access_token ="1006278565749510146-FsCR9PNCGfcOoHNMeb04rWgstDpksG"
access_token_secret = "55kysx1tgAbN3foJjbJIv0xVj1QtDmxUX0t3dJ1rKoQ43"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


print("-----------------------------------the latest 20 followers and friends for first user-----------------------------------")
print("")
user= api.get_user("34373370")
followers = user.followers()
print('The latest 20 followers of first user :')
print("")
for follower in followers:
    print("the screen_name of follwer : {}  UserId: {}\n--------------------------------------------------\n".format(follower.screen_name,str(follower.id)))
print("")
friends = user.friends()
print('The latest 20 friends of first user:')
print("")
for friend in friends:
    print("the screen_name of friend : {}  UserId: {}\n--------------------------------------------------\n".format(friend.screen_name, str(friend.id)))
print("")

print("----------------------------------- the latest 20 followers and friends for second user-----------------------------------")
print("")
user= api.get_user("26257166")
followers = user.followers()
print('The latest 20 followers of second user :')
print("")
for follower in followers:
    print("the screen_name of follwer : {}  UserId: {}\n--------------------------------------------------\n".format(
        follower.screen_name, str(follower.id)))
print("")
friends = user.friends()
print('The latest 20 friends of second user :')
print("")
for friend in friends:
    print("the screen_name of friend : {}  UserId: {}\n--------------------------------------------------\n".format(friend.screen_name, str(friend.id)))
print("")

print("----------------------------------- the latest 20 followers and friends for third user -----------------------------------")
print("")
user= api.get_user("12579252")
followers = user.followers()
print('The latest 20 followers of third user :')
print("")
for follower in followers:
    print("the screen_name of follwer : {}  UserId: {}\n--------------------------------------------------\n".format(follower.screen_name, str(follower.id)))
print("")
friends = user.friends()
print('The latest 20 friends of third user :')
print("")
for friend in friends:
    print("the screen_name of friend : {}  UserId: {}\n--------------------------------------------------\n".format(friend.screen_name, str(friend.id)))
print("")
print("------------------------------------ End -----------------------------------")