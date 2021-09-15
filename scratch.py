power_of_alfavit = 209145
message = input('Введите текстовое сообщение:')
print("Ваше текстовое сообщение:", message)
key = input('Введите ключ(key):')
print("Ваш ключ:", key)


def crypter(input_message,key):
    key *= len(input_message) // len(key) + 1
    encrypted_message  = ''
    for i,j in enumerate(input_message):
        encrypted_message += chr((ord(j) + ord(key[i])) % power_of_alfavit)
    return(encrypted_message)



def decrypter(encrypted_message ,key):
    key *= len(message) // len(key) + 1
    decrypter_message= ''
    for i,j in enumerate(encrypted_message):
        decrypter_message += chr((ord(j) - ord(key[i])) % power_of_alfavit )
    return(decrypter_message)


shifr = crypter(message,key)
print('Шифрованное слово : {}'.format(shifr))
deshifr = decrypter(shifr,key)
print('Дешифрованное слово : {}'.format(deshifr))














