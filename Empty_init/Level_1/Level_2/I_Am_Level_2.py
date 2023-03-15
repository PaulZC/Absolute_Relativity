if __name__ == '__main__':
    from Level_3 import I_Am_Level_3
else:
    from .Level_3 import I_Am_Level_3

def Level_2():
    print("I am Level 2")
    I_Am_Level_3.Level_3()

if __name__ == '__main__':
    Level_2()
