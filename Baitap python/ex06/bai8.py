from operator import itemgetter
n=int(input())
list=[tuple([x for x in input().split(',')]) for i in range(n)]
print(sorted(list,key=itemgetter(0,1,2)))