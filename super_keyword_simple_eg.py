class India:
	Location="India"
	def getLocation(self):
		print("I am in ",India.Location)
	def proud(self):
		print("I am Indian")

class Maharashtra(India):
	Location="Maharashtra"
	def getLocation(self):
		super().getLocation()
		print("I am in ",Maharashtra.Location)

class Kolhapur(Maharashtra):
	Location="Kolhapur"
	def getLocation(self):
		print(India.Location)
		print(Maharashtra.Location)
		print(super().Location)
		super().getLocation()
		print("I am in ",Kolhapur.Location)
		k.proud()

k=Kolhapur()
k.getLocation()