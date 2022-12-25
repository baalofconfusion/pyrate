import track
from album import Album

class State:
    def __init__(self):
        self.album_list = []
        self.album = None
        self.name1 = None
        self.name2 = None

    def end(self):
        if self.album:
            self.album_list.append(self.a)

    def add_track(self, track):
        if not self.album:
            self.album = Album(self.name2)
        self.album.add_track(track)

    def set_name1(self, text):
        self.name1 = text

    def set_name2(self, text):
        self.name2 = text
    

def main():
    parse("./test_files/Tribe.txt") 


def parse(filename):
    state = State()
    with open(filename) as track_file:
        for line in track_file:
            line = line.rstrip()
            if not line:
                state.end()
            else:
                t = track.parse_line(line)
                if t:
                    state.add_track(t)
                elif line.startswith("\t"):
                    state.set_name2(line.strip())
                else:
                    state.set_name1(line)
    return state.album_list


if __name__ == "__main__":
    main()
