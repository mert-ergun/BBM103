def f(s):
    if len(s) <= 1:
        return s
    return f(f(s[1:]))+s[0]
#Note that there is double recursion here
print(f('bab'))
print(f('baba'))