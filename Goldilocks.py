import math
import tkinter
import tkinter.ttk
"""GLOBAL TRUTHS
These are true no matter what you're doing, so lock them in here.
Prefill into GUI, but they can be overwritten.
"""
MaterialLength = 6000
MinLILO = 10
"""
UNIT TEST SECTION
Test each function individually
"""

def Tests():
    return()

"""
FUNCTION SECTION
Contains all functions used
"""

#Basic Panel Calc Functions
#Contains functions for the number of slats, the lilo, how long the slats are,
#And whether the panel is acceptable.
def LILOcalc(Height,Slats,Slat,Spacing):
    val = (Height - (Slats*Slat) -((Slats-1)*Spacing))/2
    return val

def SpecifiedLIcalc(Height,Slats,Slat,Spacing,LI):
    val = (Height - (Slats*Slat) -((Slats-1)*Spacing))-LI
    return val

def NumSlatcalc(Height,Slat,Spacing):
    return math.floor(Height/(Slat+Spacing))

def SlatSizecalc(Length,material):
    return(Length-((material*2)-30))

def Acceptable(Spacing,LILOorLO):
    if (LILOorLO <= Spacing and LILOorLO >=MinLilo):
        Result = True
    else:
        Result = False
    return(Result)

def ReqChange(Height,LILOorLO,Spacing,Slat):
    newHeightlower = Height-(LILOorLO-MinLILO)
    newHeightupper = Height-LILOorLO+Spacing+Slat+MinLILO
    
    return(newHeightupper, newHeightlower)

def ListCheck(List1,List2,List3):
    if len(List1)==len(List2)==len(List3):
        passed = True
    else:
        passed = False
    return(passed)

#Underestimator Functions
#Contains stock requirement estimator using Lineal Metres.
#Will almost always underestimate required stock

def LinealEstimate(Length,Number):
    return math.ceil((Length*Number)/MaterialLength)

#Overestimator Functions
#Contains stock requirement estimator using conservative methods
#Will almost always overestimate required stock

def SafeEstimate(Length,Number):
    perSlat = math.floor(MaterialLength/Length)
    return(math.ceil(Number/perSlat))


#Goldilocks Functions
#Contains the functions that estimate accurate stock requirements
#Will almost always be just right.

def Goldilocks(Length,Number):
    return()

"""
GUI SECTION
GUI Layout and Formating
"""

def GUI():
    
    window = tkinter.ttk.Notebook()
    f1 = tkinter.ttk.Frame(window)
    f2 = tkinter.ttk.Frame(window)   # second pane
    window.add(f1)
    window.add(f2)
    window.mainloop()
    window.tabs()

    return()

"""
C-C-C-COMBO SECTION
Functions pull together to be useful here
"""
