url = "http://www.pythonchallenge.com/pc/def/map.html"
old_string  = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
not_letter = "().' /"

def translate(string):
    """ 
    pure function that solves the second python pythonchallenge
    http://www.pythonchallenge.com/pc/def/map.html
    """
    new_string = ""
    for letter in string:
        if letter in not_letter:
            new_string += letter
        else:
            new_string += chr((ord(letter)+2)%123) if (ord(letter)+2)%123> 96 else chr( ( (ord(letter)+2)%123 )+97) 
    return new_string