alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# create an encrypt function which take message and shift to encrypt the message
def encrypt(word,shift_amount):
    cipher_text = ""
    # going through each letter
    for i in word:
        new_index = alphabet.index(i) + shift_amount
        new_index %= len(alphabet)
        cipher_text += alphabet[new_index]
    print(f'Here is the encoded result: {cipher_text}')




# create a decrypt function which decode the cipher text
def decrypt(encode_text,shift_amount):
    normal_text = ""
    for letter in encode_text:
        new_index = alphabet.index(letter) - shift_amount
        new_index %=len(alphabet)
        normal_text += alphabet[new_index]
    print(f'Here is the decoded result: {normal_text}')


# Creating function caesar
def caesar(original_text,shift_amount,direction_of_text):
    if direction_of_text == 'encode':
        encrypt(original_text,shift_amount)
    elif direction_of_text == 'decode':
        decrypt(original_text,shift_amount)
    else:
        print('You have put wrong input')

caesar(text,shift,direction)
