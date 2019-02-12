# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lines = []
f = open('/Users/mravi/Desktop/C/MMDS - Sta/HW/HW1/browsing.txt', 'r')
with f as fobj:
	lines = fobj.readlines()


# Pass 1
counts = {}  #word count
for line in lines:
	# mapper 1
	for item in line.split():
		if item in counts:
			counts[item] += 1
		else:
			counts[item] = 1

new_counts = {}
for item in counts:
	c = counts[item]
	if c >= 100:
		new_counts[item] = c




pairs = {}
for line in lines:
    # mapper 2
    items = set(line.split())
    freq_items = sorted(items, key=new_counts.get)

	#freq_items = sorted(list(items & new_counts))
for i in range(len(freq_items)):
    for j in range(i + 1, len(freq_items)):
        p = (freq_items[i], freq_items[j])
        if p in pairs:
		pairs[p] += 1
        else:
           pairs[p] = 1

new_pairs = {}
for p in pairs:
	n = pairs[p]
	if n >= 100:
		new_pairs[p] = n


confidence = {}
k,l = new_pairs[0]
m = new_pairs[1]
confidence = (k,l), 1.0 * m / new_pairs[k],
(l,k), 1.0 * m / new_pairs[l]

for i in confidence:
	print (i[0][0], i)