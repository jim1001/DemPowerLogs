import re
import csv
f = open("UsageLogs/In/26_6_2018.txt", "r") # Open file for reading
f_out = open("UsageLogs/Out/26_6_2018_out.txt", "w",encoding='utf-8') # Open file for (over-)writing
reader = csv.reader(f)
for row in reader:
    screen = row[0] # Put first element of log line into vble "screen"
    if screen[3:5] == "_3": # _3 indicates activity screen
        section = screen[0:3] # save section number
    datetime = row[1] # Put second element of log line into vble "datetime"
    if "Photo" in screen or "TextRes" in screen:
        screen = section + "_" + screen # Prepend section number
    f_out.write(screen + "," + datetime +  "\r")
f.close()                   # Free up system resources.