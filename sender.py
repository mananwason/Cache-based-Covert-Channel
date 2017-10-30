import os
import time
import random
import math
import mmap
import binascii

pth = os.path.dirname(os.path.abspath(__file__))

fp = open(pth + "sender.txt", 'r+')

fmap = mmap.mmap(f.fileno(), 0)

def convertToBinary(s):
	return bin(int(binascii.hexlify(s),16)).replace("b","")

def send():

	fileSize = 635756000


	t1 = time.time()

	for i in range (0, 6):

		x = random.randint(0, int((2.0/7)*fileSize))
		y = random.randint(int((5.0/7)*fileSize), fileSize)

		fmap[x:y]

	t2 = time.time()

	print round(t2-t1, 3)


sendingBits = raw_input("\nEnter the string to transfer: ")
#sendingBits = convertToBinary(inpSt)
#print "binary version of the string " + sendingBits
bits = list("1"+sendingBits+"1")

tm = 0

for i in range(0, len(bits)):

	if bits[i] == '1':

		tm = tm + 1

	elif bits[i] == '0':

		tm = tm + 2

for i in range(0,len(bits)):
	if bits[i] == '1':
		send()
	elif bits[i] == '0':
		time.sleep(4.5)
		print "Sent 0"