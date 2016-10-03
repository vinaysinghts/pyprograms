"""        
Ex2:
input 11
find max(11) --> 27 --> [27,9,3,1]
[9+3+1] > 11 --> change
change fine max(11) --> 9 --> [9,3,1]
set --> [1,0,0]
remaining --> 11 - 9 = 2
find max(2) in [3,1] --> 3
[1] < 2 --> skip change
set --> [1,1,0]
remaining --> 2 - 3 = -1
negate [
    find max(1) in [1] --> 1
    [1] = 1
    set --> [T,T,1]
    remaining --> 1 - 1 = 0 --> finish
]
done, negation set last, hence negate final result
final result [1,1,T]
"""
import math
dec = int(input("enter a number: "))
def main():
    result = ""
    if abs(dec) == 2:
        result = "21"
    elif abs(dec) == 1:
        result = "1"
    elif abs(dec) == 0:
        result = "0"
    else:   
        #1 find max
        n,maxVal = nthPower(abs(dec),abs(dec))
        if n != None and maxVal!= None:
        #2 sum of total remaining should be less than dec
            p = n
            sumRemainP = addPower(p-1)
            if sumRemainP >= abs(dec):
                p -= 1
            #create a list of n length
            resultString = [0]*(p+1)
        #3 repeat above and set the list    
            resultStringTemp,negateBit = doTheTrick(abs(dec),n+1,resultString,0)
            if negateBit == 1:
                resultStringTemp = negate(resultStringTemp)
        else:
            print("error in finding max power!")
        result = ''.join(str(e) for e in resultStringTemp)
    #Final result format 
    if dec > 0:
        result = result.replace('2','T')
        result = result[::-1]
    elif dec < 0:
        result = result.replace('1','T')
        result = result.replace('2','1')
        result = result[::-1]
    print (result)

def doTheTrick(dec,n,resultString,negateBit):
    m,maxVal = nthPower(dec,n)
    if m != None and maxVal!= None:
        print("N:",m," maxVal:",maxVal)
        sumRemain = addPower(m-1)
        print("SumRemain",sumRemain)
        if sumRemain >= dec:
            print("sumRemain[",sumRemain,"] >= dec [",dec,"]")
            m -= 1
            m,maxVal = nthPower(dec,m)
            print("N1:",m," maxVal1:",maxVal)
            sumRemain = addPower(m-1)
            print("SumRemain1",sumRemain)
            #resultString,negateBit = doTheTrick(dec,m,resultString,negateBit)        
        resultString[m] = 1
        print("setting resultList -->",resultString)
        rem = dec - maxVal
        print("rem: ",rem)
        if rem == 0:
            return resultString,negateBit
        elif rem == 1:
            resultString[0] = 1
            print("setting resultList -->",resultString)
            return resultString,negateBit
        elif rem < 0:
            resultString = negate(resultString)
            negateBit = 1 - negateBit
            print("negated list: ",resultString," negBit:",negateBit)
        if m > 0:
            resultString,negateBit = doTheTrick(abs(rem),m-1,resultString,negateBit)
        return resultString,negateBit
    else:
        print("Woooopppsssss..")
        return resultString,negateBit

def negate(resultString):
    for i,x in enumerate(resultString):
        if x==2:
            resultString[i] = 4
        if x==1:
            resultString[i] = 3
    for i,x in enumerate(resultString):
        if x==4:
            resultString[i] = 1
        if x==3:
            resultString[i] = 2
    return resultString        
    
def addPower(n):
    if n <= -1:
        return 0
    elif n == 0:
        return 1
    else:
        return int(math.pow(3,n)) + addPower(n-1)
        
def nthPower(x,length):
    if length == 0:
        return 0,1
    elif length == 1:
        return 1,3
    elif length == -1:
        return 0,0
    else:
        for i in range(length+1):
            val = int(math.pow(3,i))
            if val >= x:
                return i,val
            if i == length:
                return i,val
            
if __name__ == "__main__":
    main()