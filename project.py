def say_hello():
    print("\nHello welcome to the console application")
    print("\nThis is a simple message")
def present_value_of_ordinary_annuity():
    print("\nSimple Calculation")
    class OrdinaryAnnuity:
        def __init__(self, rate, periods):
            """
         Initialize the OrdinaryAnnuity class.

            :param rate: Interest rate per period (as a decimal, e.g., 0.05 for 5%)
            :param periods: Number of periods
            """
            self.rate = rate
            self.periods = periods

        def present_value_factor(self):
            """
            Calculate the present value factor for an ordinary annuity.

            :return: Present value factor
            """
            if self.rate == 0:
                return self.periods
            return (1 - (1 + self.rate) ** -self.periods) / self.rate

        def present_value(self, payment):
            """
            Calculate the present value of an ordinary annuity.

            :param payment: Amount of each annuity payment
            :return: Present value of the annuity
            """
            pv_factor = self.present_value_factor()
            return round(payment * pv_factor, 2)


    # Example usage
    payment = float(input("Enter the annuity payment amount: "))
    rate = float(input("Enter the interest rate (as a decimal, e.g., 0.05 for 5%): "))
    periods = int(input("Enter the number of periods: "))

    annuity = OrdinaryAnnuity(rate, periods)
    pv = annuity.present_value(payment)
    print(f"The present value of the ordinary annuity is: {pv}")
def future_value_of_ordinary_annuity():
    print("\nSimple Calculation")
    class OrdinaryAnnuityFutureValue:
        def __init__(self, rate, periods):
            """
            Initialize the OrdinaryAnnuity class.

            :param rate: Interest rate per period (as a decimal, e.g., 0.05 for 5%)
            :param periods: Number of periods
            """
            self.rate = rate
            self.periods = periods

        def future_value_factor(self):
            """
            Calculate the future value factor for an ordinary annuity.

            :return: Future value factor
            """
            if self.rate == 0:
                return self.periods
            return ((1 + self.rate) ** self.periods - 1) / self.rate

        def future_value(self, payment):
            """
            Calculate the future value of an ordinary annuity.

            :param payment: Amount of each annuity payment
            :return: Future value of the annuity
            """
            fv_factor = self.future_value_factor()
            return round(payment * fv_factor, 2)


    # Example usage
    payment = float(input("Enter the annuity payment amount: "))
    rate = float(input("Enter the interest rate (as a decimal, e.g., 0.05 for 5%): "))
    periods = int(input("Enter the number of periods: "))

    annuity = OrdinaryAnnuityFutureValue(rate, periods)

    fv = annuity.future_value(payment)
    print(f"The future value of the ordinary annuity is: {fv}")

def exit_application():
    print("\nexiting application....")
    print("Goodbye!")

def main_menu():
    while True:
        #display menu
        print("\n===================================")
        print("     Console Application Menu")
        print("===================================")
        print("1.Say Hello")
        print("2.Present Value of ordinary annuity")
        print("3.Present Value of ordinary annuity")
        print("4.Exit")
        print("===================================")
        choice =input("select an option: ")
        if choice == "1":
            say_hello()
        elif choice == "2":
            present_value_of_ordinary_annuity()
        elif choice == "3":
            future_value_of_ordinary_annuity()
        elif choice == "4":
            exit_application()
            break
        else:
            print("\nInvalid option, please try again")

if __name__ == "__main__":
    main_menu()