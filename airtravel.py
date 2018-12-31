class Flight:

	def __init__(self, flnum, aircraft):
		self._flightnumber = flnum
		self._aircraft = aircraft

	def get_aircraft_model(self):
		return self._aircraft.getModel()
	




class AirCraft:
    
    def __init__(self, reg, model, rows, seatinrow):
    	self._registeration = reg
    	self._modelnumber = model
    	self._totalrows = rows
    	self._seatsperrow = seatinrow

    def getRegisteration(self):
    	return self._registeration

    def getModel(self):
    	return self._modelnumber

    def seatingplan(self):
    	return (range(1, self._totalrows), "ABCDEFGHIJHKLMNOPQRSTUVWXYZ"[:self._seatsperrow])
