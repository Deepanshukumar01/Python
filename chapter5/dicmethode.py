name={
    "A":"ans",
    "B":"bns",
    "C":"cns"
}
print(name)
print(name.items())
print(name.keys())
print(name.values())

name.update({"c":"nds","D":"dns"})
print(name.items())

print(name.get("E"))       #it gives none 
#print(name["E"])           #it gives error