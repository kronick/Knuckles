#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import twitter
import time
import syslog
import sys
from secrets import *

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)

countFile = open("/Users/kronick/Documents/Knuckles/countFile.dat", "r+")
tatFile = open("/Users/kronick/Documents/Knuckles/all-simpsons.txt")
tats = tatFile.readlines()
count = int(countFile.read())

while True:
  try:
   print tats[count]
   api.PostUpdate(tats[count])
   syslog.syslog(syslog.LOG_ALERT, "KnuckleTweet: " + tats[count])
   count += 1
   countFile.seek(0)
   countFile.write(str(count))
   time.sleep(60 * 45) # Tweet every 45 minutes
  except twitter.TwitterError as e:
   if str(e).strip() == "Status is a duplicate.":
     count += 1
     syslog.syslog(syslog.LOG_ALERT, "Tried to post a duplicate status update.")
   else:
    syslog.syslog(syslog.LOG_ALERT, str(e))
    time.sleep(10) # On failure, retry every 10 seconds
  except:
    time.sleep(10)

