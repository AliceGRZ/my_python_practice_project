class Shelter:
    name = ""
    color  = ""
    breed = ""
    age = 0
    health_condition = ["bad", "moderate", "good", "excellent"]
    in_foster_family = True

    def description(self):
        return print(f"Dog's description: name: {self.name}, color: {self.color}, breed: {self.breed}, age: {self.age}, health_condition: {self.health_condition}, in foster family: {self.in_foster_family}")
    
    def adopt_dog(self):
        if self.age <= 6: 
            if self.health_condition <= self.health_condition[2]:
                if self.in_foster_family == False:
                    if self.breed == "mixed":
                        print(f"Dog {self.name} can be adopted for 50$")
                    else:
                        print(f"Dog {self.name} can be adopted for 100$")
                else:
                    print(f"Dog {self.name} can be adopted in 1 month")
            else:
                print(f"Dog {self.name} hospitalized - consult adoption with the vet")
        else:
            print(f"Dog {self.name} older than 6")
                
dog_1 = Shelter()
dog_1.name = "Fafik"
dog_1.color = "brown"
dog_1.breed = "mixed"
dog_1.age = 2
dog_1.health_condition = dog_1.health_condition[2] 
dog_1.in_foster_family = False

dog_2 = Shelter()
dog_2.name = "Bobek"
dog_2.color = "white and black"
dog_2.breed = "Jack Russel"
dog_2.age = 1.5
dog_2.health_condition = dog_2.health_condition[1]
dog_2.in_foster_family = True

dog_3 = Shelter()
dog_3.name = "Ronia"
dog_3.color = "black"
dog_3.breed = "German Sheppard"
dog_3.age = 8
dog_3.health_condition = dog_3.health_condition[3]
dog_3.in_foster_family = False

#dog_1.description()
#dog_2.description()
       
dog_1.adopt_dog()
dog_2.adopt_dog()
dog_3.adopt_dog()



    


