if __name__ == '__main__':
    import Level_2
else:
    from . import Level_2

def Level_1():
    print("I am Level 1")
    Level_2.Level_2()
    Level_2.Level_3.Level_3()

if __name__ == '__main__':
    Level_1()
