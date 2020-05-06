def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    v = value.replace(" ", "").lower()
    if (v == v[::-1]):
        return True
    else:
        return False

