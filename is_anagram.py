"""
def is_anagram(text1, text2):
    # Remove spaces and convert to lowercase
    cleaned_text1 = "".join(text1.lower().split())
    cleaned_text2 = "".join(text2.lower().split())
    
    # Check if either string is empty
    if not cleaned_text1 or not cleaned_text2:
        return False
        
    # Sort both strings and compare
    return sorted(cleaned_text1) == sorted(cleaned_text2)

# Get input from user
text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

# Print result
print("These are anagrams" if is_anagram(text1, text2) else "These are not anagrams")

"""
#Here is the code with the Counter function

from collections import Counter

def is_anagram(text1, text2):
    # Remove spaces and convert to lowercase
    cleaned_text1 = "".join(text1.lower().split())
    cleaned_text2 = "".join(text2.lower().split())
    
    # Check if either string is empty
    if not cleaned_text1 or not cleaned_text2:
        return False
    
    # Use Counter to count characters in both strings
    return Counter(cleaned_text1) == Counter(cleaned_text2)

# Get input from user
text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

# Print result
print("These are anagrams" if is_anagram(text1, text2) else "These are not anagrams")
