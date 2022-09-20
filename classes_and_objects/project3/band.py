from classes_and_objects.project3.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name):
        for current in self.albums:
            if current.name == album_name:
                if current.published:
                    return f'Album has been published. It cannot be removed.'
                self.albums.remove(current)
                return f'Album {album_name} has been removed.'
        return f'Album {album_name} is not found.'

    def details(self):
        output = f'Band {self.name}\n'
        for current in self.albums:
            output += current.details() + '\n'
        return output.strip()
