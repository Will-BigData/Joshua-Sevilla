from Reservation import Reservation as rev
from ReservationDataFrame import ReservationDataFrame as rd
from ReservationService import ReservationService as rs
from ReservationDatabase import reservation_database
from flask import request

class api_controller():
    def __init__(self, data: rd, db: reservation_database):
        self.__service = rs(data, db)
        
    def start_up_database(self):
        print('Starting DB')
        self.__service.start_up()

    def create_reservation(self):
        data = request.get_json()

        reservation = rev('0', data['no_of_adults'], data['no_of_children'], data['no_of_weekend_nights'], data['no_of_week_nights'],
                            data['type_of_meal_plan'], data['required_car_parking_space'], data['room_type_reserved'], data['arrival_year'],
                            data['arrival_month'], data['arrival_date'], data['avg_price_per_room'])

        return self.__service.create_reservation(reservation)

    def get_reservation(self, id: str):
        return self.__service.get_reservation_info(id)
    
    def update_reservation(self, id: str):
        data = request.get_json()

        reservation = rev(id, data['no_of_adults'], data['no_of_children'], data['no_of_weekend_nights'], data['no_of_week_nights'],
                            data['type_of_meal_plan'], data['required_car_parking_space'], data['room_type_reserved'], data['arrival_year'],
                            data['arrival_month'], data['arrival_date'], data['avg_price_per_room'])
        return self.__service.update_reservation(reservation)
    
    def delete_reservation(self, id: str):
        return self.__service.delete_reservation(id)
    
    def meal_plan_distribution(self):
        return self.__service.get_meal_plan_distribution()

