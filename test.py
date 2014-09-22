#!/usr/bin/psh

ls = `ls`

print "Number of files: %d" % len(ls.split())

ls = `ls -lrS`

largest = ls.split('\n')[-1] # last line in 'ls -lrS'

columns = largest.split()
 
print "Largest file: %s (%s bytes)" % (columns[8], columns[4])

