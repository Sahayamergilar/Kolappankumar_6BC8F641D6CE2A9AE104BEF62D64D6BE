def Leapyear(year):
  if (year / 4== 0 and year / 100 != 0):
    return True
  elif year / 400 == 0:
    return True
  else:
    return False

year= int(input('Enter a year:'))
res= Leapyear(year)
if True:
  print("this year is Leapyear")
else:
  Print(" this year is not a Leapyear")
    
    