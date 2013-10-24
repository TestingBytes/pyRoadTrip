pyRoadTrip
==========

Python classes for processing data from the Road Trip iPhone app by Darren Stone.  http://darrensoft.ca/roadtrip/

Usage Example:
-------

    csvPath = sys.argv[1]
    csvFile = open(csvPath,"r")
    vehicle = RoadTripVehicle(csvFile)
    
    for record in vehicle.FuelRecords:
      output = '{0}: {1}{2} @ {3} $/{2}, {4} km'.format(
    	  record.Date,record.FillAmount,record.FillUnits,record.PricePerUnit,record.Odometer)
      print(output)
      
Output:

    2013-02-04: 40.552L @ 1.069 $/L, 117727 km
    2013-02-14: 41.699L @ 1.039 $/L, 118409 km
    2013-02-27: 38.063L @ 1.079 $/L, 119046 km
    2013-03-11: 41.434L @ 1.099 $/L, 119674 km


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/TestingBytes/pyroadtrip/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

