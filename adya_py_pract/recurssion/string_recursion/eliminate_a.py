# def eliminate_a(p,up):
#     if not up:
#         return p
        
#     char = up[0]
    
#     if char == "a":
#         return eliminate_a(p,up[1:])
#     else:
#         return eliminate_a(p+char,up[1:])

def eliminate_a_without_p(up):
    if not up:
        return ""
        
    char = up[0]
    
    if char == "a":
        return eliminate_a_without_p(up[1:])
    else:
        return char + eliminate_a_without_p(up[1:])
        
# p=''
# up="baccab"
# print(eliminate_a(p,up))

up = "bcaaan"
print(eliminate_a_without_p(up))