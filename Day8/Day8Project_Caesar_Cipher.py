alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Creating function caesar
def caesar(original_text,shift_amount,direction_of_text):
    cipher = ""
    if direction_of_text == 'decode':
        shift_amount *= -1
    for letter in original_text:
        new_index = alphabet.index(letter) + shift_amount
        new_index %= len(alphabet)
        cipher+= alphabet[new_index]
    print(f'Here is your {direction_of_text} with result {cipher}')

caesar(text,shift,direction)
