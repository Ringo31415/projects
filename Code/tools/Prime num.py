Find_prime_S=[]
Find_prime_var=int(input("bigger than one"))
for Find_prime_num in range(2,Find_prime_var + 1):
        for Find_prime_i in range(2,Find_prime_num):
            if (Find_prime_num%Find_prime_i)==0:  
                break
        else:
            Find_prime_S.append(Find_prime_num)


