def genre_most_sold(games):
    
    genero = {}

    for game in games:
        if not game.genre in genero:
            genero[game.genre] = []
        genero[game.genre].append(game)
        
    genero_ventas = {}

    for genre, game_list in genero.items():
        total_ventas = sum(game.global_sales for game in game_list)
        genero_ventas[genre] = total_ventas
        
    genero_mas_vendido = max(genero_ventas, key=genero_ventas.get)
    ventas_totales = genero_ventas[genero_mas_vendido]
    
    return genero_mas_vendido, ventas_totales

def top_game_per_genre(games):
    
    genero = {}
    
    for game in games:
        if not game.genre in genero:
            genero[game.genre] = []
        genero[game.genre].append(game)
            
    top_game_list = []
            
    for genre in genero:
        mejor_juego = max(genero[genre], key=lambda game: game.global_sales)
        top_game_list.append(mejor_juego)

    return top_game_list

def publisher_most_sold(games):
    
    publishers = {}

    for game in games:
        if not game.publisher in publishers:
            publishers[game.publisher] = []
        publishers[game.publisher].append(game)
        
    publishers_sales = {}

    for publisher, game_list in publishers.items():
        total_ventas = sum(game.global_sales for game in game_list)
        publishers_sales[publisher] = total_ventas
        
    publisher_most_sales = max(publishers_sales, key=publishers_sales.get)
    ventas_totales = publishers_sales[publisher_most_sales]
    
    return publisher_most_sales, ventas_totales

#Esta funcion solo ayuda a conseguir las primerass tres palabras de un juego 
def get_base_name(name):
    nombre_limpio = name.replace(":", "").replace(",", "")
    separados = nombre_limpio.split()
    palabras_3 = separados[0:3]
    nombre_base = " ".join(palabras_3)
    return nombre_base


def game_with_sequels(games):
    base_name = {}
    sequels_games = {}
    nombres_vistos = set()
    juegos_unicos = []
    
    for game in games:
        if game.name not in nombres_vistos:
            nombres_vistos.add(game.name)
            juegos_unicos.append(game)
    
    
    for game in juegos_unicos:
        base = get_base_name(game.name)
        if base not in base_name:
            base_name[base] = []
        base_name[base].append(game.name)
      
    for base, lista in base_name.items():
        if len(lista) > 1:
            sequels_games[base] = lista
        
    return sequels_games
            