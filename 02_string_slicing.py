greeting = "Good Morning, "
name = "neha"
print(type(name))
print(greeting + name)

# Concatenating two strings
c= greeting + name
print(c)

name = "neha"
print(name[3])
# # name[3]="d"  --> Does not work

print(name[0:3])  # including 0 but excluding 3
print(name[0:4])
print(name[1:4])
print(name[:2])  # is same as name[0:2]
print(name[0:])   # is same as name[0:4]
c = name[-4:-1]   # same as name[0:3]
print(c)


