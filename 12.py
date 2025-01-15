s='2'*36
while ('2222' in s) or ('333' in s):
    if ('2222' in s):
        s=s.replace ('2222','',1)
        s=s + '3'
    else:
        s=s.replace ('333','',1)
        s = s + '2'
print(s)