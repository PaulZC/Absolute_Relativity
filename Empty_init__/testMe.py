from Level_1 import I_Am_Level_1
from Level_1.Level_2 import I_Am_Level_2
from Level_1.Level_2.Level_3 import I_Am_Level_3

def runTest():
    print("I Am Main")
    I_Am_Level_1.Level_1()
    I_Am_Level_2.Level_2()
    I_Am_Level_3.Level_3()

runTest()
