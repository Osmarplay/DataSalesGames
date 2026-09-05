from data_loader import load_games
from analysis import genre_most_sold

if __name__ == "__main__":
    games = load_games("vgsales.csv")
    print(f"Se cargaron {len(games)} juegos")
    
    genero, ventas = genre_most_sold(games)
    print(f"Género más vendido: {genero} con {ventas} ventas globales")