def caesar_cipher(text, shift):
    d_t = []
    for word in text:
        if word.isalpha():  
            shift_base = ord('a') if word.islower() else ord('A')
            d_t.append(chr((ord(word) - shift_base - shift) % 26 + shift_base))
        else:
            d_t.append(word)  
    return ''.join(d_t)

# Example usage
e_t = "wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}"
shift_value = 7
print(caesar_cipher(e_t, shift_value))