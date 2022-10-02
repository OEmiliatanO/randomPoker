from pic import *
import time
import random
import os

def goup():
	print("\033[F", end = '')

def move(i,j):
	print("\033[%d;%dH" % (i, j), end = '')

def clear():
	os.system("clear")

suit = [Clovers, Diamond, Heart, Pikes]
number = [A, two, three, four, five, six, seven, eight, nine, ten, J, Q, K]

decker = []
for s in suit:
	for n in number:
		decker.append((s, n))

def print3poker(poker1, poker2, poker3):
	su = [poker1[0][1:], poker2[0][1:], poker3[0][1:]]
	nu = [poker1[1][1:], poker2[1][1:], poker3[1][1:]]
	h = 25
	suw = [0,0,0]
	nuw = [0,0,0]
	for i in range(len(su)):
		for j in range(len(su[i])):
			suw[i] += 1
			if su[i][j] == '\n': break
	for i in range(len(nu)):
		for j in range(len(nu[i])):
			nuw[i] += 1
			if nu[i][j] == '\n': break
	for i in range(h):
		for j in range(len(su)):
			print(su[j][i*suw[j]:(i+1)*suw[j]-1] + nu[j][i*nuw[j]:(i+1)*nuw[j]-1],end = '____|____')
		print("")
	return sum(suw) + sum(nuw) + 9*2
	
def print3pokerwithnoisy(poker1, poker2, poker3, p = 1):
	move(0, 0)
	h, w = 25, print3poker(poker1, poker2, poker3)
	move(0, 0)
	for i in range(h):
		for j in range(w):
			if random.uniform(0, 1) <= p:
				print(random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '/']), end = '')
			else:
				move(i, j)
		print("")

def main():
	while True:
		clear()
		t1 = time.time()
		while True:
			t2 = time.time()
			print3pokerwithnoisy(random.choice(decker), random.choice(decker), random.choice(decker), 1 - (t2 - t1) / 6)
			time.sleep(0.05)
			if t2 - t1 > 6: break
		move(35, 0)
		ch = input("contine? [y/n]: ")
		if ch.lower() == 'y':
			continue
		else:
			clear()
			break

if __name__ == "__main__":
	main()
