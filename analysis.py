
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



