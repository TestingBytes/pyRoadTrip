import sys
import datetime
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)

log_formatter = logging.Formatter("{asctime} {levelname} {message}", style='{')
ch.setFormatter(log_formatter)

log.addHandler(ch)

class RoadTripVehicleFuelRecord:
	def __init__(self, csvRow):
		values = csvRow.split(",")

		self.Odometer 		= values[0]
		self.TripDistance 	= values[1]
		dateValue			= values[2].split(" ")[0].replace('"','')
		(year,month,day) 	= dateValue.split('-')
		self.Date 			= datetime.date(int(year),int(month),int(day))
		self.FillAmount 	= values[3]
		self.FillUnits 		= values[4]
		self.PricePerUnit 	= values[5]
		self.TotalPrice 	= values[6]
		self.PartialFill 	= values[7]

class RoadTripTireLogRecord:
	def __init__(self, csvRow):
		values = csvRow.split(",")
		self.Name 		= values[0]
		year,month,day 	= values[1].replace('"','').split('-')
		self.StartDate 	= datetime.date(int(year),int(month),int(day))
		self.StartOdometer = values[2]
		self.Distance = values[6]

class RoadTripVehicle:
	def __init__(self, csvFile):
		section = ""
		self.Version = ""
		self.Language = ""
		self.FuelRecords = []
		self.TireLogRecords = []

		# Logging
		log = logging.getLogger(__name__)

		i = 0
		for line in csvFile:
			i+=1
			line = line.strip()
			if section and not line:
				section = ""
				log.debug(str(i)+": clearing section")
				continue

			if "Version,Language" in line:
				#_setSection("Version,Language")
				section = line
				log.debug(str(i)+": found Version/Language Section")
				continue

			if "Version,Language" in section:
				values = line.split(",")
				self.Version = values[0]
				self.Language = values[1]
				log.debug(str(i) + ": Saving Version/Language values")
				continue

			if "FUEL RECORDS" in line:
				section = line
				log.debug(str(i) + ": found " + line + " Section")
				continue

			if "FUEL RECORDS" in section:
				if "Odometer" not in line:
					record = RoadTripVehicleFuelRecord(line)
					self.FuelRecords.append(record)
					log.debug(str(i) + ": added " + section)
					continue
				else:
					continue

			if "TIRE LOG" in line:
				section = line
				log.debug(str(i) + ": found " + line + " Section")
				continue

			if "TIRE LOG" in section:
				if "Name" not in line:
					section = line
					log.debug(str(i) + ": added " + section)
					record = RoadTripTireLogRecord(line)
					self.TireLogRecords.append(record)
					continue
				else:
					continue

	#def _setSection(self, sectionName):

	#def _addRecord(self, sectionName):

	#def _clearSection(self):


csvPath = sys.argv[1]
csvFile = open(csvPath,"r")
vehicle = RoadTripVehicle(csvFile)

for record in vehicle.FuelRecords:
	strout = '{0}: {1}{2} @ {3} $/{2}, {4} km'.format(
		record.Date,record.FillAmount,record.FillUnits,record.PricePerUnit,record.Odometer)
	log.debug(strout)