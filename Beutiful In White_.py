#nami.music.py

import time

lirik = [
    "What we have is timeless",
    "My love is endless",
    "And with this ring I",
    "Say to the world",
    "You're my every reason",
    "You're all that i believe in",
    "With all my heart i mean every word",
    
    "So as long as live i love you",
    "Will have and hold you",
    "You look so beautiful in white",
    "And from now till my very last breath",
    "This day i'il cherish",
    "You look so beautiful in white",
    "Tonight......",
]

waktu_jeda = 4

print("memulai lagu dalam 3 detik...")
time.sleep(3)
print("\n======== Beautiful in white =======\n")

for baris in lirik:
    print(baris)
    time.sleep(waktu_jeda)

print("=======THANK YOU======")