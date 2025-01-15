def check_num(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(245660, 245690+1):
    k=0
    s=[]
    for y in range(2, i//2+1):
        if i%y==0:
            k+=1
            s.append(y)
            if k>2:
                break
    if k==2 and check_num(s[0]) and check_num(s[1]):
        print(*s)