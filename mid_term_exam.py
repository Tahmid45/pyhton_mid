
class Hall:
    def __init__(self, rows,cols,hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def entry_show(self,id, movie_name,time):
        tuple1 = (id, movie_name, time)
        self.show_list.append(tuple1)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range (self.rows)]

    def book_seats(self,id,r,c):
        if id in self.seats:
            if 0<=r<=self.rows and 0<=c<=self.cols:

                if self.seats[id][r][c]==0:
                    self.seats[id][r][c] = 1
                    print(f"({r}, {c}) Seat booked successfully")

                else:
                    print("Seat is not available")

            else:
                print("Invalid Position")

        else:
            print("Movie Id is wrong")
        
    def view_available_seats(self,id):
        if id in self.seats:
            print("Available Seats are here: ")
            for i in self.seats[id]:
                print(i)
        else:
            print("Invlid Id") 

    def view_show_list(self):
        for i in self.show_list:
            (movie_id,movie_name,time) = i
            print(f"Movie Id: {movie_id} Movie name: {movie_name} Time: {time}")

class Star_Cinema(Hall):
    hall_list = []
    def __init__(self,rows,cols,hall_no):
        super().__init__(rows,cols,hall_no)

    def entry_hall(self, hall):
        self.hall_list.append(hall)

m1 = Star_Cinema(5,5,1)
sangita = Hall(6,6,2)
m1.entry_hall(sangita)
m1.entry_show(101, "gravity", "2:00 pm")
m1.entry_show(102, "Paran", "6:00 pm2")


while True:
    print("1. View ALL Show Today")
    print("2. View Available Seats")
    print("3. BOOK Ticket")
    print("4. Exit")
    choice = int(input("Enter Option: "))
    if choice == 1:
        m1.view_show_list()
    elif choice == 2:
        show_id = int(input("Enter Show ID: "))
        m1.view_available_seats(show_id)
    elif choice == 3:
        id = int(input("Enter Show Id: "))
        

        num = int(input("Number of tickets: "))
        for i in range (num):
            j=1+i
            print(f"For seat no {j}: ")
            r = int(input("Enter row position of your seat: "))
            c = int(input("Enter col position of your seat: "))
            m1.book_seats(id,r,c)
    elif choice == 4:
        print("Thanks for using this system")
    else:
        print("Invalid Input")