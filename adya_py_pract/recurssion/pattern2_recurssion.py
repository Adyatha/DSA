# *
# **
# ***
# ****

def pattern(row , col):
    if row == 0:
        return None
    if col < row:
        pattern(row , col+1)
        print("*", end=" ")
    else:
        pattern(row-1 , 0)
        print()

pattern(4,0)