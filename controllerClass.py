from ReservationDataFrame import ReservationDataFrame as rd
from ReservationService import ReservationService as rs
from ReservationDatabase import reservation_database
from abc import ABC, abstractmethod

class controller(ABC):
    def __init__(self, data: rd, db: reservation_database):
        self.__service = rs(data, db)

    def start_up_database(self):
        print('Starting DB')
        self.__service.start_up()

    def meal_plan_distribution(self):
        return self.__service.get_meal_plan_distribution()
    
    def get_room_type_distribution(self):
        return self.__service.get_room_type_distribution()
    
    def get_all_reservation_details(self):
        return self.__service.get_all_reservation_details()

    def get_service(self):
        return self.__service
    
    @abstractmethod
    def create_reservation(self):
        pass

    @abstractmethod
    def update_reservation(self):
        pass

    @abstractmethod
    def delete_reservation(self):
        pass

    @abstractmethod
    def get_reservation(self):
        pass

    @abstractmethod
    def get_reservation_database(self):
        pass