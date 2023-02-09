

import mysql.connector
# imports

from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
} # Connecting to MSQL database


def show_players(cursor, title):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    characters = cursor.fetchall()
    print("\n  -- {} --".format(title))
    for player in characters:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
# inner join and display


try:

    db = mysql.connector.connect(**config) # Connect to MYSQL 
    cursor = db.cursor() # Cursor object obtained
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
    player_data = ("Smeagol", "Shire Folk", 1)
    cursor.execute(add_player, player_data)

    db.commit()
    show_players(cursor, "DISPLAYING PLAYER AFTER INSERT")

    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player)
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key... ")


# Error work
except mysql.connector.Error as err:
    """errors""" 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Your username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  That database does not exist")

    else:
        print(err)

finally:
    """ Quit MySQL """

    db.close()