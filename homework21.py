'''
Homework21
Name:Drake Pierce-Demksi
github link: 
'''
def is_palindrome(string):
    # Normalize the string by removing non-alphanumeric characters and converting to lowercase
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

def is_anagram(string1, string2):
    # Normalize the strings by removing non-alphanumeric characters and converting to lowercase
    cleaned_string1 = ''.join(char.lower() for char in string1 if char.isalnum())
    cleaned_string2 = ''.join(char.lower() for char in string2 if char.isalnum())
    # Compare sorted versions of the cleaned strings
    return sorted(cleaned_string1) == sorted(cleaned_string2)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest21.py'))
