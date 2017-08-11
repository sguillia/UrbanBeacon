import wx
import math
import struct
#import sys

def new_hybrid_button(self, path, label, bmp_w, bmp_h, btn_w, btn_h):
	bmp = wx.Bitmap(path, wx.BITMAP_TYPE_ANY)
	bmp = scale_bitmap(bmp, bmp_w, bmp_h)
	btn = wx.Button(self, label=label, size=(btn_w, btn_h))
	btn.SetBitmap(bmp)
	return btn

def scale_bitmap(bitmap, width, height):
	image = wx.ImageFromBitmap(bitmap)
	image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
	result = wx.BitmapFromImage(image)
	return result

'''
t0 = float('4853.8025')
t1 = float('00219.1076')
nmea_sample = (t0, t1)
t2 = float('48.8967083')
t3 = float('2.31846')
gps_sample = (t2, t3)
'''

########################################
# Example from NMEA to GPS conversion  #
# 4853.8025 N 00219.1076 E			   #
# 48 + (53.8025 / 60) = 48.896708333   #
# 002 + (19.1076 / 60) = 2.31846	   #
# 48.896708333,2.31846				   #
########################################

# Lat is in format DDMM.MMMM
# Lon is in format DDDMM.MMMM
# M's are to be divided by 60 to get Decimal Degrees (DD) coordinates
def nmea2gps(nmea):
	lat = str(nmea[0]).zfill(9)
	lon = str(nmea[1]).zfill(10)
	lat = round(float(lat[:2]) + (float(lat[2:]) / 60), 7)
	lon = round(float(lon[:3]) + (float(lon[3:]) / 60), 7)
	return ((lat, lon))
	###
###

def gps2nmea(gps):
	latd = int(math.floor(gps[0]))
	latm = (gps[0] - latd) * 60.0
	lat = 100 * latd + latm
	lond = int(math.floor(gps[1]))
	lonm = (gps[1] - lond) * 60.0
	lon = 100 * lond + lonm
	return ((lat, lon))
	###
###

def gps2nmea_str(gps):
	latd = int(math.floor(gps[0]))
	latm = (gps[0] - latd) * 60.0
	lat = 100 * latd + latm
	lond = int(math.floor(gps[1]))
	lonm = (gps[1] - lond) * 60.0
	lon = 100 * lond + lonm
	lat_str = "%.4f" % round(lat, 4)
	lon_str = "%.4f" % round(lon, 4)
	lat_str = lat_str.zfill(9)
	lon_str = lon_str.zfill(10)
	return ((lat_str, lon_str))
	###
###

#a = 49.0948182
#b = 2.2304527
#print gps2nmea_str((a, b))

def pack_wp(wp):
	wp_data = struct.pack("fff%dsB" % 19,
		float(wp[2]),
		float(wp[3]),
		float(wp[4]),
		wp[1],
		int(wp[0]))
	return wp_data

def pack_list(wps):
	#data = '\x00' * 1000
	data = ''
	for wp in wps:
		wp_data = pack_wp(wp)
		data = data + wp_data
	print "Waypoints len is " + str(len(data))
	data = data + '\xFF' * (1000 - len(data))
	print "Total dump len is " + str(len(data))
	print "Gaps are filled with full bytes"
	return data

def write_file(path, data):
	f = open(path, "w")
	f.write(data)
	f.close()

def flash_eeprom(wps, com):
	print "--- ! --- Flashing"
	print "--- Setting current waypoint to 0 (before) ---"
	wp_reset_packet = '!' + struct.pack("B", 0)
	com.Write_packet(wp_reset_packet, 0)
	ret = com.com.read(2)
	ret = str(ret)
	print "--- Got two-bytes response : " + ret + " ---"
	i = 0
	for wp in wps:
		print "--- Loading waypoint :"
		print wp
		wp_data = pack_wp(wp)
		packet = '$' + struct.pack("B", i) + wp_data
		print "Packed wp, len is " + str(len(packet))
		print "Flashing item number " + str(i)		
		com.Write_packet(packet, True)
		print "Done writing waypoint\n"
		i = i + 1
	empty_data = '\xFF' * 32
	for _ in range(31 - i):
		print "--- Loading gap"
		empty_packet = '$' + struct.pack("B", i) + empty_data
		print "Flashing item number " + str(i)		
		i = i + 1
		com.Write_packet(empty_packet, True)
		print "Done writing gap\n"
		break

	print "--- Setting current waypoint to 0 (after) ---"
	com.Write_packet(wp_reset_packet, 0)
	ret = com.com.read(2)
	ret = str(ret)
	print "--- Got two-bytes response : " + ret + " ---"
	
	print "---   --- Done."

def unpack_dump(data):
	print "Unpacking dump"
	wps = []
	for i in range(31):
		buf = data[i*32 : (i+1)*32]
		try:
			res = struct.unpack("fff%dsB" % 19, buf)
		except Exception as e:
			print "Error from unpack : " + str(e)
			return None
		res = list(res)
		res[0] = str(res[0])
		res[1] = str(res[1])
		res[2] = str(res[2])
		res[3] = res[3].split('\0', 1)[0];
		if res[4] == 255:
			for wp in wps:
				wp.append(wp.pop(3)) # Move label to the end
				wp.append(wp.pop(0)) # Move lat to the end
				wp.append(wp.pop(0)) # Move lon to the end
				wp.append(wp.pop(0)) # Move alt to the end
				print wp
			print "Returning unpacked dump"
			return wps
		res[4] = str(int(res[4]))
		wps.append(res)
