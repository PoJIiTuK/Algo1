class Ship:
    def __init__(self, name='no', tonnage=0, number_of_passengers=0):
        self.name = name
        self.tonnages = tonnage
        self.number_of_passengers = number_of_passengers

    def __str__(self):
        return  "[Name="+self.name+ ";Tonnage="+ str(self.tonnages) +"; Number of passengers="+ str(self.number_of_passengers)+";]"
