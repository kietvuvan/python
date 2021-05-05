
n=int(input())
arr=list(map(int,input().split()))[:n]

print(all(x*y<0 for x,y in zip(arr,arr[1:]))) # checking <0 or >0
print(all(x<y for x,y in zip(arr,arr[1:]))) # list increase
print(all(y/x==arr[1]/arr[0] for x,y in zip(arr,arr[1:]))) # cap so nhan
print(all(y-x==arr[1]-arr[0] for x,y in zip(arr,arr[1:]))) # cap so cong

print(list(y/x for x,y in zip(arr,arr[1:])))
print(list(y-x for x,y in zip(arr,arr[1:])))

