from StegaPy.stegapy import decode_image

def deimage(imgname):
    decoded = decode_image(imgname)
    print("Successfully decoded : ",decoded)

