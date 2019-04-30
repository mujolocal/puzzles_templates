def scramble(s1, s2):
    """
    >>> scramble('cedewaraaossoqqyt')
    'codewars'
    """
#     s2 = [l for l in s2]
#     for letter in s1:
#         if letter in s2:
#             s2.remove(letter)
#     return not bool(s2)
    for letter in set(s2):
        print(letter)
        if s1.count(letter) >= s2.count(letter):
            return False
    return True
    
    if __name__ == "__main__":
        print(scramble('cedewaraaossoqqyt', 'codewars'))