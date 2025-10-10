
"""
🎵 TASK 6 — Playlist Update
Topic: dict of lists (mutations) + loops

Playlist: {"rock": ["Queen", "AC/DC"], "pop": ["Adele"], "jazz": []}
Add one new artist to each genre list, then print all genres and artists.

"""
import random

# Starter:
playlist = {"rock": ["Queen", "AC/DC"], "pop": ["Adele"], "jazz": []}
# TODO: append one artist per genre; then print genre -> list
for i in playlist:
    a = playlist[i]
    for c in range(3):
        b = random.randint(1, 3)
        if b == 1:
            artist = "Mikel Jackson"
        if b == 2:
            artist = "Billie Eilish"
        if b == 3:
            artist = "Mozart"
    playlist[i].append(artist)
print(playlist)

