def interchange1with2(n):
    n=str(n)
    n=n.replace('1','.')
    n=n.replace('2','1')
    n=n.replace('.','2')
    return n
inp=int(input("inter chain 1 with 2:"))
print(interchange1with2(inp))
      
