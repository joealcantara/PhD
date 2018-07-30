def make_album(artist_name, album_title, num_tracks = ''):
    album = {'artist_name': artist_name, 'album_title': album_title}
    if num_tracks:
        album['num_tracks'] = num_tracks
    return album

response = ''
while response.lower() != 'no':
    a_name = input('Please enter the name of the artist : ')
    a_title = input('\nPlease enter the name of the album : ')
    n_tracks = input('\nPlease enter the number of tracks on the album ')
    if n_tracks:
        album = make_album(a_name, a_title, n_tracks)
    else:
        album = make_album(a_name, a_title)
    print(album)
    response = input('\nWould you like to put in a new album (yes/no)?')

print("end of program.")