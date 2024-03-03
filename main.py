import json 

# see if user time is bigger or lower than rqt and nqt times to tell user if he qualifies or not
def see_record(age, stroke, user_times, qualification_times):
    if age>=6 and age<12:
        key = "age_6_11"
    elif age>=12 and age<15:
        key = "age_12_14"
    elif age>=15 and age<17: 
        key = "age_15_16"
    elif age>=17:
        key = "age_17_"
    else:
        print("Your age is invalid, so we'll assign a random age to you.")
        key = "age_6_11"

    nqt_qualification_time = qualification_times[key][stroke]["nqt"]
    rqt_qualification_time = qualification_times[key][stroke]["rqt"]
    user_time = user_times[stroke]
    
    if user_time > rqt_qualification_time:
        print("You are not qualified")
    elif user_time <= rqt_qualification_time and user_time > nqt_qualification_time:
        print("You are qualified for the regionals")
    elif user_time <= nqt_qualification_time:
        print("You are qualified for the nationals!")
    else:
        print("We cannot process your time. ")


def add_record(time, stroke, user_times, user_times_file):
    #replacing or creating
    try:
        old_time = user_times[stroke]
    except:
        old_time = 3600

    if time <= old_time:
        user_times[stroke] = time
        print(user_times)
        with open(user_times_file, 'w') as file:
             json.dump(user_times, file)
    else:
        print("You already have better records")
    

user_times_file = input("Enter your file name: ")
#user_times_file = 'gab_times.json'
qualification_times_file = "qualification_times.json"

with open(qualification_times_file) as file:
    qualification_times = json.load(file)

with open(user_times_file) as file:
    user_times = json.load(file)

user_age = int(input("What is your age? Please you should be 6 and above. "))
answer = input("Would you like to ADD or SEE times and qualifications? ")

if answer.lower() == "add":
    stroke_to_add = input("What stroke and distance would you like to add? ")
    time_to_add = float(input("What was your time in this race? "))
    try:
        add_record(time_to_add, stroke_to_add, user_times, user_times_file)
    except:
        print("Couldn't add records, try again :/")       
elif answer.lower() == "see":
    stroke_to_check = input("What stroke are you competing on? ")
    try:
        see_record(user_age, stroke_to_check, user_times, qualification_times)    
    except:
        print("The stroke you entered may not be available in the qualification time records or yours, or another error has occured")
else:
    print("Invalid input. Enter either add or see.")






