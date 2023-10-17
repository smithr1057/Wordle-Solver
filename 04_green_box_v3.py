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
green_letters = input("Please enter the correct letters (green box) for example ha--y would be happy: ").lower()


# Make list for possible words
possible_words = []

# Filter the words based on the input letters
for word in word_list:
    valid_word = True
    for i, letter in enumerate(green_letters):
        if letter != '-' and letter != word[i]:
            valid_word = False
            break
    if valid_word:
        possible_words.append(word)

# Print possible words
print(possible_words)
