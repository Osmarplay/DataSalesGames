from data_loader import load_games
from analysis import genre_most_sold, top_game_per_genre, publisher_most_sold


if __name__ == "__main__":
    games = load_games("vgsales.csv")
    print(f"Se cargaron {len(games)} juegos")
    
    genero, ventas = genre_most_sold(games)
    print(f"Género más vendido: {genero} con {ventas} ventas globales")
    
top_games = top_game_per_genre(games)
print(f"\nJuego con más ventas por género:")
for game in top_games:
    print(f" {game.genre}: {game.name}, ({round(game.global_sales)}M ventas)")
       
publisher, ventas_pub = publisher_most_sold(games)
print(f"\nPublisher con más ventas: {publisher} con {round(ventas_pub, 2)}M ventas globales")