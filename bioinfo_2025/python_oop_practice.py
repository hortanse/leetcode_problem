#Python OOP
class Microwave:
    def __init__(self, brand:str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.is_on = False

    def turn_on(self) -> None:
        if self.is_on:
            print(f"Microwave ({self.brand}) is already turned on")
        else:
            self.is_on = True
            print(f"Microwave ({self.brand}) is now turned on")

    def turn_off(self) -> None:
        if self.is_on:
            self.is_on = False
            print(f"Microwave ({self.brand}) is now turned off")
        else:
            print(f"Microwave ({self.brand}) is already turned off")

    def run(self, seconds: int) -> None:
        if self.is_on:
            print(f"Running ({self.brand}) for {seconds} seconds")
        else:
            print(f'A mystical force whispers: "Turn on your microwave first..."')
    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'
    
    def __repr__(self) -> str:
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'
    
smeg = Microwave('Smeg', 'B')
print(smeg)
print(smeg.brand)
print(smeg.power_rating)

bosch = Microwave('Bosch', 'C')
print(bosch.brand)
print(bosch.power_rating)

#Test the functionality
smeg.run(30)
smeg.turn_on()
smeg.run(30)
smeg.turn_off()
print(repr(smeg))
print(bosch)
