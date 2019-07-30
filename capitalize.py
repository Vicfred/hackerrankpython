if __name__ == '__main__':
    s = input()
    name = ""
    name += s[0].upper()
    for idx in range(1,len(s)):
        if idx ==  len(s)-1:
            if s[len(s)-2] == " ":
                name += s[len(s)-1].upper()
            else:
                name += s[len(s)-1]
        else:
            if s[idx-1] == " ":
                name += s[idx].upper()
            else:
                name += s[idx]
    print(name)
