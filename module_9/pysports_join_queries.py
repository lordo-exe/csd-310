
import mysql.connector
# imports

from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
} # MySQL login info

try:
    db = mysql.connector.connect(**config) # connect to the pysports database 
    cursor = db.cursor() # cursor object get
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    # join query
    players = cursor.fetchall() # get cursor results

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key... ")


# Error work 
except mysql.connector.Error as err:
    """errors"""

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Your username or password is incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  That database doesn't exist")

    else:
        print(err)

finally:


    db.close()