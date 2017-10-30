import os
import time
import random
import math
import mmap

pth = os.path.dirname(os.path.abspath(__file__))

fp = open(pth + "/lolita.txt", 'r+')
fmap = mmap.mmap(fp.fileno(), 0)

fileSize = 1043069100

fileReadStart = int(math.floor((1.5/7)*fileSize))
fileReadEnd = int(math.floor((4.5/7)*fileSize))

oneThreshold = 6.0
zeroThreshold = 2.2
timeThreshold = 2.8

n = input("\nEnter for how many bits you want the receiver to read: ")
n = (n+2)*7
print "\n"

def BinaryToString(s):
	return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(0,len(s)//8))

def getTimes(n):

	times = list()
	for i in range(0, n):

		t1 = time.time()
		fmap[fileReadStart:fileReadEnd]
		t2 = time.time()

		times.append(round(t2-t1, 3))

		print round(t2-t1, 3)

	return(times)

def getResult(tmp):

	prev = -1
	flag = 1
	ans = ""
	longerTime = 0

	st = list()

	oneStart = 0
	while oneStart < len(tmp):

		count = 0
		oneEnd = oneStart
		while round(tmp[oneEnd], 1) > timeThreshold:
			if (oneEnd + 1) == len(tmp):
				break

			else:
				oneEnd += 1

			count = count + 1

		if count >= 4:

			if prev != -1:
				for k in range(0, int(round((oneStart - prev)/zeroThreshold))):
					ans = ans + str(flag)
				flag = 1
				
				for k in range(0,int(round((oneEnd - oneStart)/oneThreshold))):
					ans = ans + str(flag)
				flag = 0
				prev = oneEnd

			else:
				for k in range(0, int(round((oneEnd - oneStart)/oneThreshold))):
					ans = ans + str(flag)
				flag = 0
				prev = oneEnd

			st.append(oneStart)
			st.append(oneEnd)
			oneStart = oneEnd

		else:
			oneStart += 1

	ans = ans [1:-1]
	#for x in st:
	#	print x

	f = open("results.txt", 'a')
	f.write("-----------------------------\n")
	f.write(ans+"\n")
	for x in tmp:
		f.write(str(x)+"\n")
	for y in st:
		f.write(str(y)+"\n")
	f.close()
	return ans
 
timeList = getTimes(n)
print "\n"
answer = getResult(timeList)
print "\n"
print "The information transmitted by sender is: ", answer
st = BinaryToString(answer)
#print st
print "\n"
