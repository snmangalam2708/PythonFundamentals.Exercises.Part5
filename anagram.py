def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    return(bool(sorted(first_string) == sorted(second_string)))
    # count = 0
    # s1 = list(first_string)
    # s2 = list(second_string)
    # s1.sort()
    # s2.sort()
    # for i in range(len(first_string)):
    #     if (s1[i] == s2[i]):
    #         count = count + 1
  
    # if count == len(first_string):
    #     return("True")
    # else:
    #     return("False")



# return (sorted(first_string) == sorted(second_string))

is_anagram("tip","pat")