def eliminate_apple(up):
    if not up:
        return ""
    
    if up.startswith("apple"):
        return eliminate_apple(up[5:])
    else:
        return up[0] + eliminate_apple(up[1:])
    
def eliminate_app_not_apple(up):
    if not up:
        return ""
    
    if up.startswith("app") and  not up.startswith("apple"):
        return eliminate_app_not_apple(up[3:])
    else:
        return up[0] + eliminate_app_not_apple(up[1:])
    
    
up="thereapplev"
print(eliminate_apple(up))
print(eliminate_app_not_apple(up))