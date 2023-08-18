# write a program that can take name in lower case and return it in upper case
def con1(string1):
    return string1.upper()


str_ing = input("entre a string: ").split()
ans = list(map(con1, str_ing))
print(ans)

print("thx :)")
# ---------------------------------
