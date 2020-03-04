from http import HTTPStatus
print("ans:{}".format(HTTPStatus.OK))

if HTTPStatus.OK == 200:
    print("Ok is equal to 200")
else:
    print("OK is not 200")

print("ans:{}".format(HTTPStatus.OK.phrase))

print("Description:{}".format(HTTPStatus.OK.description))

print(list(HTTPStatus))

# print(list(http))

