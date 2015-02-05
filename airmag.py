import numpy as np
import matplotlib.pyplot as plt
with open("phot_out", "r") as data:
    alls = []
    for line in data:
        col = line.split()
        alls.append(col)

mags = alls[79::10] # Replace the 10 with the number of comparison stars times 5
mag = []
for item in mags:
    mag.append(item[4])

airs = alls[78::10] # Replace 10 with the number of comparison stars times 5
air = []
for item in airs:
    air.append(item[1])

errs = alls[79::10] # Do the thing!
err = []
for item in errs:
    err.append(item[5])

am = dict(zip(air, mag))
ae = dict(zip(air, err))
ma = dict(zip(mag, air))
me = dict(zip(mag, err))
em = dict(zip(err, mag))
ea = dict(zip(err, air))

x = []
y = []
q = []
for item in air:
    if am[item] != 'INDEF' and ae[item] != 'INDEF' and item != 'INDEF':
        x.append(item)
for item in mag:
    if item != 'INDEF' and ma[item] != 'INDEF' and me[item] != 'INDEF':
        y.append(item)
for item in err:
    if em[item] != 'INDEF' and item != 'INDEF' and ea[item] != 'INDEF':
        q.append(item)
        
x = [float(item) for item in x]
y = [float(item) for item in y]
q = [float(item) for item in q]



p = np.polyfit(x, y, 1)
print p
plt.show()
plt.xlabel('Airmass')
plt.ylabel('Instrumental Magnitude')
plt.title('Magnitude vs Airmass')
#plt.plot(x, y, 'bo')
plt.errorbar(x, y, yerr=q, fmt='o')
plt.plot(x,np.polyval(p,x),'r-')
plt.show()
