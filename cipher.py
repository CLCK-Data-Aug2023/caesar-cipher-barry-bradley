def caesar_cipher(text, shift):
    char_map = {
        'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j',
        'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o',
        'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't',
        'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y',
        'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd', 'z': 'e',
        'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J',
        'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O',
        'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T',
        'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y',
        'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'
    }

    result = ""
    for char in text:
        if char in char_map:
            result += char_map[char]
        else:
            result += char
    return result

shift = 5
text = input("Enter a string to encode: ")
encoded_text = caesar_cipher(text, shift)
print("Encoded string:", encoded_text)
