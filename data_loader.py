import pandas as pd
from game import Game

def load_games(csv_path):
    read_info = pd.read_csv(csv_path)
    game_list = []
    for index, row in read_info.iterrows():
        sales = {
            "NA_Sales": row["NA_Sales"],
            "EU_Sales": row["EU_Sales"],
            "JP_Sales": row["JP_Sales"],
            "Other_Sales": row["Other_Sales"]
        }
        
        global_sales = sum(valor for valor in sales.values())
        game = Game(row["Rank"], row["Name"],row["Year"],row["Genre"],row["Publisher"],row["Platform"], sales, global_sales)
        game_list.append(game)
        
    return game_list

