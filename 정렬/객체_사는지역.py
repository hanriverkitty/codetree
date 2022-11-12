n = int(input())
arr = [list(input().split()) for i in range(n)]
arr.sort()



class Address:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

people = [Address(name,address,region) for name,address,region in arr]

print(f"name {people[-1].name}")
print(f"addr {people[-1].address}")
print(f"city {people[-1].region}")