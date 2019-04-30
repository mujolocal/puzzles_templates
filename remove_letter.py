def rl(string, letters = "aeiouAEIOU"):
    """
    remove all letters in letters for the string default set to vowels
    
    """
    return "".join(c for c in string if c not in letters)
    
def song_decoder(song):
    """
    >>>song_decoder("AWUBBWUBC")
    "A B C"
    """
    import re
    pattern = re.compile("(WUB)+")
    return " ".join([a for a in pattern.split(song) if a != "WUB" and a != ""])
    
if __name__=="__main__":
    print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
    print(song_decoder("AWUBBWUBC"))