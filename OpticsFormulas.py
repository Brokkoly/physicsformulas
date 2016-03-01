import numpy as np
from math import sin
from math import cos
from math import asin
#R = reflectance, the ratio (outgoing energy/time)/(incoming energy/time in reflected beam)
def snellsLaw(ni,nt,thetai):
	return asin(ni*sin(thetai)/nt)
def degToRad(x):
	return x*np.pi/180
def radToDeg(x):
	return x*180/np.pi
def rParallel(ni,nt,thetai):
	thetat = snellsLaw(ni,nt,thetai)
	retval = (nt*cos(thetai) -ni*cos(thetat))/(ni*cos(thetat)+nt*cos(thetai))
	return retval
def rPerpendicular(ni,nt,thetai):
	thetat = snellsLaw(ni,nt,thetai)
	retval = (ni*cos(thetai)-nt*cos(thetat))/(ni*cos(thetat)+nt*cos(thetai))
	return retval
def tParallel(ni,nt,thetai):
	thetat = snellsLaw(ni,nt,thetai)
	retval = (2*ni*cos(thetai))/(ni*cos(thetat)+nt*cos(thetai))
	return retval

