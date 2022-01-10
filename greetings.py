from datetime import datetime

def get_time_period():
    right_now = datetime.now()
    return right_now.hour

def determine_saying(time):
    if time >= 7 and time < 12:
        time_saying = "morning"
    elif time >= 12 and time < 17:
        time_saying = "afternoon"
    elif time >= 17 and time < 19:
        time_saying = "evening"
    else:
        time_saying = "night"
    return time_saying

def main():
    time_saying = "NOT YET SET."
    time = get_time_period()
    time_saying = determine_saying(time)
    
    print(f"Good {time_saying}, friend! How are you today?\n")

if __name__ == "__main__":
    main()