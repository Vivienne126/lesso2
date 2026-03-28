def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
        print("Time complexity- O(n)")
 
    j=1
    while(j<=n+1):
        print("Second Loop ",j)
        j=j*2
        print("Time complexity- O(1)")
 
    for i in range(0,100):
        print("Third loop")
        
myfunction(5)

    
