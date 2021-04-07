# Avoid Use of Unncessary Comments, rather focus on better naming conventions, which will reduce the use of comments automatically

# Not good
db = []
def get_name(p1):   # Here get_name will get the player's name. Here, player is player1
    return search(p1, db)    # Here 'db' is the database of the players


# Better
player_database = []
def get_player_name(player1):
    return search_player_name(player1, player_database)

# Her, Instead of additonal comments, we are using more descriptive variable and function names
