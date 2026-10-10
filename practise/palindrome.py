def is_palindrome(s):
    """Assumes s is a str
       Returns True if letters in s form a palindrome; False
        otherwish. Non-letters and capitalization are ignored."""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklnmopqrstuvwxyz':
                letters += c

        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print(is_palindrome('abaaba'))