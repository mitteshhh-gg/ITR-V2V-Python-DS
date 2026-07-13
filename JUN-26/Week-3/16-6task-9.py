text = input("Enter a sentence : ").lower()
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word,0) + 1

print("\nWord Frequeny:")
for word,count in freq.items():
    print(f"{word}: {count}")

