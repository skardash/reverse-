s = " This      is     a cat"
##############################
def rev1(s):
	#need memory usage
	sr = ""
	arr = s.split()
	if len(arr) > 0:
		for i in range(len(arr)-1,0,-1):
			sr += arr[i] + " "
		sr += arr[0]
	return sr

##############################
def rev2(s):
	#doesn't need memory
	sr = ""
	#find position of the first non-space symbol
	pos_start = 0
	nonspace_found = False
	for c in s:
		if c != " ":
			nonspace_found = True
			break
		pos_start += 1

	#iterate in reverse order till the first non-space symbol
	if nonspace_found:
		pos_old = len(s)
		pos = len(s)-1
		for c in reversed(s):
			if (pos == pos_start):
				break
			elif c == " ":
				if pos_old != pos + 1:
					sr += s[pos+1:pos_old] + " "
				pos_old = pos
			pos -= 1
		sr += s[pos_start:pos_old]
	return sr
##############################

print "------------------"
print rev1(s) 
print rev2(s)
print "------------------"
print rev1(s).replace(" ", "_") #replace to see spaces explicitly
print rev2(s).replace(" ", "_")
print "------------------"
print "len1 = " + str(len(rev1(s)))
print "len2 = " + str(len(rev2(s)))
print "------------------"