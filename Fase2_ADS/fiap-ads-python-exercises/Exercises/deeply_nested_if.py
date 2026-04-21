# Check whether the heart rate is within the appropriate range.
# The program asks the user for age and beats per minute (BPM),
# then checks whether the result is within, above, or below the expected range.

# AGE ______________________ BPM
# Up to 2 years old         - 120 to 140
# From 8 to 17 years old    - 80 to 100
# Sedentary adult           - 70 to 80
# Older adults              - 50 to 60

print("""
__________________________________
HEART RATE CHECKER
__________________________________
""")

age = int(input("Please enter your AGE: "))
bpm = int(input("Please enter your HEART RATE (BPM): "))

if age <= 2:
    if bpm >= 120:
        if bpm <= 140:
            print("Heart rate is WITHIN the normal range for the given age.")
        else:
            print("Heart rate is ABOVE the recommended range for this age.")
    else:
        print("Heart rate is BELOW the recommended range for this age.")
elif age >= 8:
    if age <= 17:
        if bpm >= 80:
            if bpm <= 100:
                print("Heart rate is WITHIN the normal range for the given age.")
            else:
                print("Heart rate is ABOVE the recommended range for this age.")
        else:
            print("Heart rate is BELOW the recommended range for this age.")
    if age >= 18:
        if age <= 60:
            if bpm >= 70:
                if bpm <= 80:
                    print("Heart rate is WITHIN the normal range for the given age.")
                else:
                    print("Heart rate is ABOVE the recommended range for this age.")
            else:
                print("Heart rate is BELOW the recommended range for this age.")
        else:
            if bpm >= 50:
                if bpm <= 60:
                    print("Heart rate is WITHIN the normal range for the given age.")
                else:
                    print("Heart rate is ABOVE the recommended range for this age.")
            else:
                print("Heart rate is BELOW the recommended range for this age.")