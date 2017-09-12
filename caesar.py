from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    #text=str(input("What would you like to translate?"))
    #rot=int(input("What should the encryption key be? (Please use only numbers)"))
    x=0
    translation=[]
    for characters in text:
        translation.append(rotate_character(text[x], rot))
        x=x+1
    translation=''.join(translation)
    return(translation)

        
