from StegaPy.stegapy import create_image

def enimage(message,imgname):

    create_image(message, 'original-image.png', imgname)

#encode("Hello")