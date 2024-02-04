def is_palindrome(input_string):
    cleaned_input = ''.join(input_string.split()).lower()
    return cleaned_input == cleaned_input[::-1]

# Example usage:
word = "madam"
result = is_palindrome(word)
print(result)