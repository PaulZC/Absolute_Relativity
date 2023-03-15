if __name__ == '__main__':
    from Level_2 import I_Am_Level_2
    from Level_2.Level_3 import I_Am_Level_3
else:
    from .Level_2 import I_Am_Level_2
    from .Level_2.Level_3 import I_Am_Level_3

def Level_1():
    print("I am Level 1")
    I_Am_Level_2.Level_2()
    I_Am_Level_3.Level_3()

if __name__ == '__main__':
    Level_1()
