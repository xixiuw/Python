#https://edube.org/learn/pe-2/lab-improving-the-caesar-cipher-3
print("Please input your text")
text = input()
print("Please input the shift value between 1 and 25")
shift = int(input())

# Create an empty string to store the result
cipher_text = ""

for char in text:
    if char.isalpha():
        if char.isupper():
            char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        cipher_text += char
    else:
        cipher_text += char

# Print the complete encrypted text
print(cipher_text)

