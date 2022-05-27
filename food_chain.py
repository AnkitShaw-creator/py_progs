
if __name__ == "__main__":
    t = int(input())
    
    while(t>0):
        e, k = map(int, input().split())
        #print(k+e)
        i=1
        while(e>=k):
            e = e//k
            i += 1

        t -= 1
        print(i)