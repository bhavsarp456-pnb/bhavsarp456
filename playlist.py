playlist = {'title':'morning travel',
            'author':'Piyush Bhavsar',
            'songs': [
                {'title':'one',
                'artist':'metallica',
                'album':'...and justice for all',
                'duration':7.44},
                {'title':'Indigrove',
                'artist':'chineseman',
                'album':'Indigrove',
                'duration':4.088},
                {'title':'One Step Closer',
                'artist':'LinkinPark',
                'album':'Hybrid Theory',
                'duration':6.55}
            ]
        }
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
    print(f"Total Playlist Duration: {total_length}")