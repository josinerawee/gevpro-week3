import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import sys

def main(argv):
	
	tree = ET.parse(argv[1])
	root = tree.getroot()
	for POINT in root.findall('POINT'):
		bottomhz=POINT.find("BOTTOM_HZ").text
		tophz=POINT.find("TOP_HZ").text
		f0end=POINT.find("F0_END").text
		f0start=POINT.find("F0_START").text
		if bottomhz <= f0end <= tophz:
			pass
		else:
			end=POINT.findall("F0_END")
			for F0_END in end:
				POINT.remove(F0_END)
		if bottomhz<= f0start <=tophz:
			pass
		else:
			start=POINT.findall("F0_START")
			for F0_START in start:
				POINT.remove(F0_START)
	tree.write(argv[2])
main(sys.argv)
