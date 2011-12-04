#!/usr/bin/python2.7
import optparse
from collections import defaultdict
from copy import deepcopy
	
def trace(stTrakov, trenutniOpisi):
	beseda = ''
	for stanje, trakovi, index in trenutniOpisi: 
		beseda += stanje+' -\t'
		for i in range(stTrakov):
			tr = trakovi[i][:]
			tr.insert(index[i]+1,']')
			tr.insert(index[i],'[')
			beseda += ''.join(tr) + '\t\t'
		beseda += '\n'
	return beseda

def run(fileName, beseda, printTrace, clearBlanks, printResult):
	a, delta = open(fileName), defaultdict(list)
	a.readline()
	a.readline()
	stTrakov = len(a.readline().split('-')[0].split())-1 # tko sm mislu
	a.seek(0)
	stanje, final= a.readline().split()[1],a.readline().split()[1:]
	[delta[tuple(i.split()[:stTrakov+1])].append(i.split()[stTrakov+2:]) for i in a]

	trakovi = [list(beseda)] #trakovi 1
	for i in range(stTrakov-1):
		trakovi.append(['B']) #trakovi i
	index = [0 for i in range(stTrakov)]
	premik = ['S' for i in range(stTrakov)]	

	trenutniOpisi = [(stanje, trakovi, index)]	
	while(trenutniOpisi!=[]):
		if printTrace:
			print trace(stTrakov, trenutniOpisi)
		noviOpisi = []
		for stanje, trakovi, index in trenutniOpisi:
			t = [stanje]
			for i in range(stTrakov):
				t.append(trakovi[i][index[i]])
			for moznostDelta in delta[tuple(t)]:
				novoStanje = moznostDelta[0]
				novoTrakovi = deepcopy(trakovi)
				novoIndex = deepcopy(index)
				for i in range(stTrakov):
					novoTrakovi[i][novoIndex[i]] = moznostDelta[i+1]
					premik[i] = moznostDelta[i+1+stTrakov]
					
				for i in range(stTrakov):
					if clearBlanks:
						j = len(novoTrakovi[i])-1
						while j > 3 and novoTrakovi[i][j] == 'B' and j > novoIndex[i]: 
							j -= 1
						j = 0 if j<2 else j-1
						k = 0
						while k < novoIndex[i]-2 and novoTrakovi[i][k] == 'B':
							k += 1
						novoTrakovi[i] = novoTrakovi[i][k:j+3]
						novoIndex[i] -= k

					if novoIndex[i] == 0:
						novoTrakovi[i].insert(0, 'B')
						novoIndex[i] += 1
					if novoIndex[i] == len(novoTrakovi[i])-1:
						novoTrakovi[i].append('B')

					if premik[i] == 'L':
						novoIndex[i] -= 1
					if premik[i] == 'R':
						novoIndex[i] += 1
				noviOpisi.append((novoStanje, novoTrakovi, novoIndex))
				if any(i in novoStanje for i in final):
					if printTrace:
						print trace(stTrakov, noviOpisi)
					if printResult:
						print '\n\nRezultat na traku 1 : '+''.join(novoTrakovi[0])+'\n'
					return True
		trenutniOpisi = noviOpisi
	return False

parser = optparse.OptionParser("usage: %prog [options] word1 word2")
parser.add_option("-t", "--trace", dest="t", action="store_true", default=False, help="Set for trace turing machine")
parser.add_option("-r", "--result", dest="r", action="store_true", default=False, help="Print the output from the first track")
parser.add_option("-b", "--clearBlanks", dest="b", action="store_true", default=False, help="Clear unused blanks from tracks")
parser.add_option("-f", "--fileName", dest="f", default="avtomat.txt", type="string", help="Filename for turing machine")
(options, args) = parser.parse_args()
if len(args) < 1:
	parser.print_help()
for beseda in args:
	if run(options.f, beseda, options.t, options.b, options.r):
		#print "Beseda '%s' je v jeziku" % beseda
		print "Beseda je v jeziku" 
		print
	else:
		#print "Besede '%s' ni v jeziku" % beseda
		print "Besede ni v jeziku"
		print
