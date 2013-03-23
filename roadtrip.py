import sys

class RoadTripVehicleFuelRecord:
	def __init__(self, csvRow):
		values = csvRow.split(",")

		self.Odometer 		= values[0]
		self.TripDistance 	= values[1]
		self.Date 			= values[2]
		self.FillAmount 	= values[3]
		self.FillUnits 		= values[4]
		self.PricePerUnit 	= values[5]
		self.TotalPrice 	= values[6]
		self.PartialFill 	= values[7]

class RoadTripVehicle:
	def __init__(self, csvFile):
		section = ""
		self.Version = ""
		self.Language = ""
		self.FuelRecords = []

		i = -1
		for line in csvFile:
			i+=1
			
			if section and not line.strip():
				section = ""
				print str(i) + ": clearing section"
				continue

			if "Version,Language" in line:
				section = line
				print str(i) + ": found Version/Language Section"
				continue

			if "Version,Language" in section:
				values = line.split(",")
				self.Version = values[0]
				self.Language = values[1]
				print str(i) + ": Saving Version/Language values"
				continue

			if "FUEL RECORDS" in line:
				section = line
				print str(i) + ": found " + line + " Section"
				continue

			if "FUEL RECORDS" in section:
				record = RoadTripVehicleFuelRecord(line)
				self.FuelRecords.append(record)
				print str(i) + " added " + section
				continue

csvPath = sys.argv[1]
csvFile = file(csvPath,"r")
vehicle = RoadTripVehicle(csvFile)
