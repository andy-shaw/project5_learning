import os
import time
import sys

def printStats(stats):
	print 'min:', min(stats)
	print 'max:', max(stats)
	print 'avg:', avg(stats)

def avg(nums):
	return sum(nums)/len(nums)

def parseStats(filename):
	f = open(filename, 'r')
	lines = f.readlines()
	f.close()

	#first line is deterministic, second in non-deterministic
	dstats = []
	for stat in lines[0].strip().split(',')[:-1]: dstats.append(int(stat))

	ndstats = []
	for stat in lines[1].strip().split(',')[:-1]: ndstats.append(int(stat))

	return dstats, ndstats

def printTimes(t1, t2):
	print '    deterministic runs:', round(t1, 3), 's'
	print 'non-deterministic runs:', round(t2, 3), 's'
	print 'total runtime:', round(t1 + t2, 3), 's'

def main(runs):

	print '\nAnalyzing Convergence rate over', runs, 'runs'
	print 'The analysis will take approximately', round(runs*.381119, 3), 'seconds'
	times = []

	#run the deterministic
	start = time.time()
	for i in range(runs):
		os.system(r"python learner.py Input_Files\places.txt Input_Files\deterministic_transitions.txt SILENT")
	finish = time.time()
	times.append(finish-start)

	if runs > 99: print "Completed with deterministic tests"

	#make newline in stats file
	f = open('stats.txt', 'a')
	f.write('\n')
	f.close()

	#run the non-deterministic
	start = time.time()
	for i in range(runs):
		os.system(r'python learner.py Input_Files\places.txt Input_Files\non-deterministic_transitions.txt SILENT')
	finish = time.time()
	times.append(finish-start)

	if runs > 99: print "Completed with non-deterministic tests"

	#parse stats for both
	dstats, ndstats = parseStats('stats.txt')

	#run analysis
	print '\nStats for deterministic'
	printStats(dstats)

	print '\nStats for non-deterministic'
	printStats(ndstats)

	print '\nTimes for the runs'
	printTimes(times[0], times[1])

	print '\nAnalysis complete'

	os.system('del stats.txt')

if __name__ == '__main__':
	args = sys.argv[1:]

	if len(args) < 1:
		print 'please specify the amount of times to run'
		exit()

	try: 
		int(args[0])
	except: 
		print 'invalid number of runs, make sure it is a number'
		exit()

	main(int(args[0]))