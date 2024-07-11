ri = 0
rg = 0
rb = 0

# for colorIndex in range(3):
for i in range(256):
    Rect(i,0,20,10,fill=rgb(ri,rg,rb))
    ri += 1
ri = 0
for i in range(256):
    Rect(i,10,20,10,fill=rgb(ri,rg,rb))
    rg += 1
rg = 0
for i in range(256):
    Rect(i,20,20,10,fill=rgb(ri,rg,rb))
    rb += 1

rb = 0
# now within values
for i in range(256):
    Rect(i,30,20,10,fill=rgb(ri,rg,rb))
    ri += 1
    rg += 1
    rb += 1
ri = 0 
rg = 0
rb = 0 

for i in range(256):
    Rect(i,40,20,10,fill=rgb(ri,rg,rb))
    ri += 1
    rg += 1
    # rb += 1
ri = 0 
rg = 0
rb = 0 
for i in range(256):
    Rect(i,50,20,10,fill=rgb(ri,rg,rb))
    # ri += 1
    rg += 1
    rb += 1
ri = 0 
rg = 0
rb = 0
for i in range(256):
    Rect(i,60,20,10,fill=rgb(ri,rg,rb))
    ri += 1
    # rg += 1
    rb += 1
ri = 0 
rg = 0
rb = 0 

