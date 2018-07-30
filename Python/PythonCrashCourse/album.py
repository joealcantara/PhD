def make_album(artist_name, album_title, num_tracks = ''):
    album = {'artist_name': artist_name, 'album_title': album_title}
    if num_tracks:
        album['num_tracks'] = num_tracks
    return album

album1 = make_album("Ed Sheeran", "Divid")
print(album1)
album2 = make_album("Oasis", "The Masterplan")
print(album2)
album3 = make_album("S Club 7", "S Club Party", num_tracks=8)
print(album3)
