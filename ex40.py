class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
        self._counter = 0

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def policz_linie(self):
        self._counter = 0
        for line in self.lyrics:
            self._counter += 1
        print(self._counter)

    def dodaj_linie(self, linia):
        self.lyrics.append(linia)


happy_bday = Song(["Happy birthday to you",
                   "I don;t want to get sued",
                   "So I'll stop right there"])

happy_bday.sing_me_a_song()

happy_bday.policz_linie()

happy_bday.dodaj_linie("sgdvisoghwsibisdk")

happy_bday.sing_me_a_song()
happy_bday.policz_linie()
print(happy_bday._counter)