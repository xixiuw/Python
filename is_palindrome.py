def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned_text = "".join(text.lower().split())
    print("cleaned_text: ", cleaned_text)
    
    # Check if string is empty
    if not cleaned_text:
        return False
        
    # Compare characters from start and end moving inward
    left = 0
    right = len(cleaned_text) - 1
    
    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Get input and print result
text = input("Enter text to check if it's a palindrome: ")
print("It's a palindrome" if is_palindrome(text) else "It's not a palindrome")