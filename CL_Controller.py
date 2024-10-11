from Reservation import Reservation as rev
from ReservationDataFrame import ReservationDataFrame as rd
from ReservationService import ReservationService as rs
from ReservationDatabase import reservation_database
from controllerClass import controller

class cl_Controller(controller):
    def __init__(self, data: rd, db: reservation_database):
        super().__init__(data, db)

    def create_reservation(self):
        adults = input("Number of adults: ")
        children = input("Number of children: ")
        weekend_nights = input("Number of weekend nights: ")
        weekday_nights = input("Number of weekday nights: ")
        meal_plan_choice = input("Select Meal Plan: \n1, 2, or none: ")
        meal_plan = 'Not Selected'
        match meal_plan_choice:
            case '1':
                meal_plan = 'Meal Plan 1'
            case '2':
                meal_plan = 'Meal Plan 2'
            case _:
                meal_plan = 'Not Selected'

        parking = input("Select y or n if parking is needed: ")
        if parking == 'y':
            parking = '1'
        else:
            parking = '0'

        room_type = input("Select room type: \n1 or 4: ")
        if room_type == '1':
            room_type = 'Room_Type 1'
        elif room_type == '4':
            room_type = 'Room_Type 4'
        year = input("Input arrival year: ")
        month = input("Input arrival month: ")
        date = input("Input arrival date: ")
        average_price = input("Input average price: ")

        new_reservation = rev('0', adults, children, weekend_nights, weekday_nights, meal_plan, parking, room_type, year, month, date, average_price)
    
        print(super().get_service().create_reservation(new_reservation))

    def update_reservation(self):
        id = input("Enter ID of reservation to update: ")
        adults = input("Number of adults: ")
        children = input("Number of children: ")
        weekend_nights = input("Number of weekend nights: ")
        weekday_nights = input("Number of weekday nights: ")
        meal_plan_choice = input("Select Meal Plan: \n1, 2, or none: ")
        meal_plan = 'Not Selected'
        match meal_plan_choice:
            case '1':
                meal_plan = 'Meal Plan 1'
            case '2':
                meal_plan = 'Meal Plan 2'
            case _:
                meal_plan = 'Not Selected'

        parking = input("Select y or n if parking is needed: ")
        if parking == 'y':
            parking = '1'
        else:
            parking = '0'

        room_type = input("Select room type: \n1 or 4: ")
        if room_type == '1':
            room_type = 'Room_Type 1'
        elif room_type == '4':
            room_type = 'Room_Type 4'
        year = input("Input arrival year: ")
        month = input("Input arrival month: ")
        date = input("Input arrival date: ")
        average_price = input("Input average price: ")

        new_reservation = rev(id, adults, children, weekend_nights, weekday_nights, meal_plan, parking, room_type, year, month, date, average_price)

        return super().get_service().update_reservation(new_reservation)


    def delete_reservation(self):
        id = input("Enter ID of reservation to delete: ")
        return super().get_service().delete_reservation(id)

    def get_reservation(self):
        id = input("Enter ID of reservation: ")
        return super().get_service().get_reservation_info(id)
    
    
    