class Animal():
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = "Covers body"
    run = "fast"
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise
    def run_way(self):
    	return self.run
dog = Animal()
dog.make_noise()
dog.size = "small"
dog.color = "black"
dog.hair = "hairless"


class Dog(Animal):
    name = 'John'
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise
    def run_way(self):
    	return self.run
    
    # color = 'brown'
    # def get_color(self):
    #  		return self.color

jon = Dog()
jon.color = 'white'
jon.name = 'jon snow'