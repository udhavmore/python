from operator import le


def mid(string: str):
    if len(string)%2 != 0:
        return string[len(string)//2]
    else:
        return ""


print(mid("udhavmore"))
