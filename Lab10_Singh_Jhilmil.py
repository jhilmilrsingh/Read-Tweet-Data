import json

filename = "tweet_data.txt"
file_handle = open(filename)
outer_dictionary = json.load(file_handle)
tweet_list = outer_dictionary.get("tweet_list")

for tweet in tweet_list:
    print("Tweet:", tweet.get("text"))
    print("Tweeted at:", tweet.get("created_at"))    
    print("Tweet ID:", tweet.get("id"))
    print("Language:", tweet.get("lang"))

    user_dictionary = tweet.get("user")
    
    print("Tweeted by:", user_dictionary.get("name"), end=" ")

    if user_dictionary["verified"] == False:
        print("(Not Verified)")
    else:
        print("(Verified)")
        
    print("Location:", user_dictionary.get("location"))
    print("Who has", user_dictionary.get("followers_count"), "followers")

    retweet = tweet.get("retweeted_status")
    
    if retweet == None:
        print("This was an original tweet")
    else:
        print("This was retweeted", retweet.get("retweet_count"), "times.")

        retweet_user_dictionary = retweet.get("user")
        print ("The original tweet was", retweet.get("id"), "from", retweet_user_dictionary.get("name"))

    print ("")

file_handle.close()
