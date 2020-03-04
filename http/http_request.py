import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")

r1=conn.getresponse()

print(r1.status, r1.reason)

data = r1.read()

# print(data)

conn.request("GET", "/")

r2 = conn.getresponse()

# while not r2.closed:
#     print(r2.read(10))



conn = http.client.HTTPSConnection("www.google.com")
conn.request("HEAD", "/")
r3 = conn.getresponse()
print(r3.status, r3.reason)

data = r3.read()

print(len(data))
print(data)

print(data == b'')

conn = http.client.HTTPSConnection("www.facebook.com")
conn.request("GET", "/")
r1 = conn.getresponse()

data = r1.read()

print(r1.status, r1.reason)

print(len(data))

