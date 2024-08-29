def add(firstName:str | None, lastName:str=None):
    return firstName + " " + lastName

fname="vraj"
lname ="Clerk"

name=add(fname.capitalize(),lname)
print(name)