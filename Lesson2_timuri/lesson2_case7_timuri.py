string1 = 'wtf'
string2 = 'mon uybbjo cxgujjs whjk tcx afdp'

a = string2.find(string1[0])
b = string2.find(string1[1])
c = string2.find(string1[2])

print(string2[min(a, b, c):max(a, b, c) + 1])
