import re
from album import Album
from track import Track


class State:
    def __init__(self):
        self.album_list = []
        self.album = None
        self.name1 = None
        self.name2 = None

    def end(self):
        if self.album:
            self.album_list.append(self.album)

    def add_track(self, track):
        if not self.album:
            self.album = Album(self.name2, self.name1)
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
                track = parse_line(line)
                if track:
                    state.add_track(track)
                elif line.startswith("\t"):
                    state.set_name2(line.strip())
                else:
                    state.set_name1(line)
        state.end()
    return state.album_list


def parse_line(line):
    if match := re.search(r"([\*\+]*)\t\t(\d+)\. (?:(?:(.*?)(?: -- )(.*))|(.*))", line):
        # group 2 is the track number which is not being used right now
        rating = parse_rating(match.group(1))
        title = match.group(4)
        if title == None:
            title = match.group(5)
        return Track(title, rating, match.group(3))
    return None


def parse_rating(text):
    val = text.count("*") + (text.count("+") * 0.5)
    if val < 0.5:
        return None
    else:
        return val


if __name__ == "__main__":
    main()
