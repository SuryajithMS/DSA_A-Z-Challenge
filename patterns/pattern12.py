def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    num=65
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j),end=" ")
            num+=1
        print()    


"""
A
A B 
A B C 
A B C D
"""
