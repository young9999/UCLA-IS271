'''
IS271 - Assignment 4

Name: Yang Guo
'''

import csv
from datetime import timedelta
import json
import os
import collections


def total_runtime(album_file_path):
	with open(album_file_path, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		tracks = []
		totaltime = 0
		for row in reader:
			time = row['duration']
			second = int(time.split(':')[0])*60 + int(time.split(':')[1])
			totaltime += second
			tracks.append(row)
		#totaltime = timedelta(seconds = totaltime)
		totaltime = timedelta(minutes = totaltime / 60, seconds = totaltime % 60 )
	#album_file_path = "music/queens_of_the_stone_age/like_clockwork.csv"
	folder_path = os.path.split(album_file_path)[0]
	filename = os.path.split(album_file_path)[1]
	filename_original = filename  #original filename
	filename = filename.split('.csv')[0] ###.json file name
	filename = filename.replace('_', ' ')
	filename = filename.title()
	upper_path = os.path.split(folder_path)[0]
	artist_folder = os.path.split(folder_path)[1]
	artist_folder = artist_folder.replace('_',' ')
	artist_folder = artist_folder.title()
	tuple1 = (folder_path, filename)#######I do not know the use of these 2 tuples
	tuple2 = (upper_path, artist_folder)

	with open(album_file_path, 'r') as file:
		reader = csv.DictReader(file)
		tracks = []
		for row in reader:
			tracks.append(row)
	album = collections.OrderedDict()
	album['duration'] = str(totaltime)
	album['title'] = filename
	album['artist'] = artist_folder
	album['tracks'] = tracks

	#Serialize the data in a new JSON file
	#album_file_path = "music/queens_of_the_stone_age/like_clockwork.csv"
	new_filename = filename_original.split('.csv')[0] + '_v2.json' #new_filename is XXXXX_v2.json
	new_path = album_file_path.split('/')[0] + '/' + album_file_path.split('/')[1]


	with open(os.path.join(new_path, new_filename), 'w') as outputfile:
		outputfile.write(json.dumps(album, indent = 2))

#run
if __name__ == "__main__":
	total_runtime("music/queens_of_the_stone_age/like_clockwork.csv")
