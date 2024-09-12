import math
def getcylindervolume(radius,height):
    volume = math.pi*(radius**2)*height
    return volume
x = getcylindervolume(10,12)
y = getcylindervolume(2, 6)
print (round(x,4))
print (round(y,4))
print (int(x))
print (int(y))

def getnumberofslices(radius, height, volumeofslice):
        volume = getcylindervolume(radius,height)
        numberofslices = volume/volumeofslice
        return int(numberofslices)
numberofslice1 = getnumberofslices(10, 10, 100)
print(numberofslice1)