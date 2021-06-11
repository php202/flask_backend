import uuid
def uudiv4():
    x = uuid.uuid4()
    return x

def uudiv5(password):
    x = uuid.uuid5(uuid.NAMESPACE_DNS,password)
    return x

if __name__ == '__main__':
    x = uudiv5("happy")
    print(x)
    