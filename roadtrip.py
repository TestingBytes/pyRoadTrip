import sys
import datetime
import logging

log = logging.getLogger(__name__)
#log.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)

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
		
		# Instance Variables
		self._section = ""
		self.Version = ""
		self.Language = ""
		self.FuelRecords = []
		self.TireLogRecords = []

		# Logging
		log = logging.getLogger(__name__)

		self._i = 0
		for line in csvFile:
			self._i+=1
			line = line.strip()
			if self._section and not line:
				self._section = line
				log.debug(str(self._i)+": clearing section")
				continue

			if line in ("Version, Language", "FUEL RECORDS", "TIRE LOG"):
				self._section = line
				log.debug(str(self._i)+": found " + self._section + " Section")
				continue

			if "Version,Language" in self._section:
				values = line.split(",")
				self.Version = values[0]
				self.Language = values[1]
				log.debug(str(self._i) + ": Saving Version/Language values")
				continue

			if "FUEL RECORDS" in self._section:
				if "Odometer" not in line:
					self.FuelRecords.append( RoadTripVehicleFuelRecord(line) )
					log.debug(str(self._i) + ": added " + self._section)
				continue

			if "TIRE LOG" in self._section:
				if "Name" not in line:
					self.TireLogRecords.append( RoadTripTireLogRecord(line) )
					log.debug(str(self._i) + ": added " + self._section)
				continue
