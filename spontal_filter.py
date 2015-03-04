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
		BOTTOM_HZ=float(bottomhz)
		TOP_HZ=float(tophz)
		F0_END=float(f0end)
		F0_START=float(f0start)
		if F0_END < BOTTOM_HZ or F0_END >TOP_HZ or F0_START< BOTTOM_HZ or F0_START >TOP_HZ:
			root.remove(POINT)
	tree.write(argv[2])
main(sys.argv)
