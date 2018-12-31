from math import sqrt
from itertools import islice,count
import numpy

def isPrime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w


    # for i in range(2, int(sqrt(n))+1):
    #     if n%i==0:
    #         return False
    return True

def getPrimes():
    """
    this method yields infinite prime numbers starting from 2
    you will need to use any logic to get how many u want
    Tip: use islice from itertools
    """

    yield 2
    num=3
    while 1:
        if isPrime(num):
            yield num
        num+=2


def isPalindrome(num):
    if str(num)==str(num)[::-1]:
        return True
    return False

def getFactors(num):
    factorlist = []
    for x in range(1, (num)+1):
        if num%x==0:
            factorlist.append(x)
    return factorlist


def primeFactors(num):
    factorlist = []
    for x in range(1, int(sqrt(num)+1)):
        if num%x==0 and isPrime(x)==True:
            factorlist.append(x)

    return factorlist

# problem 4
def largestPalindromeProduct(digitcount):
    palindromelist = []
    lb = int("1"+"0"*(digitcount-1))
    ub = int("1"+"0"*(digitcount))
    for i in range(lb, ub):
        for j in range(lb, ub):
            val = i*j
            if isPalindrome(val):
                palindromelist.append(val)
    return max(palindromelist)



# problem 5
def smallestMultiple(lb, ub):
    dividors = [x for x in range(lb, ub+1)]

    # we need product of all numbers between lb and ub, not factorial of ub

    product = 1
    for d in dividors:
        product*=d

    for num in range(ub, product+1):
        flag=0
        for x in dividors:
            if num%x!=0:
                flag=1
                break
        if flag==0:
            return num

#problem 6
def squaresum(lb, ub):
    sumsquares = 0
    for n in range(lb, ub+1):
        sumsquares += n * n

    squaresum = sum([x for x in range(lb, ub+1)]) ** 2

    return (squaresum - sumsquares)

#problem 7
def getFirstNPrimes(count):
    """
    This method accepts the count param as how many first prime numbers
    you want.
    """
    primes = islice((x for x in getPrimes()), count)
    return primes


#problem 9
def specialPythagoreanTriplet(sum):
    triplets = []
    for x in range(1, 1000):
        for y in range(x+1, 1000):
            for z in range(y+1, 1000):
                if x+y+z==sum:
                    triplets.append([x,y,z])
    return triplets

def testPythogras(triplet):
    """"
    :param triplets: here triplets is a list where at
    0th index is a
    1st index is b
    2nd index is c
    :return: this will return only  true of false based on whether it satifies the pythogorean property
    """

    if ( triplet[0]**2 + triplet[1]**2) == (triplet[2]**2):
        return True
    return False

def breakIntoChunks(iterable, chunklength):
    if chunklength>=len(iterable) or chunklength<=0:
        return iterable

    n = chunklength
    chunks = [iterable[i * n:i * n + n] for i in range(0, len(iterable) // n)]
    return chunks

# problem 10
def adjacentChunks(iterable, cl):
    if cl>=len(iterable) or cl<=0:
        return iterable

    n = cl
    return [iterable[i:i + n] for i in range(0, len(iterable) - (n - 1))]

#problem 13
def largeSum(num):
    """
    :param num: num should be supplied in string format
    :return: will return the sum in string format
    """
    nums = [int(num[i * 50:i * 50 + 50]) for i in range(0, 100)]

    return str(sum(nums))

def getNumberOfFactors(num, primes):
    #first get the first prime numbers upto the sqrt of the num
    primes =  primes[:int(sqrt(num))+1]
    # return primes
    countlist = [0 for _ in range(len(primes)+1)]
    i=0
    while i<len(primes):
        if num%primes[i]!=0:
            i+=1
            continue
        if num//primes[i]==0:
            break
        else:
            countlist[primes.index(primes[i])]+=1
            num = num//primes[i]
    count=1
    for f in countlist:
        if f==0:
            continue
        count*=f+1
    return count

def longestCollatzSequence(start, end):
    n = start
    x = n
    length = []
    while n < end:
        chain = 1
        while x != 1:
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3 * x + 1
            chain += 1
        length.append(chain)
        n += 1
        x = n

    # 0 index represent the start no
    return start+length.index(max(length))

def getAmicablePairs(lb, ub):
    num = lb
    amicables = []
    while num < ub:
        factors = getFactors(num)
        s = sum(factors[:-1])
        fac = getFactors(s)
        if sum(fac[:-1]) == num and s != num and [s, num] not in amicables:
            amicables.append([num, s])
        num += 1
    return amicables

def getScoreOfNamesInFile(filename, mode):
    file = open(filename, mode)
    names = [name.strip("\"") for name in str(file.read()).split(',')]
    names.sort()
    lettercost = [x for x in range(1, 27)]
    alphabets = [chr(x) for x in range(65, 91)]
    # print(lettercost)
    # print(alphabets)

    score=0
    for name in names:
        sum=0
        for char in list(name):
            sum+=lettercost[alphabets.index(str(char))]
        score+=(sum*(names.index(name)+1))

    # print(score)
    return score


def getFibonacciNumbers(includeZero):
    if includeZero:
        a,b=0,1
    else:
        a,b=1,1

    while 1:
        yield a
        a,b = b, a+b

if __name__ == "__main__":
    combos = []

    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    combos.append([a,b,c,d])
    del combos[0]
    del combos[0]
    del combos[combos.index([1,1,1,1])]
    del combos[combos.index([1,0,0,0])]
    del combos[combos.index([2,0,0,0])]
    del combos[combos.index([3,0,0,0])]
    del combos[combos.index([4,0,0,0])]
    del combos[combos.index([5,0,0,0])]
    del combos[combos.index([6,0,0,0])]
    del combos[combos.index([7,0,0,0])]
    del combos[combos.index([8,0,0,0])]
    del combos[combos.index([9,0,0,0])]
    # print(combos)

    for combo in combos:
        if int("".join([str(c) for c in combo])) == int(sum([c**5 for c in combo])):
            print(combo)


    # problem 25
    # fibos = (x for x in getFibonacciNumbers(False))
    # i=1
    # f = next(fibos)
    # while len(str(f))!=1000:
    #     f = next(fibos)
    #     i+=1
    #     print(i, f)


    # problem 22
    # print(getScoreOfNamesInFile("p022_names.txt", "r"))

    # problem 21
    # amicables = getAmicablePairs(1, 10000)
    # nums = []
    # for pair in amicables:
    #     nums.append(pair[0])
    #     nums.append(pair[1])
    # print(amicables)
    # print(nums)
    # print(sum(nums))





    # print(longestCollatzSequence(13, 1000000))

    # problem 12
    # primes  = [x for x in range(2, 1000) if isPrime(x)]
    # n=1
    # while 1:
    #     triangular = n*(n+1)//2
    #     factorcount = getNumberOfFactors(triangular, primes)
    #     if factorcount>500:
    #         print("Triangular number = ", triangular)
    #         break
    #     n+=1

    # problem 11

    # m = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 "
    # m += "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 "
    # m += "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 "
    # m += "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 "
    # m += "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 "
    # m += "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 "
    # m += "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 "
    # m += "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 "
    # m += "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 "
    # m += "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 "
    # m += "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 "
    # m += "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 "
    # m += "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 "
    # m += "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 "
    # m += "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 "
    # m += "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 "
    # m += "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 "
    # m += "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 "
    # m += "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 "
    # m += "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
    #
    # numberlist = [int(num) for num in m.split()]
    #
    #
    # twoDimAdjacent = []
    #
    # i=0
    # while i<=len(numberlist)-4:
    #     # for horizontally adjacent
    #     twoDimAdjacent.append(numberlist[i:i+4])
    #
    #     # for vertically adjacent
    #     if i<=339:
    #         twoDimAdjacent.append([numberlist[j] for j in [x for x in range(i, (i+20)*4, 20)][:4]])
    #
    #     # for diagonally adjacent
    #
    #
    #     i+=1
    #
    # for quad in twoDimAdjacent:
    #     print(quad)

    ###############################################

    # num = "37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231965867550793241933316490635246274190492910143244581382266334794475817892575867718337217661963751590579239728245598838407582035653253593990084026335689488301894586282278288018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558297169388870771546649911559348760353292171497005693854370070576826684624621495650076471787294438377604532826541087568284431911906346940378552177792951453612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683061932846081119106155694051268969251934325451728388641918047049293215058642563049483624672216484350762017279180399446930047329563406911573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871720121925776695478182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275889028025717332296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585629946580636237993140746255962240744869082311749777923654662572469233228109171419143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470230530811728164304876237919698424872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225512486764533677201869716985443124195724099139590089523100588229554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236377742425354112916842768655389262050249103265729672370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957014548792889848568277260777137214037988797153829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539409579530664052326325380441000596549391598795936352974615218550237130764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886755061649651847751807381688378610915273579297013376217784275219262340194239963916804498399317331273132924185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818971426179103425986472045168939894221798260880768528778364618279934631376775430780936333301898264209010848802521674670883215120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411606618262936828367647447792391803351109890697907148578694408955299065364044742557608365997664579509666024396409905389607120198219976047599490197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791786391670211874924319957006419179697775990283006991536871371193661495281130587638027841075444973307840789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690"
    # print(largeSum(num)[:10])

    # number = str("7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450")
    # number  = [int(x) for x in number]
    # products = [numpy.prod(q) for q in adjacentChunks(number, 13)]
    # print(max(products))



    # primes = [x for x in islice((x for x in getPrimes()), 150000) if x<2000000]
    # print(sum(primes))

    # for triplet in specialPythagoreanTriplet(1000):
    #     if testPythogras(triplet):
    #         print(triplet)
    #         break

