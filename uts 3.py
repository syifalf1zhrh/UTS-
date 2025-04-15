#program Inherintance, Polymorphism, Abstarct Class

from abc import ABC, abstractmethod

class ABBA(ABC):
    def __init__(self, title, artist= "ABBA"):
        self.title = title
        self.artist = artist

    @abstractmethod
    def show(self):
        pass

class ABBASong(ABBA):
    def show(self):
        return (f" {self.title} by {self.artist}")
    
def cetak_info(ABBA, index):
    print(f"{index}. {ABBA.show()}")
       

print ("Write down your favorite ABBA songs !!!!! ")
jumlah = int(input("\nHow many songs do you want to add? "))

list_songs = []

for i in range(jumlah):
    title = input(f"Enter the title of song {i+1}: ")
    songs= ABBASong(title)
    list_songs.append(songs)

print("\nYour Favorite ABBA Songs:")
for index, songs in enumerate(list_songs, start=1):
    cetak_info(songs,index)

print("\nThank you for sharing your favorite ABBA songs!")