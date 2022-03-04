def calculateAndAssign(x,y):
  return 
def Karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    var1, var2, var3, var4, var5 = calculateAndAssign(x, y)
    ad_plus_bc = Karatsuba(var1, var2) - var3 - var4
    return (10 ** (2*var5))*var3 + (10 ** var5)*ad_plus_bc + var4

x=int(input())
y=int(input())
print(Karatsuba(x,y))