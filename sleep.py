import os
import time

# time constants are in seconds
SONG_START_TIME = 14.88
SONG_END_TIME = 28 # this should actually be around 29-30s, but this caused the sound to not sync with the countdown properly, so I added an offset
OFFSET = 0.18

os.startfile('media\outro.mp3')
time.sleep(SONG_START_TIME)
os.startfile('media\ded.jpg')

print('Your PC is gonna die in:')
time.sleep(OFFSET)

wait_time = round(SONG_END_TIME - SONG_START_TIME)
for i in range(wait_time):
    time.sleep(1)
    print(wait_time - i - 1)

print("\ngoodnight")
os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0') # puts the pc to sleep