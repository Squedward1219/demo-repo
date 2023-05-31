# Problem 1
def factors(x) :
    n = 1
    fact = []
    print("These are the factors of " + str(x) + ":")
    while n <= x :
        if x % n == 0 :
            fact.append(n)
        n += 1
    print(fact)

# Problem 2

def fahr(c) :
    d = c * 1.8 + 32
    return d

def tempConv() :
    num = 1
    id_list = [13, 2, 5, 14, 12, 1]
    temperatures = [75, 23, 78, 22, 24, 69]
    while num < len(id_list) :
        if id_list[num] % 2 == 0 :
            temperatures[num] = fahr(temperatures[num])
        num += 1
    print(temperatures)

def main() :
    factors(88)
    tempConv()



main()
