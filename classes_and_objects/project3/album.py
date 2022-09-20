from classes_and_objects.project3.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = [x for x in args]

    def add_song(self, song: Song):
        if song in self.songs:
            return f'Song is already in the album.'
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f'Cannot add songs. Album is published.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return f'Cannot remove songs. Album is published.'
        for current in self.songs:
            if current.name == song_name:
                self.songs.remove(current)
                return f'Removed song {song_name} from album {self.name}.'
        return 'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        output = f'Album {self.name}\n'
        for current in self.songs:
            output+= f'== {current.get_info()}\n'
        return output