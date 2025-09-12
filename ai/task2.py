class sru_student:
    """
    A class representing a student at SRU with attributes for name, roll number, hostel status, and fee payment status.
    Attributes:
        name (str): The name of the student.
        roll_no (str or int): The roll number of the student.
        hostel_status (str): The hostel accommodation status of the student.
        fee_paid (bool): Indicates whether the student's fee has been paid.
    Methods:
        __init__(name, roll_no, hostel_status):
            Initializes a new SRU student with the given name, roll number, and hostel status. Fee status is set to unpaid by default.
        fee_update(status):
            Updates the fee payment status of the student.
        display_details():
            Prints all details of the student including name, roll number, hostel status, and fee payment status.
    """
    # This sets up the student with their name, roll number, hostel status, and fee status
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False

    # This method updates whether the fee is paid or not
    def fee_update(self, status):
        self.fee_paid = status

    # This method prints out all the details of the student
    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Fee Paid:", "Yes" if self.fee_paid else "No")

# Ask the user for student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Hostel status (Yes/No): ")

# Make a student object with the details
student = sru_student(name, roll_no, hostel_status)

# Ask if the fee is paid and update it
fee_status = input("Has the fee been paid? (Yes/No): ")
student.fee_update(fee_status.lower() == "yes")

# Show all the details
student.display_details()
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Hostel status (Yes/No): ")

student = sru_student(name, roll_no, hostel_status)

fee_status = input("Has the fee been paid? (Yes/No): ")
student.fee_update(fee_status.lower() == "yes")

student.display_details()