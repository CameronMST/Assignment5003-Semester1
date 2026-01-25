class Song:
    def __init__(self, title):
        self.title = title
        self.next_song = 0

class Playlist:
    def __init__(self, first_song):
        self.first_song = first_song
        self.current_song = None
    
    def __iter__(self):
        self.current_song = self.first_song
        return self

    def __next__(self):
        if self.current_song:
            title_to_return = self.current_song.title
            self.current_song = self.current_song.next_song
            return title_to_return
        else:
            raise StopIteration
    
song1 = Song("Bohemian Rhapsody")
song2 = Song("Stairway to Heaven")
song3 = Song("Hotel California")            
            
song1.next_song = song2
song2.next_song = song3

my_playlist = Playlist(song1)

for song_title in my_playlist: #(NeetCode, 2023)
    print(f"Now playing - {song_title}")
    time = 0
    while time < 100000000:
        time +=1 #Simulating Time Delay, Since we're not allowed to import any libraries.
print("Playlist ended.")


#References

#NeetCode (2023). 8 Design Patterns EVERY Developer Should Know. YouTube. Available at: https://www.youtube.com/watch?v=tAuRQs_d9F8.[Accessed 25/01/2026]