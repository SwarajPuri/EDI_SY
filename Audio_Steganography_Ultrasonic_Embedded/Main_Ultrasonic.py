from Audio_Steganography_Ultrasonic_Embedded.Ultrasound_Encryption import ultrasonic_encrypt
from Audio_Steganography_Ultrasonic_Embedded.encrypt import encrypt
from Audio_Steganography_Ultrasonic_Embedded.decrypt import decrypt

file_name =str()
def sound_encrypt(plaintext):
    ultrasonic_encrypt(plaintext)
    global file_name
    file_name = encrypt()
    return file_name

def sound_decrypt(file_name):
    decrypt(file_name)

#sound_encrypt("klmkjlkj")
#sound_decrypt()


