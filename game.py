class Game:
    def __init__(self, rank, name, year, genre, publisher, platform, sales, global_sales):
    
        if isinstance(year,str) and year.isdigit() and len(year) == 4 and 1900 <= int(year) <= 2026 :
            self.year = int(year)
        else:
            self.year =  None
        self.rank = rank   
        self.name = name
        self.genre = genre
        self.publisher = publisher
        self.platform = platform
        self.sales = sales
        self.global_sales = global_sales
        
    def __str__ (self):
       return f"Puesto:{self.rank}\nNombre:{self.name}\nAño de lanzamiento:{self.year}\nGenero:{self.genre}\nPublicadores:{self.publisher}\nPlataforma:{self.platform}\nVentas por region{self.sales}\nVentas Globales{self.global_sales}"
        
        
    