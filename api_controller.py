from Reservation import Reservation as rev
from ReservationDataFrame import ReservationDataFrame as rd
from ReservationService import ReservationService as rs
from ReservationDatabase import reservation_database
from controllerClass import controller
from flask import request

class api_controller(controller):
    def __init__(self, data: rd, db: reservation_database):
        super().__init__(data, db)

    def create_reservation(self):
        data = request.get_json()

        reservation = rev('0', data['no_of_adults'], data['no_of_children'], data['no_of_weekend_nights'], data['no_of_week_nights'],
                            data['type_of_meal_plan'], data['required_car_parking_space'], data['room_type_reserved'], data['arrival_year'],
                            data['arrival_month'], data['arrival_date'], data['avg_price_per_room'])

        return super().get_service().create_reservation(reservation)

    def get_reservation(self, id: str):
        return super().get_service().get_reservation_info(id)
    
    def update_reservation(self, id: str):
        data = request.get_json()

        reservation = rev(id, data['no_of_adults'], data['no_of_children'], data['no_of_weekend_nights'], data['no_of_week_nights'],
                            data['type_of_meal_plan'], data['required_car_parking_space'], data['room_type_reserved'], data['arrival_year'],
                            data['arrival_month'], data['arrival_date'], data['avg_price_per_room'])
        return super().get_service().update_reservation(reservation)
    
    def delete_reservation(self, id: str):
        return super().get_service().delete_reservation(id)
    
    def get_reservation_database(self, id: str):
        return super().get_service().get_reservation_database(id)
    

