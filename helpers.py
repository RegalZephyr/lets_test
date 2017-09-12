def alphabet_position(letter):
    translation=ord(letter)
    if letter.isupper()==True:
        translation=translation-65
    elif letter.islower()==True:
        translation=translation-97
    return(translation)
def rotate_character(char, rot):
    translation=""
    if char.isalpha()==False:
        return(char)
    elif char.isupper()==True:
        new_number=alphabet_position(char)
        translation=new_number+rot+65
        while translation>90:
            translation=translation-26
        translation=chr(translation)
    elif char.islower()==True:
        new_number=alphabet_position(char)
        translation=new_number+rot+97
        while translation>122:
            translation=translation-26
        translation=chr(translation)
    return(translation)