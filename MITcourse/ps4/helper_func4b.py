def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
                another letter (string). 
    '''
    letter_mapping = {}
    alph_lower = 'abcdefghijklmnopqrstuvwxyz'
    alph_upper = alph_lower.upper()
    for i in range(len(alph_lower)):
        letter_mapping[alph_lower[i]] = alph_lower[(i+shift)%26]
        letter_mapping[alph_upper[i]] = alph_upper[(i+shift)%26]
    return letter_mapping




def apply_shift(shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        
    
    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
            down the alphabet by the input shift
    '''
    message_text = 'bqyg ukq'
    letter_mapping = build_shift_dict(shift)
    n = len(message_text)
    encrypted_text = ''
    for i in range(n):
        if message_text[i] in letter_mapping:
            encrypted_text = encrypted_text + letter_mapping[message_text[i]]
        else:
            encrypted_text = encrypted_text + message_text[i]
    return encrypted_text

print(apply_shift(4))
print('a', 'ab')

L = []
s = 'sd sdk dkadj'
for i in s.split():
    L.append(i)
print(L)