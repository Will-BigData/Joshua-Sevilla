import csv
import pandas as pd
from Reservation import Reservation as rev

# read and write to dataframe
# replace with database
class ReservationDataFrame():

    __df = pd.DataFrame

    def __init__(self) -> None:
        self.__df = pd.read_csv("Hotel_Reservations.csv", dtype='string')

    def read_data(self):
        self.__df = pd.read_csv("Hotel_Reservations.csv", dtype='string')

    def write_data(self):
        self.__df.to_csv('Hotel_Reservations.csv', mode='w', index=False, header=True)

    def print_df(self):
        print(self.__df)

    def print_tail(self):
        print(self.__df.tail())

    def get_next_id(self):
        id = self.__df.at[self.__df.index[-1],'Booking_ID']
        new_num = int(id[3:]) + 1
        number_of_zeros = 5 - len(str(new_num))
        return "INN" + '0' * number_of_zeros + str(new_num)
    
    def get_reservation(self, id):
        exists = self.__df['Booking_ID'].isin([id]).any()

        if exists:
            return self.__df[self.__df['Booking_ID'] == id]
        else:
            return pd.DataFrame()
        
    def delete_reservation(self, id):
        exists = self.__df['Booking_ID'].isin([id]).any()

        if exists:
            self.__df = self.__df[self.__df['Booking_ID'] != id]
            self.__df.to_csv('Hotel_Reservations.csv', mode='w', index=False, header=True)
            self.read_data()
            return "Deleted"
        else:
            return "Not found"
        
    def appendToDataframe(self, new_reservation: rev):
        new_data = pd.DataFrame([{'Booking_ID': new_reservation.get_Booking_ID(),
                         'no_of_adults': new_reservation.get_no_of_adults(),
                         'no_of_children': new_reservation.get_no_of_children(),
                         'no_of_weekend_nights': new_reservation.get_no_of_weekend_nights(),
                         'no_of_week_nights': new_reservation.get_no_of_week_nights(),
                         'type_of_meal_plan': new_reservation.get_type_of_meal_plan(),
                         'required_car_parking_space': new_reservation.get_required_car_parking_space(),
                         'room_type_reserved': new_reservation.get_room_type_reserved(),
                         'arrival_year': new_reservation.get_arrival_year(),
                         'arrival_month': new_reservation.get_arrival_month(),
                         'arrival_date': new_reservation.get_arrival_date(),
                         'avg_price_per_room': new_reservation.get_avg_price_per_room()
                         }])
      
        new_data.to_csv('Hotel_Reservations.csv', mode='a', index=False, header=False)
        self.read_data()

        return self.get_reservation(new_reservation.get_Booking_ID())
       
    def updateReservation(self, reservation: rev):
        exists = self.__df['Booking_ID'].isin([reservation.get_Booking_ID()]).any()

        if exists:
            self.__df.loc[self.__df['Booking_ID'] == reservation.get_Booking_ID(), 
                      ['Booking_ID', 'no_of_adults', 'no_of_children', 'no_of_weekend_nights', 'no_of_week_nights'
                       , 'type_of_meal_plan', 'required_car_parking_space', 'room_type_reserved',
                       'arrival_year', 'arrival_month', 'arrival_date', 'avg_price_per_room']] = [
                            reservation.get_Booking_ID(), reservation.get_no_of_adults(), reservation.get_no_of_children(),
                           reservation.get_no_of_weekend_nights(), reservation.get_no_of_week_nights(),
                           reservation.get_type_of_meal_plan(), reservation.get_required_car_parking_space(),
                           reservation.get_room_type_reserved(), reservation.get_arrival_year(),
                           reservation.get_arrival_month(), reservation.get_arrival_date(), reservation.get_avg_price_per_room()]
                     
            self.__df.to_csv('Hotel_Reservations.csv', mode='w', index=False, header=True)
            self.read_data()

            return self.get_reservation(reservation.get_Booking_ID())
        else:
            return pd.DataFrame()





