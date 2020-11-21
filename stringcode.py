def maxdistchar(str,n):
    count=[0]*num_of_chars
    for i in range(n):
        count[ord(str[i])]+=1
    maxdist=0
    for i in range(num_of_chars):
        if(count[i]!=0):
            maxdist+=1
    return maxdist
def smallest_substring(str):
    n=len(str)
    maxdist=maxdistchar(str):
    minl=n
    
    for i in range(n):
        for j in range(n):
            sub=str[i:j]
            sublen=len(sub)
            subdistchar = maxdistchar(sub,sublen)
    return minl
if __name__=="__main__":
l=smallest_substring(str):
print(l)
