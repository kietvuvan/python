import statistics as s
r=list(map(float,input().split(',')))
print(r)
print(s.mean(r))
mean_of_list=s.mean(r)
sigma=0.0
for i in range(len(r)):
    sigma=sigma+((r[i]-mean_of_list)**2)

print(sigma/len(r))