# Make list for possible words
possible_words = [
    "apple", "table", "water", "fairy", "piano", "ocean", "quiet", "crazy", "jumps",
    "dream", "blank", "knife", "happy", "music", "zebra", "jokes", "quilt", "juice",
    "grape", "earth", "cable", "fence", "beard", "zebra", "shoes", "wrist", "speak",
    "camel", "quack", "vivid", "punch", "truck"
]

checked_words = []

# Input for correct letters
green_letters = input("Please enter the correct letters (green box): ").lower()
print()

for word in possible_words:
    valid_word = True
    for i, letter in enumerate(green_letters):
        if letter != '-' and letter != word[i]:
            valid_word = False
            break
    if valid_word:
        checked_words.append(word)

# reset lists
possible_words = checked_words
checked_words = []

# Print the possible words
print(possible_words)
print(checked_words)
