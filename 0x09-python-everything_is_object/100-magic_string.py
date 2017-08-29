#!/usr/bin/python3
def magic_string(H=[]):
    print(id(H))
    H += ["Holberton"]
    return (", ".join(H))
