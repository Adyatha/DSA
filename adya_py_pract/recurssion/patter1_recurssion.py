# ****
# ***
# **
# *
def pattern(row , col):
    if row == 0:
        return None
    if col < row:
        print("*", end=" ")
        pattern(row , col+1)
    else:
        print("")
        pattern(row-1 , 0)

pattern(4,0)