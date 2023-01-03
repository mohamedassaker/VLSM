result = []

def binary(prefix):
    binary_list = []
    print_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    c = 1
    for i in range(4):
        binary_list.append([])
        for j in range(8):
            if(c <= prefix):
                binary_list[i].append(1)
                c+=1
            else:
                binary_list[i].append(0)
    c = 1
    for k in range(32):
        if(c <= prefix):
            print_list[k] = 1
            c+=1

    # print("prefix binary:", *print_list, sep=" ")
    binToDec(binary_list)


def binToDec(binary_list):
    n = 0
    for j in range(len(binary_list)+4):
        if binary_list[0][j] == 1:
            n += pow(2, 7-j)
    result.append(n)

    n = 0
    for j in range(len(binary_list)+4):
        if binary_list[1][j] == 1:
            n += pow(2, 7-j)
    result.append(n)

    n = 0
    for j in range(len(binary_list)+4):
        if binary_list[2][j] == 1:
            n += pow(2, 7-j)
    result.append(n)

    n = 0
    for j in range(len(binary_list)+4):
        if binary_list[3][j] == 1:
            n += pow(2, 7-j)
    result.append(n)

    print("Subnet mask: ", end="")
    print(*result, sep=".")

def calculate(host, IPinitial, prefix):
    IP = [8192,4096,2048,1024,512,256,128,64,32,16,8,4,2]
    hm = []
    exp = []
    num_list = []
    c = 0
    for i in range(len(host)):
        for j in range(len(IP)):
            if IP[j] > host[i]:
                x = pow(2, 13 - j) - 2
                e = 13-j
        hm.append(x)
        exp.append(e)

    for i in range(len(exp)):
        result.clear()
        ceros = 32-prefix 
        print(f"For {host[i]} hosts {exp[i]} bits are needed")
        print(f"Max hosts: (2^{exp[i]}) - 2 [initial & broadcast addresses] = ", hm[i])
        print("Home address: ", end ="")
        IPinitial[3] = int(IPinitial[3]) + int(c)
        if IPinitial[3] == 256:
            num_list = IPinitial[:]
            num_list[2] = int(num_list[2]) + int(1)
            num_list[3] = 0
            print(*num_list, sep =".")
        else:
            print(*IPinitial, sep =".")
        t = ceros-exp[i]+prefix
        
        print(f"Mask prefix: {ceros} - {exp[i]} + {prefix} = {t} ")
        binary(t)
        print("Valid address range: ", end ="")
        IPinitial[3] = int(IPinitial[3]) + int(1)
        if IPinitial[3] > 255:
            IPinitial[3] = 1
            IPinitial[2] = int(IPinitial[2]) + int(1)
            print(*IPinitial, sep =".", end="")
        elif IPinitial[3] < 256:
            print(*IPinitial, sep =".", end="")
    
        IPinitial[3] = int(IPinitial[3]) + int(hm[i]) - int(1)    
          
        if IPinitial[3] > 254:
            IPinitial[3] = 254
            print(" - ", end="")
            if result[3] > 0:
                IPinitial[3] = int(255) - int(result[3])
                print(*IPinitial, sep =".")
            elif result[3] == 0 and result[2] > 0:
                IPinitial[2] = int(IPinitial[2]) + (int(255) - int(result[2]))
                print(*IPinitial, sep =".")

        elif IPinitial[3] <= 254:                
            print(" - ", end="")  
            print(*IPinitial, sep =".")
        print(f"Network broadcast: ", end="")
        IPinitial[3] = int(IPinitial[3]) + int(1)
        print(*IPinitial, sep =".")
        if c==0:
            c = int(c) + int(1)
        print('\n')

IPinitial = []
host = []
print("Enter IP initial")
for i in range(4):
    correct = False
    while(not correct):
        try:
            initial = (input(f"Enter octet {i+1}: "))
            if (int(initial) >= 0):
                correct = True
                IPinitial.append(initial)
            else:
                print("\nEnter a correct value. Try again\n")
        except (RuntimeError, TypeError, NameError, IndexError, ValueError):
            print("\nEnter a correct value. Try again\n")
            
correct = False
while(not correct):
    try:
        prefix = int(input("Enter mask: "))
        if prefix > 0:
            correct = True
        else:
            print("\nEnter a correct value. Try again\n")
    except (RuntimeError, TypeError, NameError, IndexError, ValueError):
        print("\nEnter a correct value. Try again\n")        
print("IP obtained:")
print(".".join(IPinitial),"/",prefix)
binary(prefix)
print('\n')

correct = False
while(not correct):
    try:
        j = int(input("Number of Subnets: "))
        if j > 0:
            correct = True
        else:
            print("\nEnter a correct value. Try again\n")
    except (RuntimeError, TypeError, NameError, IndexError, ValueError):
        print("\nEnter a correct value. Try again\n")

for i in range(j):
    correct = False
    while(not correct):
        try:
            h = int(input(f"Number of hosts in Subnet {i+1}: "))
            if h >= 0:
                correct = True
                host.append(h)
            else:
                print("\nEnter a correct value. Try again\n")
        except (RuntimeError, TypeError, NameError, IndexError, ValueError):
            print("\nEnter a correct value. Try again\n")                

host.sort(reverse=True)
print("Sort number of hosts from largest to smallest:")
print(host)
result.clear()
calculate(host, IPinitial, prefix)