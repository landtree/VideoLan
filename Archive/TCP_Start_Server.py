#!/usr/bin/env python

import socket
import os
import subprocess
from subprocess import Popen
import time
import pygame

pygame.init()

#player adresses
player1 = '192.168.0.100'
player2 = '192.168.0.101'
player3 = '192.168.0.102'
player4 = '192.168.0.103'

movie1 = '/home/pi/player/video/1.mp4'
movie2 = '/home/pi/player/video/2.mp4'
movie3 = '/home/pi/player/video/3.mp4'
movie4 = '/home/pi/player/video/4.mp4'
movie5 = '/home/pi/player/video/5.mp4'
movie6 = '/home/pi/player/video/6.mp4'

TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((player1, TCP_PORT)) #Set to Current player, start_server is always player 1
s.listen(1)

MESSAGE1 = "100"
MESSAGE2 = "101"
MESSAGE3 = "102"
MESSAGE4 = "103"
MESSAGE5 = "104"
MESSAGE6 = "105"

#Flags
flagStart = 1
flag1 = 0
flag2 = 0
flag3 = 0
counter = 0

screen = pygame.display.set_mode((0,0), pygame.NOFRAME)
pygame.mouse.set_visible(False)

def data_check():
    conn, addr = s.accept()
    print ('Connection address:', addr)
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        #print ("received data:", data)
        conn.send(data)  # echo
        return data
    conn.close()

def SendToVideo1():
    print ("Sending Video")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((player1, TCP_PORT))
    s.send(MESSAGE1)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print ("received data:", data)
    
def SendToVideo2():
    print ("Sending Video")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((player2, TCP_PORT))
    s.send(MESSAGE2)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print ("received data:", data)
   
def SendToVideo3():
    print ("Sending Video")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((player3, TCP_PORT))
    s.send(MESSAGE3)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print ("received data:", data)
    
def SendToVideo4():
    print ("Sending Video")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((player4, TCP_PORT))
    s.send(MESSAGE4)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print ("received data:", data)
    
def SendToVideo5():
    print ("Sending Video")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((player1, TCP_PORT))
    s.send(MESSAGE5)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print ("received data:", data)
  
def SendToVideo6():
    print ("Sending Video")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((player4, TCP_PORT))
    s.send(MESSAGE6)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print ("received data:", data)

def start_up():
    print("Booting and Waiting for all Pis to connect")
    print("5...")
    time.sleep(1)
    print("4...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Starting Video...")
   
def OMXcheck():
  string = os.system('sudo pgrep -l omxplayer.bin')
  return string


while True:

    if flagStart == 1:
        start_up()
        flagStart = 0        
        Popen(['omxplayer','-o','local',movie1])
        time.sleep(1)
        while flag3 == 0:
            BooMX = OMXcheck()	
            intCon = int(BooMX)
            
            if intCon != 0:
                counter = counter + 1
                if counter >= 5:
                    flag3 = 1
                    counter = 0
                    os.system('killall omxplayer')
                    print("Player is not Active")
                    SendToVideo2()      
                

    vid = data_check()
    print("This is the video to play:", vid)

    if vid == '100':
        #play video
        os.system('killall omxplayer')
        time.sleep(.1)
        Popen(['omxplayer','-o','local',movie1])
        flag3 = 0
        time.sleep(1)
        #start checking to see if video is playing
        while flag3 == 0:
            BooMX = OMXcheck()	
            intCon = int(BooMX)
            	
            if intCon != 0:
                counter = counter + 1
                if counter >= 5:
                    flag3 = 1
                    counter = 0
                    os.system('killall omxplayer')
                    print("Player is not Active")
                    
        if flag3 == 1:
            SendToVideo2()