import tkinter as tk
import datetime

admin = {'admin': 'admin'}
manager = {'manager': 'manager'}
standard = {'standard': 'standard'}
scheduled = {'AGENTX44': ["10:10", 'Manila', "Delayed"], 'ADO2354': ['5:30', 'Cebu City', 'Delayed'],
             'ASIA1231': ['1:49', 'Boracay', 'Scheduled'], 'AGENT221': ['7:40', 'Cagayan De Oro', 'Scheduled'],
             'ASIAPACIFIC': ['2:50', 'Albay', 'Delayed'], 'AB3452': ['9:320', 'Laguna', 'Scheduled'],
             'LA3452': ['8:40', 'Dumaguete City', 'Scheduled']}
cancelled = {'ASIA3456': ["3:00", "Marawi City", "Cancelled"]}





def update():
    scheduled_update = tk.Tk()
    scheduled_update.title("Update/Add A Flight")
    tk.Label(master=scheduled_update, text="Enter The Flight Number").grid(row=1, column=0)
    number_of_flight = tk.Entry(master=scheduled_update)
    number_of_flight.grid(row=1, column=1)

    def update_btn1():
        if number_of_flight.get() not in scheduled:
            scheduled[number_of_flight.get()] = ["", "", ""]
        tk.Label(master=scheduled_update, text="Enter Departure Time").grid(row=3, column=0)
        departure_time = tk.Entry(master=scheduled_update)
        departure_time.grid(row=3, column=1)
        tk.Label(master=scheduled_update, text="Enter Status").grid(row=4, column=0)
        stat = tk.Entry(master=scheduled_update)
        stat.grid(row=4, column=1)
        tk.Label(master=scheduled_update, text="Enter Destination").grid(row=5, column=0)
        destination_place = tk.Entry(master=scheduled_update)
        destination_place.grid(row=5, column=1)

        def update_btn2():
            if departure_time.get() != "":
                scheduled[number_of_flight.get()][0] = departure_time.get()
            if stat.get() != "":
                scheduled[number_of_flight.get()][2] = stat.get()
            if destination_place.get() != "":
                scheduled[number_of_flight.get()][1] = destination_place.get()
            update_root = tk.Tk()
            update_root.title("Successfully Updated!")
            tk.Label(master=update_root, text="Successfully Updated!!").grid(row=0, column=0)
            scheduled_update.destroy()

        tk.Button(master=scheduled_update, text="Confirm", command=update_btn2).grid(row=6, column=1)

    tk.Button(master=scheduled_update, text="Confirm", command=update_btn1).grid(row=2, column=1)
    scheduled_update.mainloop()



def admin_main_features():  # admin control panel
    def switch_users_admin():
        admin_main_scheduled.destroy()
        login()

    admin_main_scheduled = tk.Tk()
    admin_main_scheduled.title("Admin Control Panel")
    tk.Button(master=admin_main_scheduled, text="View The Details Of Flights", command=viewing_flights).grid(row=1,                                                                                                  column=1)
    tk.Button(master=admin_main_scheduled, text="Switch User", command=switch_users_admin).grid(row=2, column=1)
    tk.Button(master=admin_main_scheduled, text="Exit The Program", command=exit).grid(row=6, column=1)
    tk.Button(master=admin_main_scheduled, text="Add A Flight details", command=update).grid(row=3, column=1)


def viewing_flights():  # viewing flights
    can = 0
    ret = 1
    display = tk.Tk()
    display.title("View Details Of Flights")
    tk.Label(master=display, text="Flight Number--------ETA--------Destination-------Status").grid(row=1, column=0)
    for i in scheduled:
        can += 1
        ret += 1
        tk.Label(master=display,
                 text=(i, "-------", scheduled[i][0], "--------", scheduled[i][1], "--------", scheduled[i][2])).grid(
            row=ret, column=0)
    for i in cancelled:
        can += 1
        ret += 1
        tk.Label(master=display,
                 text=(i, "-------", cancelled[i][0], "--------", cancelled[i][1], "--------", cancelled[i][2])).grid(
            row=ret, column=0)



def login():  # login function
    def user_verification():
        def password_verification():
            pas = password.get()
            if check == 1:
                if admin[a] == pas:
                    login_sched.destroy()
                    admin_main_features()
                  
                else:
                    admin3 = tk.Tk()
                    admin3.title("Wrong Password!")
                    tk.Label(master=admin3, text="Wrong Password! Please Try Again!").grid(row=1, column=1)

            elif check == 2:
                if manager[a] == pas:
                    login_sched.destroy()
                   
                else:
                    admin3 = tk.Tk()
                    admin3.title("Wrong Password!")
                    tk.Label(master=admin3, text="Wrong Password! Please Try Again!").grid(row=1, column=1)
            elif check == 3:
                if standard[a] == pas:
                    login_sched.destroy()

                else:
                    admin3 = tk.Tk()
                    admin3.title("Wrong Password!")
                    tk.Label(master=admin3, text="Wrong Password! Please Try Again!").grid(row=1, column=1)

        a = username.get()

        if not (a in admin or a in manager or a in standard):
            admin1 = tk.Tk()
            admin1.title("Wrong Username!")
            tk.Label(master=admin1, text="Username Not Found. Please Try Again!").grid(row=1, column=1)
        else:
            if a in manager:
                check = 2
            elif a in admin:
                check = 1
            elif a in standard:
                check = 3

            tk.Label(master=login_sched, text="Enter Your Password").grid(row=2, column=0)
            password = tk.Entry(master=login_sched, show='*')
            password.grid(row=2, column=1)
            admin3 = tk.Button(master=login_sched, text="Confirm Password", width=25,
                               command=password_verification).grid(row=2, column=2)

    login_sched = tk.Tk()
    login_sched.title("Login")
    tk.Label(master=login_sched, text="").grid(row=5, column=1)
    image = tk.PhotoImage(file="icon.png")
    no = tk.Label(master=login_sched, image=image).grid(row=0, column=1)
    tk.Label(master=login_sched, text="Enter Your Username").grid(row=1, column=0)
    username = tk.Entry(master=login_sched)
    username.grid(row=1, column=1)
    asking = tk.Button(master=login_sched, text="Confirm Username", width=25, command=user_verification).grid(row=1,
                                                                                                              column=2)
    login_sched.mainloop()

login()
def user_management():
    def adding_flight():
        def adding_admin():
            def admin_username():
                def admin_username_back():
                    password = passwrd.get()
                    admin[user] = password
                    root = tk.Tk()
                    root.title("Success")
                    tk.Label(master=root, text="Admin Successfully Added!").grid(row=1, column=1)

                user = username.get()
                if user in admin or user in manager or user in standard:
                    root = tk.Tk()
                    root.title("Username Already Exists!")
                    tk.Label(master=root, text="Username Already Exists! Please Try Again").grid(row=1, column=1)

                    system.destroy()
                else:
                    tk.Label(master=system, text="Enter the Password").grid(row=2, column=0)
                    passwrd = tk.Entry(master=system, show='*')
                    passwrd.grid(row=2, column=1)
                    tk.Button(master=system, text="Confirm Password", command=admin_username_back, width=25).grid(row=2,
                                                                                                                  column=3)

            system = tk.Tk()
            system.title("Add An Admin")
            tk.Label(master=system, text="Enter the Username").grid(row=1, column=0)
            username = tk.Entry(master=system)
            username.grid(row=1, column=1)
            admin3 = tk.Button(master=system, text="Confirm Username", width=25, command=admin_username).grid(row=1,
                                                                                                              column=3)


