"""Q.3 Draw this Pattern 👇

    *
   * * 
  * * *
 * * * *
* * * * * 
"""
num=int(input("Enter number of rows of star pattern: "))
for i in range(1,num+1):
    print(" "*(num-i)+" *"*i)
