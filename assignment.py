lower = 2
upper = 200  
  
def isprime(a):
    isp = True;
    for i in range(2,a//2):
        if a% i == 0:
           isp  = False
           break
    return isp  

for num in range(lower,upper + 1): 
   res = isprime(num)
   if(res == True):
       print(num,end=",")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! programe 2

altitude = int(input("Enter the altitude: "));
if(altitude <= 1000):
    print("You are safe for landing")
elif(altitude <= 5000):
    print("clam down to 1000")
else:
    print("Turn Around")