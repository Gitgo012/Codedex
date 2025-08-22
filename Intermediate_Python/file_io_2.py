liked_songs={'Woh': 'Khatth ft. Stithi', 'Closer': 'The Chainsmokers', 'Wolves': 'Selena Gomez', 'End of Beginning': 'Djo'}
file_name='music_file.txt'
def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write("Liked Songs: \n")
        for i, (song, artist) in enumerate(liked_songs.items()):
            file.write(f"{i+1}. {song} by {artist}\n")
    
write_liked_songs_to_file(liked_songs, file_name)
with open(file_name, 'r') as file:
    content=file.read()
    print(content)    