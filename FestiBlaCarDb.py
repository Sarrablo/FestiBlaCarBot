import sqlite3
class Db:
    def __init__(self):
        self.con = sqlite3.connect("festiblacar", check_same_thread=False)
        self.cursor = self.con.cursor()
    def create_db(self):
        #Usuarios
        sql = '''CREATE TABLE IF NOT EXISTS
                Users
                (idUser INTEGER PRIMARY KEY,
                idTgm KEY,
                nameTgm TEXT)'''
        self.cursor.execute(sql)

        #Points
                
        sql = '''CREATE TABLE IF NOT EXISTS
                Points
                (idPoint INTEGER PRIMARY KEY,
                idUser INT,
                points INT
                )'''
        self.cursor.execute(sql)

        #Points

        sql = '''CREATE TABLE IF NOT EXISTS
                User_Point
                (idUserG INT,
                idUserR INT
                )'''

        self.cursor.execute(sql)

        #Trips

        sql = '''CREATE TABLE IF NOT EXISTS
                trips
                (idTrip INTEGER PRIMARY KEY,
                idFrom INT,
                idTo INT,
                Date DATE,
                Price INT
                )'''

        self.cursor.execute(sql)

        #User_Trips

        sql = '''CREATE TABLE IF NOT EXISTS
                user_trips
                (idTrip INT,
                idUser INT
                 )'''

        self.cursor.execute(sql)


    def execute_SQL(self, sql):
        self.cursor.execute(sql)

    def insert_user(self, idTgm, nameTgm):
        if len(self.get_user_by_id(idTgm)) <= 0:
            sql = '''INSERT INTO Users (idTgm, nameTgm)
                    VALUES
                   (%s,'%s')'''%(idTgm,nameTgm)
            self.cursor.execute(sql)
            self.con.commit()

    def insert_trip(self,_from,to,date,price):
        sql = '''INSERT INTO Trips(idFrom, idTo, Date, Price)
                VALUES
                ('%s' , '%s' , '%s' , %s )'''%(_from,to,date,price)
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()

        sql = '''SELECT max(idTrip) from Trips'''
        self.cursor.execute(sql)
        return [i for i in self.cursor]
    
    def insert_user_trip(self, idUser, idTrip):
        sql = '''INSERT INTO user_trips (idUser,idTrip)
        VALUES ( %s , %s )'''%(idUser,idTrip)
        print(sql)
        self.cursor.execute(sql)
        self.con.commit()


    def get_user_by_id(self, idTgm):
        sql = '''SELECT * FROM
            Users WHERE idTgm = %s'''%(idTgm)
        self.cursor.execute(sql)
        return [i for i in self.cursor]

    def get_all_users(self):
        sql = '''SELECT * FROM
            Users '''
        self.cursor.execute(sql)
        return [i for i in self.cursor]

    def get_all_trips(self):
        sql = '''SELECT * FROM
                Trips '''
        self.cursor.execute(sql)
        return [i for i in self.cursor] 

    def insert_full_trip(self,_from,to,date,price,idTgm):
        idUser = self.get_user_by_id(idTgm)[0] 
        idTrip = self.insert_trip(_from,to,date, price)
        self.insert_user_trip(idUser[0], idTrip[0][0])



