import os

p1 = os.system('ping -qc 1 www.facebook.com >> /dev/null')
p2 = os.system('ping -qc 1 www.facebook.corp>> /dev/null')
p3 = os.system('ping -qc 1 www.tevapharm.com >> /dev/null')
p4 = os.system('ping -qc 1 www.fasñ2.as1 >> /dev/null')
print(p1)
print(p2)
print(p3)
print(p4)

