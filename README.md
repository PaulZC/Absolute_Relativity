# Absolute Relativity

It took me a _long_ time to figure out where I was going wrong with relative and absolute imports in Python3.
I'm sharing this to hopefully save you some time if you're attempting to do the same thing.

## Thanks!

[This post by BrenBarn](https://stackoverflow.com/a/14132912) really helped me figure out what was going on...

This post helped too:

[![No Idea](img/AndyRelativeImports.jpg)](https://iq-inc.com/importerror-attempted-relative-import/)

## Objective

To create nested packages with modules that can all be run individually as __main__.

```
.
└── Empty_init/
    ├── testMe.py
    └── Level_1/
        ├── __init__.py
        ├── I_Am_Level_1.py
        └── Level_2/
            ├── __init__.py
            ├── I_Am_Level_2.py
            └── Level_3/
                ├── __init__.py
                └── I_Am_Level_3.py
```

Simple right? Well, kind of. It took me a long time to figure out that you need to import the sub-packages differently
depending on whether you are running as __main__ or as an imported module. E.g.:

```
if __name__ == '__main__':
    from Level_3 import I_Am_Level_3
else:
    from .Level_3 import I_Am_Level_3

def Level_2():
    print("I am Level 2")
    I_Am_Level_3.Level_3()

if __name__ == '__main__':
    Level_2()
```

## Empty \_\_init\_\_.py files

### Level_3

```
cd Empty_init\Level_1\Level_2\Level_3
python I_Am_Level_3.py
```

produces:

* **I am Level 3**

### Level_2

```
cd ..
python I_Am_Level_2.py
```

produces:

* **I am Level 2**
* **I am Level 3**

### Level_1

```
cd ..
python I_Am_Level_1.py
```

produces:

* **I am Level 1**
* **I am Level 2**
* **I am Level 3**
* **I am Level 3**

Note that **I am Level 3** appears twice - because it is printed by both ```Level_2()``` and ```Level_3()```

### main

```
cd ..
python testMe.py
```

produces:

* **I Am Main**
* **I am Level 1**
* **I am Level 2**
* **I am Level 3**
* **I am Level 3**
* **I am Level 2**
* **I am Level 3**
* **I am Level 3**

```testMe.py``` is:

```
from Level_1 import I_Am_Level_1
from Level_1.Level_2 import I_Am_Level_2
from Level_1.Level_2.Level_3 import I_Am_Level_3

def runTest():
    print("I Am Main")
    I_Am_Level_1.Level_1()
    I_Am_Level_2.Level_2()
    I_Am_Level_3.Level_3()

runTest()
```

## Populated \_\_init\_\_.py files

For more absolute relative fun, check out the ```With_init``` folder:

```
.
└── With_init/
    ├── testMe.py
    └── Level_1/
        ├── __init__.py
        ├── I_Am_Level_1.py
        └── Level_2/
            ├── __init__.py
            ├── I_Am_Level_2.py
            └── Level_3/
                ├── __init__.py
                └── I_Am_Level_3.py
```

E.g. ```__init__.py``` in ```Level_2``` can be:

```
from .I_Am_Level_2 import Level_2
```

```testMe.py``` can be simplified to:

```
import Level_1

def runTest():
    print("I Am Main")
    Level_1.I_Am_Level_1.Level_1()
    Level_1.Level_2.I_Am_Level_2.Level_2()
    Level_1.Level_2.Level_3.I_Am_Level_3.Level_3()

runTest()
```

## No I\_Am\_

Do we need those helpful **I\_Am\_**'s in the module names? No, not really.
Try the ```No_I_Am``` folder for more absolute relative headache-inducing fun!

```
.
└── No_I_Am/
    ├── testMe.py
    └── Level_1/
        ├── __init__.py
        ├── Level_1.py
        └── Level_2/
            ├── __init__.py
            ├── Level_2.py
            └── Level_3/
                ├── __init__.py
                └── Level_3.py
```

Enjoy!

Paul
