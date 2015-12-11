#!/usr/bin/python

D = 3000000 #3 million docs in wikipedia
N = D*100.0 #average of 100 words per doc
A = 0.1

q = 0
for i in range(1, 10000):
	num_words_occurs = (A*N)/(i*(i + 1))
	print "%d %d" % (i, num_words_occurs)
	q += num_words_occurs * (min(i, 100))
	print "total %d" % q
