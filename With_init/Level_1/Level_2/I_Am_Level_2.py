if __name__ == '__main__':
    import Level_3
else:
    from . import Level_3

def Level_2():
    print("I am Level 2")
    Level_3.I_Am_Level_3.Level_3()

if __name__ == '__main__':
    Level_2()
