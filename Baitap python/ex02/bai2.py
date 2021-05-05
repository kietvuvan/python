a,b=map(int,input().split())
import math
# ucll
print(math.gcd((a),(b)))
#bcnn
print(int(a*b/math.gcd(int(a),int(b))))
# toi gian
print(str(int(a/math.gcd(a,b)))+'/'+str(int(b/math.gcd(a,b))))
