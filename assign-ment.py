Name=input("Enter your name")
Age=int(input("Enter your age"))
current_year=2022
def getyear():
    date_of_birth=current_year-Age
    print("Hello, ",Name,"You were born in the year",date_of_birth)
getyear()
