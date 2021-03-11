msg = 'Invalid Value'

def get_duration_string(minutes, seconds):
    if((minutes < 0) or (seconds < 0 or seconds > 59)):
        return msg
    hours = minutes / 60
    remaining_minutes = minutes % 60
    hours = int(hours)
    minutes = int(minutes)
    return str(minutes) + " minutes and " + str(seconds) + " seconds equal to " + str(hours) + "h " + str(remaining_minutes) + "m " + str(seconds) + "s"

def get_duration_string1(seconds):
    if seconds < 0:
        return msg
    minutes = seconds / 60
    remaining_seconds = seconds % 60
    return get_duration_string(minutes, remaining_seconds)

print(get_duration_string(61, 30))
print(get_duration_string1(3600))