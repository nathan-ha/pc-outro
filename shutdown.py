import os
import time

# both constants are in seconds
SONG_START_TIME = 14.88
SONG_END_TIME = 28 # technically it should be ~30, but the offset accounts for it
OFFSET = 0.18

os.startfile('media\outro.mp3')
time.sleep(SONG_START_TIME)
os.startfile('media\ded.jpg')

print('Your PC is gonna die in:')
time.sleep(OFFSET)

wait_time = round(SONG_END_TIME - SONG_START_TIME)
for i in range(wait_time):
    time.sleep(1)
    print(wait_time - i)

print("\nI WANNA LIVE")
os.system("shutdown -s -t 0")
