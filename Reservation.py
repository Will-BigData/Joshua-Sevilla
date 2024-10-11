import csv
import pandas as pd

class Reservation():
    def __init__(self, Booking_ID, no_of_adults, no_of_children, no_of_weekend_nights, no_of_week_nights, type_of_meal_plan, required_car_parking_space, room_type_reserved, arrival_year, arrival_month, arrival_date, avg_price_per_room):
        self.Booking_ID = Booking_ID
        self.no_of_adults = no_of_adults
        self.no_of_children = no_of_children
        self.no_of_weekend_nights = no_of_weekend_nights
        self.no_of_week_nights = no_of_week_nights
        self.type_of_meal_plan = type_of_meal_plan
        self.required_car_parking_space = required_car_parking_space
        self.room_type_reserved = room_type_reserved
        self.arrival_year = arrival_year
        self.arrival_month = arrival_month
        self.arrival_date = arrival_date
        self.avg_price_per_room = avg_price_per_room

    def arrival_time(self):
        return f'{self.arrival_month}/{self.arrival_date}/{self.arrival_year}'
    
    def number_of_guests(self):
        adult = int(self.no_of_adults)
        children = int(self.no_of_adults)
        return adult + children

    def number_of_days(self):
        return int(self.no_of_weekend_nights) + int(self.no_of_week_nights)
    
    def __str__(self):
        return f'Booking ID: {self.Booking_ID}, Arrival Date: {self.arrival_time()}, Number Of Guests: {self.number_of_guests()}, Number Of Days: {self.number_of_days()}, Meal Plan: {self.type_of_meal_plan}, Parking: {self.required_car_parking_space}, Room Type: {self.room_type_reserved}, Average Price: {self.avg_price_per_room}'
    
    def get_Booking_ID(self):
        return self.Booking_ID
    
    def get_no_of_adults(self):
        return self.no_of_adults
    
    def get_no_of_children(self):
        return self.no_of_children
    
    def get_no_of_weekend_nights(self):
        return self.no_of_weekend_nights
    
    def get_no_of_week_nights(self):
        return self.no_of_week_nights
    
    def get_type_of_meal_plan(self):
        return self.type_of_meal_plan
    
    def get_required_car_parking_space(self):
        return self.required_car_parking_space
    
    def get_room_type_reserved(self):
        return self.room_type_reserved

    def get_arrival_year(self):
        return self.arrival_year
    
    def get_arrival_month(self):
        return self.arrival_month
    
    def get_arrival_date(self):
        return self.arrival_date
    
    def get_avg_price_per_room(self):
        return self.avg_price_per_room
    
    def set_Booking_ID(self, Booking_ID):
        self.Booking_ID = Booking_ID
    
    def set_no_of_adults(self, no_of_adults):
        self.no_of_adults = no_of_adults
    
    def set_no_of_children(self, no_of_children):
        self.no_of_children = no_of_children
    
    def set_no_of_weekend_nights(self, no_of_weekend_nights):
        self.no_of_weekend_nights = no_of_weekend_nights
    
    def set_no_of_week_nights(self, no_of_week_nights):
        self.no_of_week_nights = no_of_week_nights
    
    def set_type_of_meal_plan(self, type_of_meal_plan):
        self.type_of_meal_plan = type_of_meal_plan
    
    def set_required_car_parking_space(self, required_car_parking_space):
        self.required_car_parking_space = required_car_parking_space

    def set_room_type_reserved(self, room_type_reserved):
        self.room_type_reserved = room_type_reserved
    
    def set_arrival_year(self, arrival_year):
        self.arrival_year = arrival_year
    
    def set_arrival_month(self, arrival_month):
        self.arrival_month = arrival_month
    
    def set_arrival_date(self, arrival_date):
        self.arrival_date = arrival_date

    def set_avg_price_per_room(self, avg_price_per_room):
        self.avg_price_per_room = avg_price_per_room




