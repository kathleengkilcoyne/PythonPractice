class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        veryfirst = self.name
        RepeatFlag = False
        if self.next == veryfirst:
            RepeatFlag = True
        return RepeatFlag
        """returns: (bool) True if the playlist is repeating, False if not.
        """



first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist())