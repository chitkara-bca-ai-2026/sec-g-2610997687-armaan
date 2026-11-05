print("=" * 40)
print("         TEXT PROCESSING TOOL")
print("=" * 40)

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

# Character indexing
position = int(input("Enter position for indexing: "))

if 0 <= position < len(sentence):
    print("Character at position", position, ":",
          repr(sentence[position]))
else:
    print("Invalid position!")

# String slicing
start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))

if 0 <= start <= len(sentence) and 0 <= end <= len(sentence):
    print(f"Sliced string [{start}:{end}] :",
          repr(sentence[start:end]))
else:
    print("Invalid slicing indices!")

# Convert to uppercase
print("Uppercase             :", sentence.upper())

# Convert to lowercase
print("Lowercase             :", sentence.lower())

# Replace a word
word = input("Enter word to replace: ")
replacement = input("Enter replacement word: ")

new_sentence = sentence.replace(word, replacement)

print("After replace         :", new_sentence)

# Find length
print("Length of sentence    :", len(sentence))

print("\n" + "=" * 40)
print("Analysis Complete!")
print("="*40)