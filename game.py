class Game:
    def __init__(self, name, year, genre, publisher, platform, sales):
    
        if isinstance(year,str) and year.isdigit() and len(year) == 4 and 1900 <= int(year) <= 2026 :
            self.year = int(year)
        else:
            self.year =  None
            
        self.name = name
        self.genre = genre
        self.publisher = publisher
        self.platform = platform
        self.sales = sales
        
    def __str__ (self):
       return f"Nombre:{self.name}\nAño de lanzamiento:{self.year}\nGenero:{self.genre}\nPublicadores:{self.publisher}\nPlataforma:{self.platform}\nVentas{self.sales}"
        
        
        
        
minecraft = Game("Minecraft","10","Sandbox","Microsoft","PC",(300,200,100,120))

print(minecraft)