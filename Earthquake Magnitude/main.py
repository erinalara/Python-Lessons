
def get_magnitude(number):              # This function gets the magnitude of an earthquake
    magnitude = 0
    while magnitude <= 0:               # Validates magnitude
        magnitude = float(input("Please enter the magnitude of earthquake " + str(number)+'. '))    # User input for magnitude
    return magnitude

def compare_magnitudes(magnitude1,magnitude2):      # Function that compares the two magnitudes
    strength = (10** (1.5 * (max(magnitude1,magnitude2) - min(magnitude1,magnitude2))))     # Calculates strength of the two magnitudes
    return format(strength, '.1f')      # Formats strength

def get_run_again():        # User decides if they want to compare 2 more earthquakes
    user_input = int(input("Try again? Type 1 if yes. "))   
    if user_input == 1:     # Loops back to main function
        main()
    
def main():         # Main function
    magnitude1 = get_magnitude(1)   # First magnitude of first earthquake, calls first function
    magnitude2 = get_magnitude(2)   # Second magnitude of second earthquake, calls first function
    print("An earthquake of", max(magnitude1,magnitude2), "is", compare_magnitudes(magnitude1,magnitude2), "times more powerful than an earthquake of", min(magnitude1,magnitude2), ".")            # Prints comparison of two earthquakes using second function
    get_run_again()     # Runs third function if user wants to compare two more earthquakes
    
main()      # Calls main function
    




        