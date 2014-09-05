Real-time-tweet-map
==========================================

This map displays the location of users tweeting in Basque. 

To run the program make your own twitter api and use your own consumer key, consumer secret, access token and access
token secret.
Run fl.py and basque.py to display the map and the pins showing the location of each user 
and then open the page on http://localhost:5000 

If there are tweets in Basque but there are no pins in the map, it's because the user hasn't enabled the "Location" in 
his twitter account. The map will be updated only if it gets the coordinates of every user. 
