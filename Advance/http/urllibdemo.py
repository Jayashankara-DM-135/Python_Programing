import urllib.request
with urllib.request.urlopen('http://www.python.org') as f:
    print(f.read(100).decode('utf-8'))



# req = urllib.request.Request(url='https://localhost/cgi-bin/test.cgi', data=b'This is the data passed to CGI stdin')

# with urllib.request.urlopen(req) as f:
#     print(f.read().decode('utf-8'))

# DATA = b'some data'
# req = urllib.request.Request(url="http://localhost:8080", data=DATA, method='PUT')
# with urllib.request.urlopen(req) as f:
#     pass
# # print(f.status)
# # print(f.reason)

# print(help(f))


auth_handler = urllib.request.HTPPBasicHandler()
auth_handler.add_password(realm='PDQ appliction',
                        uri="https://www.gmail.com"),
                        user="jayashankara5.drs@gmail.com",
                        passwd='88888w2229')

opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
urllin.requet.urlopen("http://www.google.com/")
