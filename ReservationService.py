from ReservationDataFrame import ReservationDataFrame
from Reservation import Reservation as rev
from datetime import *
from ReservationDatabase import reservation_database

#interact with dataframe
class ValidationError(Exception):
    def __init__(self, message):            
        self.message = message
            
    
class ReservationService():
    def __init__(self, reservation_dataframe: ReservationDataFrame, reservation_database: reservation_database):
        self.__reservation_dataframe = reservation_dataframe
        self.__reservation_database = reservation_database

    def start_up(self):
        self.__reservation_database.start_up()

    def create_reservation(self, reservation: rev):

        int_values = [reservation.get_no_of_adults(), reservation.get_no_of_children(), 
                      reservation.get_no_of_week_nights(), reservation.get_no_of_weekend_nights(), reservation.get_avg_price_per_room(),
                      reservation.get_arrival_year(), reservation.get_arrival_month(), reservation.get_arrival_date()]

        for value in int_values:
            try:
                int(value)
            except ValueError:
                raise ValidationError("'{0}' value entered is not numeric".format(value))
        
        if int(reservation.get_no_of_adults()) < 0 or int(reservation.get_no_of_children()) < 0:
            raise ValidationError("Number of children and number of adults must be greater than 0")
        
        if int(reservation.get_no_of_adults()) + int(reservation.get_no_of_children()) == 0:
            raise ValidationError("Must have guests to reserve a room")

        if int(reservation.get_no_of_week_nights()) < 0 or int(reservation.get_no_of_weekend_nights()) < 0:
            raise ValidationError("Number of week and weekend nights must be greater than 0")
        
        if int(reservation.get_no_of_week_nights()) + int(reservation.get_no_of_weekend_nights()) == 0:
            raise ValidationError("Must have more than 0 total nights to reserve a room")
        
        if reservation.get_type_of_meal_plan() not in ("Not Selected", "Meal Plan 1", "Meal Plan 2"):
            raise ValidationError("Invalid Meal plan choice")
        
        if reservation.get_required_car_parking_space() not in ("0", "1"):
            raise ValidationError("Invalid parking choice")
        
        if reservation.get_room_type_reserved() not in ('Room_Type 1', 'Room_Type 4'):
            raise ValidationError("Invalid room choice")

        if int(reservation.get_avg_price_per_room()) < 0:
            raise ValidationError("Price must be greater than 0")
        
        date_string = "{}-{}-{}".format(reservation.get_arrival_month(), reservation.get_arrival_date(), reservation.get_arrival_year())

        if not 1900 <= int(reservation.get_arrival_year()) <= 2100:
            raise ValidationError("Invalid Year")
        
        try:
            dt = datetime.strptime(date_string, '%m-%d-%Y')
        except ValueError:
            raise ValidationError("Invalid Date")
        
        if int(reservation.get_avg_price_per_room()) < 0:
            raise ValidationError("Average price value must be greater than 0")
        
        reservation.set_Booking_ID(self.__reservation_dataframe.get_next_id())
        
        self.__reservation_database.create_reservation(reservation)
        return self.__reservation_dataframe.appendToDataframe(reservation)

    def delete_reservation(self, id):
        self.__reservation_database.delete_reservation(id)
        return self.__reservation_dataframe.delete_reservation(id)

    def update_reservation(self, reservation: rev):
        int_values = [reservation.get_no_of_adults(), reservation.get_no_of_children(), 
                      reservation.get_no_of_week_nights(), reservation.get_no_of_weekend_nights(), reservation.get_avg_price_per_room(),
                      reservation.get_arrival_year(), reservation.get_arrival_month(), reservation.get_arrival_date()]

        for value in int_values:
            try:
                int(value)
            except ValueError:
                raise ValidationError("'{0}' value entered is not numeric".format(value))
        
        if int(reservation.get_no_of_adults()) < 0 or int(reservation.get_no_of_children()) < 0:
            raise ValidationError("Number of children and number of adults must be greater than 0")
        
        if int(reservation.get_no_of_adults()) + int(reservation.get_no_of_children()) == 0:
            raise ValidationError("Must have guests to reserve a room")

        if int(reservation.get_no_of_week_nights()) < 0 or int(reservation.get_no_of_weekend_nights()) < 0:
            raise ValidationError("Number of week and weekend nights must be greater than 0")
        
        if int(reservation.get_no_of_week_nights()) + int(reservation.get_no_of_weekend_nights()) == 0:
            raise ValidationError("Must have more than 0 total nights to reserve a room")
        
        if reservation.get_type_of_meal_plan() not in ("Not Selected", "Meal Plan 1", "Meal Plan 2"):
            raise ValidationError("Invalid Meal plan choice")
        
        if reservation.get_required_car_parking_space() not in ("0", "1"):
            raise ValidationError("Invalid parking choice")
        
        if reservation.get_room_type_reserved() not in ('Room_Type 1', 'Room_Type 4'):
            raise ValidationError("Invalid room choice")

        if int(reservation.get_avg_price_per_room()) < 0:
            raise ValidationError("Price must be greater than 0")
        
        date_string = "{}-{}-{}".format(reservation.get_arrival_month(), reservation.get_arrival_date(), reservation.get_arrival_year())

        if not 1900 <= int(reservation.get_arrival_year()) <= 2100:
            raise ValidationError("Invalid Year")
        
        try:
            dt = datetime.strptime(date_string, '%m-%d-%Y')
        except ValueError:
            raise ValidationError("Invalid Date")
        
        if int(reservation.get_avg_price_per_room()) < 0:
            raise ValidationError("Average price value must be greater than 0")
        
        self.__reservation_database.update_reservation(reservation)
        return self.__reservation_dataframe.updateReservation(reservation)

    def get_reservation_info(self, id):
        return self.__reservation_dataframe.get_reservation(id)
    
    def get_meal_plan_distribution(self):
        return self.__reservation_database.get_meal_plan_distribution()
    
    def get_room_type_distribution(self):
        return self.__reservation_database.get_room_type_distribution()
    
    def get_all_reservation_details(self):
        return self.__reservation_database.get_all_reservation_details()
    
    def get_reservation_database(self, id):
        return self.__reservation_database.get_reservation_database(id)





