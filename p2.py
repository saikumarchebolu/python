radius=float(input("enter the radius of a circle :"))
if (radius<=1000 and radius>0):
    r=3.14*radius*radius
    print("area of the circle for given radius {radius} is :",r)
else :
    print("enter the radius value between 0 and 1000")