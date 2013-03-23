import csv
import StringIO

def filter_lines(reader):
	
	fuelRecordsFound = 0

	lines = []

	for row in reader:
		if fuelRecordsFound == 0:
			if "FUEL RECORDS" in row:
				fuelRecordsFound = 1
			else:
				continue
		else:
			if ( len(row.strip()) > 0 ):
				lines.append(row)
			else:
				break
	return lines

class RoadTripVehicle:
	def __init__(self, csvFile):
		for line in csvFile:
			print line


csvPath = '/Users/sam/Dropbox/Road Trip Data/iPhone 5/Exported CSV Files/2005 Toyota Echo 2013-3-18.csv'
csvFile = file(csvPath,"r")
reader = RoadTripVehicle(csvFile)


#lines = filter_lines(reader)

# First, find the vehicle


