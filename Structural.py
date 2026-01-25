#This is harder to demonstrate than my other patterns.

#Imagine there is an old music player, that plays by title.
#There is now multiple songs with the same title.
#A new interface is developed that plays by unique song ID.
#Although the new system is better, many users still want to use the old system one until the new one is more polished.
#An adapter is created to translate between these two systems.

#This may not be the best explanation or example, but its the best I could come up with.

#Old System
class SimpleMusicPlayer:
    def __init__(self):
        pass

    def playSongByTitle(self, songTitle):
        print(f"Playing song: {songTitle}")


#New System
class AdvancedMusicPlayer:
    def __init__(self):
        pass

    def playSongById(self, song_id):
        print(f"Playing song with ID: {song_id}")


#Adapter
class TitleToIdAdapter(SimpleMusicPlayer):
    def __init__(self, advancedPlayer):
        self.advancedPlayer = advancedPlayer

        # Song title → ID mapping
        self.songLibrary = {
            "Bohemian Rhapsody": 12455122,
            "Stairway to Heaven": 99887766,
            "Hotel California": 55443322
        }

    def playSongByTitle(self, songTitle):
        print(f"Adapter: Translating '{songTitle}' to ID...")

        song_id = self.songLibrary.get(songTitle)

        if song_id:
            self.advancedPlayer.playSongById(song_id)
        else:
            print(f"Error: '{songTitle}' not found in library.") #(NeetCode, 2023)


simplePlayer = SimpleMusicPlayer()
simplePlayer.playSongByTitle("Bohemian Rhapsody")

adapter = TitleToIdAdapter(AdvancedMusicPlayer())
adapter.playSongByTitle("Stairway to Heaven")

#References

#NeetCode (2023). 8 Design Patterns EVERY Developer Should Know. YouTube. Available at: https://www.youtube.com/watch?v=tAuRQs_d9F8.[Accessed 25/01/2026]