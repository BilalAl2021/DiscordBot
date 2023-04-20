import random

def get_resonse(messag: str )->str:
    p_message = messag.lower()
    if p_message== "hello":
        return "hey there!"
    if p_message=="rool":
        return str(random.randint(1,6))
    if p_message=="!help":
        return "IDK how to help"
    return 'I didn\'t understand what you wrote. Try typing "!help".'