import uuid

def unique_identifiers4():
    Uuid4 = uuid.uuid4()
    print("Generated Unique Identifier 4:",Uuid4)
def unique_identifiers1():
    Uuid1 =uuid.uuid1()
    print("Generated Unique Identifier 1:",Uuid1)
def unique_identifiers3():
    namespace = uuid.NAMESPACE_DNS
    print("Generated Unique Identifier 3:")
    print(uuid.uuid3(namespace, "example.com"))
def unique_identifiers5():
    namespace = uuid.NAMESPACE_DNS
    print("Generated Unique Identifier 5:")
    print(uuid.uuid5(namespace, "example.com"))  
