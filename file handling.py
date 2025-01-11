
#### 3.1 File Handling

def word_counter(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found!"

# Test it
print(word_counter('sample.txt'))
