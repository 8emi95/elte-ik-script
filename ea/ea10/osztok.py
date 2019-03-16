
def osztoi(x):
    osztok=[1,x]
    temp=[]
    for i in range(2,(x/2)+1) :
        if x % i == 0 :
            temp += [i]
    osztok[1:1] = temp
    return osztok

if __name__ == "__main__":    
     print osztoi(52)
