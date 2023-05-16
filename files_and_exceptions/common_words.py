line = "row, row, row your boat"
counted = line.count('row')
print(counted)

def count_words(filename, word):
    with open(filename) as f:
        content = f.read()
    counting = content.count(word)
    print(f"'{word}' appears {counting} times in {filename}")
