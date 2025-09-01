def classify_age(age):
    match True:
        case _ if age < 0:
            print("Invalid age")
        case _ if age <= 12:
            print("Child")
        case _ if age <= 17:
            print("Teenager")
        case _ if age <= 64:
            print("Adult")
        case _:
            print("Senior")
classify_age(25)