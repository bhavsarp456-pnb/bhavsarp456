playlist = {'title':'morning travel',
            'author':'Piyush Bhavsar',
            'songs': [
                {'title':'Man Usiki karo prathna',
                'artist':'Jaydeep Swadiya',
                'album':'Prayers',
                'duration':7.13},
                {'title':'Nathaji Nirakhi mara',
                'artist':'Gondal Bal vrund',
                'album':'Sukhkari Ganshyam',
                'duration':7.10},
                {'title':'Aksharpurshottam na danka',
                'artist':'BAPS Sant Vrund',
                'album':'Aje Yagnapurushne Dwar',
                'duration':13.17}
            ]
        }
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
    print(f"Total Playlist Duration:{total_length}")