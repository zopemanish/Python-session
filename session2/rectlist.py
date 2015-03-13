rect1 = {'len':10,'width':15}
rect2 = {'len':5,'width':15}
rect3 = {'len':10,'width':25}
rect4 = {'len':11,'width':17}
rect5 = {'len':12,'width':22}

rectlist = [rect1,rect2,rect3,rect4,rect5]

reslist = []
for rectN in rectlist:
	reslist.append(rectN['len']*rectN['width'])

print 'Before list'
print reslist
reslist.sort()
print reslist
