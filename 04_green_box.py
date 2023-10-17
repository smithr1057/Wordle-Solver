import string
# List of words
word_list = [
    "apple", "table", "water", "fairy", "piano", "ocean", "quiet", "crazy", "jumps",
    "dream", "blank", "knife", "happy", "music", "zebra", "jokes", "quilt", "juice",
    "grape", "earth", "cable", "fence", "beard", "zebra", "shoes", "wrist", "speak",
    "camel", "quack", "vivid", "punch", "truck", "evoke", "flame", "inbox", "wheat",
    "plumb", "jelly", "frost", "globe", "brick", "quest", "swing", "world", "knock",
    "queen", "flood", "cloud", "flute", "swirl", "plaza", "twist", "crane", "giant",
    "sweep", "crown", "laser", "blink", "field", "spark", "torch", "scary", "vowel"
]

# Input for correct letters
green_letters = input("Please enter the correct letters (green box) for example ha--y: ").lower()

# get alphabet
alphabet = string.ascii_lowercase

# Make list for possible words
possible_words = [
    "apple", "table", "water", "fairy", "piano", "ocean", "quiet", "crazy", "jumps",
    "dream", "blank", "knife", "happy", "music", "zebra", "jokes", "quilt", "juice",
    "grape", "earth", "cable", "fence", "beard", "zebra", "shoes", "wrist", "speak",
    "camel", "quack", "vivid", "punch", "truck", "evoke", "flame", "inbox", "wheat",
    "plumb", "jelly", "frost", "globe", "brick", "quest", "swing", "world", "knock",
    "queen", "flood", "cloud", "flute", "swirl", "plaza", "twist", "crane", "giant",
    "sweep", "crown", "laser", "blink", "field", "spark", "torch", "scary", "vowel"
]


# Check if letter is in word
for word in possible_words:
    valid_word = True
    for letter in green_letters:
        if letter not in word:
            valid_word = False
            break
    if not valid_word:
        possible_words.remove(word)

# Print possible words
print(possible_words)
