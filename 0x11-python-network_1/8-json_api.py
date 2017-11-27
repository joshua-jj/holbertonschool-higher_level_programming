#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_dict = r.json()
    except:
        print("Not a valid JSON")
    if len(r_dict) == 0:
        print("No result")
    else:
        print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
