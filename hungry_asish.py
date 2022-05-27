if __name__ == "__main__":
    t = int(input())

    while(t>0):
        t-=1
        x, y, z = map(int, input().split())

        if x<y and x<z:
            print("NOTHING")
        else:
            if z>x>=y:
                print("PIZZA")
            if y>x>=z:
                print("BURGER")
            if x>=y and x>=z:
                print("PIZZA")