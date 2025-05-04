#program to convert celcius into ferenheight
def f_to_c(f):
    return 5*(f-32)/9
f=int(input("Enter temperature in ferenheight: "))
c=f_to_c(f)
print(f"The Temperature in celciust is {round(c,2)}.")