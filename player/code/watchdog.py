import socket
import os
import time

MaxTime = 4 #length of longest video in secs
flag1 = 0 #just used to track allowing a timestamp
sleepy = 2

def OMXcheck():
  string = os.system('sudo pgrep -l omxplayer.bin')
  return string

while True:
    #Take a time stamp

    now = time.time()
    print ("Starting Time Stamp:", now)

    BooMX = OMXcheck() 
    intCon = int(BooMX)

    if intCon > 0:
        flag1 = 0   

    #check to see if OMXplayer is playing in background
    while flag1 == 0:
        print ("Checking to see if OMX is on")
        #converts to a boolean int
        BooMX = OMXcheck()	
        intCon = int(BooMX)
        #Take a new time stamp & calculate the difference
        while intCon != 0:
            #player is not running & pause the code a bit to wait for the sequence to make it back around
            print ("OMX off...resting for " sleepy)
            BooMX = OMXcheck()  
            intCon = int(BooMX)
            time.sleep(sleepy)

        later = time.time()
        difference = int(later - now)
        print ("Time difference:", difference)
        #if the difference is longer or equal to the Max video time (in secs)

        if difference >= MaxTime:
            print ("Time has gone past limit...")
            #timer has been triggered, assume that OMX is stuck
            #kill omxplayer and let the code move on
            os.system('sudo killall omxplayer.bin')
            os.system('sudo killall omsplayer')
            flag1 = 1
            break


