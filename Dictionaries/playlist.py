#create a spotify playlist

playlist = {
	"title": "Jeremy's playlist",
	"author": "Jeremy Marino",
	"songs": [
		{'title': 'song1', 'artist': ["blue"], "duration": 10},
		{'title': 'song2', 'artist': ["bob"], "duration": 25},
		{'title': 'song2', 'artist': ["bob"], "duration": 3}

	]
}

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']

print(f"Total length of playlist is {total_length} seconds")