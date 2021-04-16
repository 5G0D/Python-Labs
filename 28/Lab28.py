def print_factorization(n: int) -> None:
    if n == 1:
        print(1)
    else:
        i = 2
        d = dict()
        while n > 1:
            while n % i == 0:
                if i in d.keys():
                    d[i] += 1
                else:
                    d[i] = 1
                n /= i
            i += 1
        resStr = ''
        for k in d.keys():
            if d[k] == 1:
                resStr += str(k)    
            else:   
                resStr += str(k)+'^'+str(d[k])   
            resStr += '*' 
        print(resStr[:-1]) 

n = int(input())
print_factorization(n)
