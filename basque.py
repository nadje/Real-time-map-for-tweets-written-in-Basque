import tweepy
import json
import csv
import nltk

consumer_key = 'SpI3mgC7UKQOHnUcr3jRlQ'
consumer_secret = 'p7Qt4QHCrTWIOYszr9uy7lgrOcgjLyL1bgMSo9U4yM'
access_token = '2206833558-PmY7kN9MbvUbbxqaVc7g5mpKG9mn5Kod0lqcDy1'
access_token_secret = 'Df48hcvchUSZqnt3bpk1raJeao22AXsUEum2sZzZhujox'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
##
motherDict = {}

file = open("obair.txt")

lines = file.readlines()
for line in lines:
        elements = line.strip().split(',')
        user = elements[0].lower()
        motherDict[user] = elements[1] + "," + elements[2]
#print motherDict


#This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        #Twitter returns data in JSON format - we need to decode it first in a dictionary
        decoded = json.loads(data)
        #print decoded
        random_user = ''
        #Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print "Coordinates: ", decoded['coordinates']
        print "Location: ", decoded['user']['location']
        #Cuser = api.get_user(decoded['user']['screen_name'])
        #Check for presence of coordinates
        if decoded['coordinates'] != None:
                random_user = decoded['user']['screen_name']
                latLong = str(decoded['coordinates'])
                tempList = latLong.split(',')
                random_latitude = tempList[0]
                random_longitude = tempList[1]
                print random_latitude, random_longitude
##        else:
##               print "Coordinates not present"
##
##        #Check user against Obair dictionary
        screenName = decoded['user']['screen_name'].lower()
        if screenName in motherDict:
        #       print "User is in Obair.txt"
                random_user = screenName
                latLong = str(motherDict[screenName])
                tempList = latLong.split(',')
                random_latitude = tempList[0]
                random_longitude = tempList[1]
                print random_latitude, random_longitude

        #Check users friends against Obair dictionary
        #for friend in Cuser.friends():
        #         if friend.screen_name in motherDict:
        # #               print "User friend is in Obair.txt"
        #                 random_user = friend.screen_name
        #                 latLong = str(motherDict[friend.screen_name])
        #                 tempList = latLong.split(',')
        #                 random_latitude = tempList[0]
        #                 random_longitude = tempList[1]
        #                 print random_latitude, random_longitude
        print " "
        if random_user != '':
                final_data = [{'user': random_user, 'geo' :{
                                        'latitude': random_latitude,
                                       'longitude' : random_longitude
                                       }}]
                data_string = json.dumps(final_data, sort_keys = True)
                fileobj = open('data.json', 'w')
                fileobj.write(data_string)
        
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()

    print "Showing all new tweets:"
    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
 
    stream.filter(track=['izan', 'zuen', 'euskal', 'egin', 'euskara', 'hizkuntza', 'ziren', 'euskararen','zituen'])
    #stream.filter(track=['izan', 'zuen', 'euskal', 'egin', 'euskara', 'hizkuntza', 'ziren', 'euskararen','zituen', 'zuten', 'esan', 'eman', 'jainkoak', 'euskarak', 'artean', 'jaunak', 'irakurri', 'euskaraz', 'herriko', 'nafarroako', 'ondoren', 'horiek'])


