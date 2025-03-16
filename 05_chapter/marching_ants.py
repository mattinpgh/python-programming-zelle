# The Ants go Marching

def sing_song(song_dict):
    for k, v in song_dict.items():
        h = "hurrah, hurrah!"
        number = k
        activity = v
        song_lyrics = (f"The ants go marching {number} by {number}, {h}\n"
        f"The ants go marching {number} by {number}, {h}\n"
        f"The ants go marching {number} by {number},\n"
        f"The little one stops to {activity},\n"
        "And they all fo marching down...\n"
        "In the ground...\n"
        "To get out...\n"
        "Of the rain.\n"
        "Boom! Boom! Boom!")
        print(song_lyrics)

child_activities = {
    "one": "have some fun",
    "two": "tie a shoe",
    "three": "climb a tree",
    "four": "knock on the door",
    "five": "watch bees in a hive",
    "six": "pick up sticks",
    "seven": "count to eleven",
    "eight": "close the gate",
    "nine": "read a sign",
    "ten": "feed the hen"
}

sing_song(child_activities)
