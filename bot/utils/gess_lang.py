from guesslang import Guess

guess = Guess()


def gess_language_name(msg_string: str) -> str:
    """
    return the language name 
    """
    language = guess.language_name(msg_string)
    return language
