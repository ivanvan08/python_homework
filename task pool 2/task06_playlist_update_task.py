
"""
🎵 TASK 6 — Playlist Update
Topic: dict of lists (mutations) + loops

Playlist: {"rock": ["Queen", "AC/DC"], "pop": ["Adele"], "jazz": []}
Add one new artist to each genre list, then print all genres and artists.

"""
# Starter:
playlist = {"rock": ["Queen", "AC/DC"], "pop": ["Adele"], "jazz": []}
# TODO: append one artist per genre; then print genre -> list
b = []
for i in playlist:
    a = playlist.get(i)
    playlist.update(i)
print(playlist)

