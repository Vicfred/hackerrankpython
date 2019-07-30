if __name__ == '__main__':
    s = input()
    hasalphanumeric = False
    hasalphabetical = False
    hasdigits = False
    haslower = False
    hasupper = False
    for c in s:
        if c.isalnum():
            hasalphanumeric = True
        if c.isalpha():
            hasalphabetical = True
        if c.isdigit():
            hasdigits = True
        if c.islower():
            haslower = True
        if c.isupper():
            hasupper = True
    print(hasalphanumeric)
    print(hasalphabetical)
    print(hasdigits)
    print(haslower)
    print(hasupper)

