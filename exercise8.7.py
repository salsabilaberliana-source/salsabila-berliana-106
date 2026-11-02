def make_album(artist, title, songs=None):
    """Return a dictionary describing an album."""
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print(make_album("Taylor Swift", "1989"))
print(make_album("Adele", "21"))
print(make_album("Radiohead", "OK Computer"))
print(make_album("Daft Punk", "Discovery", songs=14))