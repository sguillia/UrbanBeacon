
import struct
import sys

f = open("data1000", "rb")
while True:
	#buf = f.read(1)
	buf = f.read(32)
	if len(buf) != 32:
		print "Breaking"
		break
	#assert(len(buf) == 32)
	#res = struct.unpack("fffBBBBBBBBBBBBBBBBBBBB", buf)
	try:
		res = struct.unpack("fff%dsB" % 19, buf)
	except Exception as e:
		print "error : " + str(e)
		quit()
	res = list(res)
	res[3] = res[3].split('\0', 1)[0];
	if res[4] == 255:
		print "End"
		#quit()
	print res
