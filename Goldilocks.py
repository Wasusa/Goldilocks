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
"""Determines the lead in/Lead out for a given panel where no specific value
for either is given. Automatically gives the balanced value"""
def LILOcalc(Height,Slats,Slat,Spacing):
    val = (Height - (Slats*Slat) -((Slats-1)*Spacing))/2
    return val

"""Determines the Lead out where the lead in is given""""
def SpecifiedLIcalc(Height,Slats,Slat,Spacing,LI):
    val = (Height - (Slats*Slat) -((Slats-1)*Spacing))-LI
    return val

"""Determines how many slats can fit into a given panel"""
def NumSlatcalc(Height,Slat,Spacing):
    return math.floor(Height/(Slat+Spacing))

"""Returns the required cut size of the slat given the material it is being
placed into"""
def SlatSizecalc(Length,material):
    return(Length-((material*2)-30))

"""Essentially a tolerance check: Does the panel as specified meet our
standard styling requirements?""""
def Acceptable(Spacing,LILOorLO):
    if (LILOorLO <= Spacing and LILOorLO >=MinLilo):
        Result = True
    else:
        Result = False
    return(Result)

"""Provides two options for changes to a panels height should the original not
meet standard styling requirements"""
def ReqChange(Height,LILOorLO,Spacing,Slat):
    newHeightlower = Height-(LILOorLO-MinLILO)
    newHeightupper = Height-LILOorLO+Spacing+Slat+MinLILO
    
    return(newHeightupper, newHeightlower)

"""I expect to feed in lists containing height, width, and how many of that
type of panel exist. If these lists aren't the same size, the solution
method won't work. This checks that the lists are of equal length"""
def ListCheck(List1,List2,List3):
    if len(List1)==len(List2)==len(List3):
        passed = True
    else:
        passed = False
    return(passed)

#Underestimator Functions
#Contains stock requirement estimator using Lineal Metres.
#Will almost always underestimate required stock

"""Straight sums required length of material"""
def LinealEstimate(Length,Number):
    return math.ceil((Length*Number)/MaterialLength)

#Overestimator Functions
#Contains stock requirement estimator using conservative methods
#Will almost always overestimate required stock

"""Determines the amount of material required given only so many peices can be
cut from the original length, and that there will be some waste"""
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


    return()

"""
C-C-C-COMBO SECTION
Functions pull together to be useful here
"""
