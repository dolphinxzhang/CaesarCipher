def Encryption(n, plaintext):
    """
    Encrypts the string and returns the encoded ciphertext

    n: type integer; represents the shift value
    plaintext: type str, text to be encoded
    """
    
    result = ''

    return result


def Decryption(n, ciphertext):
    """
    Decrypts the string and returns the decoded plaintext

    n: type integer; represents the shift value
    ciphertext: type str, text to be decoded
    """
    import string
    alphabet = list(string.ascii_lowercase)
    word=" "
    for c in ciphertext:
        position=alphabet.index(c)
        print position # find position of character in the alphabet list
        ogposition=position - n #find the original character's position in the alphabet list
        character= alphabet[ogposition]
        word+= character
        
    result = word

    return result


def Display(n, plaintext):
    """
    Generates the results of the Caesar cipher.
    
    n: type integer; represents the shift value
    plaintext: type str, text to be encoded
    """

    encryption = Encryption(n, plaintext)
    decryption = Decryption(n, encryption)

    print 
    print 'Shift amount: %d' % n
    print 'Input text: %s' % plaintext
    print
    print 'Encrytped text: %s' % encryption
    print 'Decrytped text: %s' % decryption
    print


if __name__ == '__main__':
    
    text = raw_input('Enter plaintext: ')
    shift = int(raw_input('Enter a shift amount: '))
    Display(shift, text)
