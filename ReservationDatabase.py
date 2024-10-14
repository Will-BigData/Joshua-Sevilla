from Reservation import Reservation as rev
import mysql.connector
import pandas as pd

class reservation_database():

    def __init__(self, user, password, host, database):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__database = database

    def get_connection(self):
        return mysql.connector.connect(user=self.__user, password=self.__password,
                              host=self.__host,
                              database=self.__database)
        
    def start_up(self):
        cnx = self.get_connection()

        cursor = cnx.cursor()

        cursor.execute("DROP DATABASE IF EXISTS project_0")
        cursor.execute("CREATE DATABASE project_0")
        cursor.execute("USE project_0")

        add_reservation_table = "CREATE TABLE reservations (Booking_ID varchar(8), no_of_adults int, no_of_children int, no_of_weekend_nights int, no_of_week_nights int, " \
                            "type_of_meal_plan varchar(255), required_car_parking_space int, room_type_reserved varchar(255), \
                            arrival_year int, arrival_month int, arrival_date int, avg_price_per_room int)"
        
        cursor.execute(add_reservation_table)

        df = pd.read_csv("Hotel_Reservations.csv", dtype='string')

        for row in df.itertuples():
            cursor.execute("INSERT INTO reservations (Booking_ID, no_of_adults, no_of_children, no_of_weekend_nights, no_of_week_nights, \
                            type_of_meal_plan, required_car_parking_space, room_type_reserved, \
                            arrival_year, arrival_month, arrival_date, avg_price_per_room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                            (row.Booking_ID, row.no_of_adults, row.no_of_children, row.no_of_weekend_nights, row.no_of_week_nights, 
                             row.type_of_meal_plan, row.required_car_parking_space,
                             row.room_type_reserved, row.arrival_year, row.arrival_month, row.arrival_date, row.avg_price_per_room))
            
            cnx.commit()

        cnx.close()
    
    def create_reservation(self, new_reservation: rev):
        cnx = self.get_connection()

        cursor = cnx.cursor()
        
        cursor.execute("INSERT INTO reservations (Booking_ID, no_of_adults, no_of_children, no_of_weekend_nights, no_of_week_nights, \
                            type_of_meal_plan, required_car_parking_space, room_type_reserved, \
                            arrival_year, arrival_month, arrival_date, avg_price_per_room) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                            (new_reservation.get_Booking_ID(), int(new_reservation.get_no_of_adults()), int(new_reservation.get_no_of_children()), 
                             int(new_reservation.get_no_of_weekend_nights()), int(new_reservation.get_no_of_week_nights()), 
                             new_reservation.get_type_of_meal_plan(), int(new_reservation.get_required_car_parking_space()),
                             new_reservation.get_room_type_reserved(), int(new_reservation.get_arrival_year()), int(new_reservation.get_arrival_month()), 
                             int(new_reservation.get_arrival_date()), int(new_reservation.get_avg_price_per_room())))

        cnx.commit()
        cnx.close()

        return self.get_reservation(new_reservation.get_Booking_ID())

    def update_reservation(self, new_reservation: rev):

        self.get_reservation(new_reservation.get_Booking_ID())

        cnx = self.get_connection()
        cursor = cnx.cursor()

        cursor.execute("UPDATE reservations SET no_of_adults = %s, no_of_children = %s, \
                       no_of_weekend_nights = %s, no_of_week_nights = %s, \
                        type_of_meal_plan = %s, required_car_parking_space = %s, room_type_reserved = %s, \
                        arrival_year = %s, arrival_month = %s, arrival_date = %s, avg_price_per_room = %s WHERE BOOKING_ID = %s", 
                        (int(new_reservation.get_no_of_adults()), int(new_reservation.get_no_of_children()), 
                             int(new_reservation.get_no_of_weekend_nights()), int(new_reservation.get_no_of_week_nights()), 
                             new_reservation.get_type_of_meal_plan(), int(new_reservation.get_required_car_parking_space()),
                             new_reservation.get_room_type_reserved(), int(new_reservation.get_arrival_year()), int(new_reservation.get_arrival_month()), 
                             int(new_reservation.get_arrival_date()), int(new_reservation.get_avg_price_per_room()), new_reservation.get_Booking_ID()))
        
        cnx.commit()
        cnx.close()

        return self.get_reservation(new_reservation.get_Booking_ID())

    def delete_reservation(self, id):
        self.get_reservation(id)

        cnx = self.get_connection()
        cursor = cnx.cursor()

        cursor.execute("DELETE FROM reservations WHERE Booking_ID = %s", (id,))

        cnx.commit()
        cnx.close()

        return 'Deleted'

    def get_reservation(self, id):
        cnx = self.get_connection()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM reservations WHERE Booking_ID = %s", (id,))

        row = cursor.fetchone()
        cnx.close()
        if row:
            return row
        else:
            return 'Not found in database'

    def get_meal_plan_distribution(self):
        cnx = self.get_connection()

        query = "select type_of_meal_plan as 'Type Selected', count(type_of_meal_plan) as 'Count' \
                        from reservations \
                        group by type_of_meal_plan;"

        return pd.read_sql(query, con = cnx)
    
    def get_room_type_distribution(self):
        cnx = self.get_connection()

        query = "select room_type_reserved as 'Room Type', count(room_type_reserved) as 'Rooms Reserved', \
                        avg(avg_price_per_room) as 'Average Price', \
                        avg(no_of_week_nights + no_of_weekend_nights) as 'Average Nights'\
                        from reservations group by room_type_reserved;"

        return pd.read_sql(query, cnx) 
    
    def get_all_reservation_details(self):
        cnx = self.get_connection()

        query = "select Booking_ID, (no_of_adults + no_of_children) as 'Number of Guests', \
                        (no_of_weekend_nights + no_of_week_nights) as 'Number of Nights', \
                        type_of_meal_plan as 'Meal Plan',  \
                        CASE \
                            WHEN required_car_parking_space = 0 THEN 'No' \
                            WHEN required_car_parking_space = 1 THEN 'Yes' \
                        END AS 'Parking', \
                        room_type_reserved as 'Room Type', \
                        concat(arrival_month, '-', arrival_date, '-', arrival_year) as 'Arrival Date', \
                        avg_price_per_room as 'Price' \
                        from reservations;"

        return pd.read_sql(query, cnx) 
    
    def get_reservation_database(self, id):
        cnx = self.get_connection()

        query = "select Booking_ID, (no_of_adults + no_of_children) as 'Number of Guests', \
                        (no_of_weekend_nights + no_of_week_nights) as 'Number of Nights', \
                        type_of_meal_plan as 'Meal Plan',  \
                        CASE \
                            WHEN required_car_parking_space = 0 THEN 'No' \
                            WHEN required_car_parking_space = 1 THEN 'Yes' \
                        END AS 'Parking', \
                        room_type_reserved as 'Room Type', \
                        concat(arrival_month, '-', arrival_date, '-', arrival_year) as 'Arrival Date', \
                        avg_price_per_room as 'Price' \
                        from reservations where Booking_ID = %s;"
        
        params = (id,)

        return pd.read_sql(query, cnx, params=params) 
