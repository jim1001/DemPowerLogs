import re
import csv
import os

path = 'UsageLogs/In'
folder = os.fsencode(path)
filenames = []

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    #if filename.endswith( ('.jpeg', '.png', '.gif') ): # whatever file types you're using...
    filenames.append(filename)

filenames.sort() #sorts in ascending order
for file in filenames:
	print("Processing " + file + "\n")
	pathIn = "UsageLogs/In/" + file
	pathOut = "UsageLogs/Out/" + file
	f_in = open(pathIn, "r")
	f_out = open(pathOut, "w")
	reader = csv.reader(f_in)
	
	for row in reader:
		screen = row[0] # Put first element of log line into vble "screen"
		if screen[3:5] == "_3": # _3 indicates activity screen
			section = screen[0:3] # save section number
		datetime = row[1] # Put second element of log line into vble "datetime"
		if "Photo" in screen or "TextRes" in screen:
			screen = section + "_" + screen # Prepend section number
		f_out.write(screen + "," + datetime +  "\r")
	f_in.close()
	f_out.close()