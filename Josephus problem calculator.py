def findTheWinner(n, k):
    n = list(range(1,n+1))
    print(josephus(n, k))
        
def josephus(ls, skip):
    skip -= 1 
    index= skip
    while len(ls) > 1:
        ls.pop(index)
        idx = (index + skip) % len(ls)
    return ls[0]

findTheWinner(10, 3)
