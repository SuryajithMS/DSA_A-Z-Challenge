n=int(input())
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1)+" "*(n-i-1))
print()
for i in range(n,0,-1):
      print(" "*(n-i)+"*"*(2*i-1)+" "*(n-i))
print()       


"""
     *
    ***
   *****
  *******
   *****
    ***
     *
"""     
