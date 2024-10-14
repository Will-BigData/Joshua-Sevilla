from ReservationDataFrame import ReservationDataFrame as rd
from CL_Controller import cl_Controller
from ReservationService import ValidationError
from api_controller import api_controller
from ReservationDatabase import reservation_database
from flask import Flask

def main():
    app = Flask(__name__)

    interface_selection = input('Select interface to use. [a]pi or [c]ommand line: ')
    selection = ''
    data = rd()
    database = reservation_database(user='root', password='MonkeysInc7!',
                                host='127.0.0.1',
                                database='project_0')

    if interface_selection == 'c':

        command_controller = cl_Controller(data, database)
        command_controller.start_up_database()

        while(selection != 'e'):
            selection = input("Select feature: [c]reate reservation, [u]pdate reservation, [d]elete reservation, [s]elect reservation, [q]ueries, [e]xit: ")
            match selection:
                #Create
                case 'c':
                    try:
                        command_controller.create_reservation()
                    except ValidationError as e:
                        print(e.message + " try again.")

                #Update
                case 'u':
                    try:
                        df = command_controller.update_reservation()
                        if df.empty:
                            print('Not found')
                        else:
                            print(df)
                    except ValidationError as e:
                        print(e.message + " try again.")

                #Delete
                case 'd':
                    print(command_controller.delete_reservation())
                #Select
                case 's':
                    df = command_controller.get_reservation()
                    if df.empty:
                            print('Not found')
                    else:
                        print(df) 
                    
                #Exit
                case 'q':
                    query_selection = input('Input Query Selection. [M]eal Plan, [R]oom type, [S]ummary, [D]etails of Reservation: ')
                    if query_selection == 'M':
                        print(command_controller.meal_plan_distribution())
                    elif query_selection == 'R':
                        print(command_controller.get_room_type_distribution())
                    elif query_selection == 'S':
                        print(command_controller.get_all_reservation_details())
                    elif query_selection == 'D':
                        print(command_controller.get_reservation_database())
                    else:
                        print('Not an option. Try Again.')

                case 'e':
                    break
                case _:
                    print("Not an option select again")
    elif interface_selection == 'a':

        controller = api_controller(data, database)
        controller.start_up_database()

        @app.route('/reservation/create', methods=['POST'])
        def create_reservation():
            try:
                reservation = controller.create_reservation()
                return reservation.to_dict(orient='records')
            except ValidationError as e:
                return e.message
            
        @app.route('/reservation/<id>', methods=['GET'])
        def get_reservation(id: str):
            reservation = controller.get_reservation(id)
            if reservation.empty:
                return 'Not found'
            else:
                return reservation.to_dict(orient='records')
            
        @app.route('/reservation/update/<id>', methods=['PATCH'])
        def update_reservation(id: str):
            try:
                reservation = controller.update_reservation(id)

                if reservation.empty:
                    return 'Not found'
                else:
                    return reservation.to_dict(orient='records')
                
            except ValidationError as e:
                return e.message

        @app.route('/reservation/delete/<id>', methods=['DELETE'])
        def delete_reservation(id: str):
            return controller.delete_reservation(id)

        @app.route('/reservation/query/meal-plans', methods=['GET'])
        def get_meal_plan_distribution_reservation():
            return controller.meal_plan_distribution().to_dict('records')
        
        @app.route('/reservation/query/room-type', methods=['GET'])
        def get_room_type_distribution_reservation():
            return controller.get_room_type_distribution().to_dict('records')

        @app.route('/reservation/query/reservations', methods=['GET'])
        def get_reservation_details():
            return controller.get_all_reservation_details().to_dict('records')
        
        @app.route('/reservation/query/reservations/<id>', methods=['GET'])
        def get_reservation_database(id: str):
            reservation = controller.get_reservation_database(id)
            if reservation.empty:
                return 'Not found'
            else:
                return reservation.to_dict(orient='records')

        app.run()
    else:
        while interface_selection not in ('a', 'c'):
            print('Invalid Choice.')
            interface_selection = input('Select interface to use. [a]pi or [c]ommand line: ')


if __name__ == '__main__':
    main()