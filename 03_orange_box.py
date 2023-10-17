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

# Initialize an empty list for possible words
possible_words = []
possible_words = word_list
checked_words = []

# Input for the correct letters in the wrong position (yellow box)
yellow_letters = \
    input("Please enter the correct letters that are in the wrong place (yellow box): ")
print()

# Filter the words based on the input orange letters
for word in possible_words:
    valid_word = True

    # Check if the letters in the yellow_letters match the word
    for i, letter in enumerate(yellow_letters):
        if letter != '-' and letter == word[i]:
            valid_word = False
            break

    # Check if the word contains any letters not in yellow_letters
    for letter in yellow_letters:
        if letter != '-' and letter not in word:
            valid_word = False
            break

    if valid_word:
        checked_words.append(word)

# reset lists
possible_words = checked_words
checked_words = []

# Print the possible words
print(possible_words)
