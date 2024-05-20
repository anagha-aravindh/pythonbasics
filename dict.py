x={"name":"anu","age":20,"job":"teacher"}
print(x)
print(type(x))
print(len(x))
y=dict(name="abi",age=28,job="busines")
print(x["age"])
print(x.get("name"))
xy=x.keys()
print(xy)
xy=x.items()
print(xy)
print("abi" in x)
print("abi" not in x)
x["age"]=56
print(x)
x.update({"job":"supervisor"})
print(x)
x.update({"place":"thrissur"})
print(x)
x["DOB"]="3-10-2001"
print(x)
x.pop("DOB")
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
# x.clear()
# print(x)
# del x
# print(x)
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
xy=x.copy()
print(xy)
yz=dict(xy)
print(yz)
family={"child1":{"name":"anju","age":20},"child2":{"name":"aji","age":30},
        "child3":{"name":"achu","age":18}}
print(family)
print(family["child3"]["name"])
print(family["child2"]["age"])