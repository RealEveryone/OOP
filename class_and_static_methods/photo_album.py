from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return PhotoAlbum(pages)

    def add_photo(self, label: str):
        # def slot_number():
        #     return len(self.photos[self.page_number - 1])
        #
        # if len(self.photos[self.page_number - 1]) == 4:
        #     self.page_number += 1
        #
        # if self.page_number > self.pages:
        #     return f'No more free slots'
        #
        # self.photos[self.page_number - 1].append(label)
        # return f'{label} photo added successfully on page {self.page_number} slot {slot_number()}'

        for row, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f'{label} photo added successfully on page {row + 1} slot {len(page)}'
        return f'No more free slots'

    def display(self):
        divider = '-' * 11 + '\n'
        output = divider
        for current_page in self.photos:
            if current_page:
                output += ' '.join(['[]' for _ in range(len(current_page))]) + '\n'
            else:
                output += '\n'
            output += divider
        return output.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
