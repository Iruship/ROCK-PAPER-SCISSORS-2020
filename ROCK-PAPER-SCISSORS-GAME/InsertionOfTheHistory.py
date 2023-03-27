def InsertionOfTheGameDetails(PlayerName,HumanPlayer_wins,computer_wins,Total_draws,Total_game_plays):
    "Insertion of the Game details"
    import mysql.connector
    from prettytable import from_db_cursor
    import mysql.connector
#Open a database connection with a dictionary
    conDict={"host":"localhost",
             "user":"root",
             "database":"historyofthegame",
             "password":""
             }
    db=mysql.connector.connect(**conDict)
#Prepare a cursor object using cursor () method
    cursor=db.cursor()
    cursor.execute("SELECT * FROM game_history")
    GamePlays = from_db_cursor(cursor)
    print(GamePlays)
    data=GamePlays.get_html_string(attributes={"name":"GameHistory","class":"table"},format=True)
    File_object=open("HTML.html","w")
    File_object.write(data)
#commit the change
#Executing sql query using the method execute
    updateText="INSERT INTO game_history VALUES ('"+PlayerName+"','"+HumanPlayer_wins+"','"+computer_wins+"','"+Total_draws+"','"+Total_game_plays+"')"
    cursor.execute(updateText)
    db.commit()
#disconnect from the server
    db.close()
    return
