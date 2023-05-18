
def add_time(start, duration, dayOfWeekIn = False):

    #Partitioning the inputted tuples to get necessary information for calculations 
    startHour = int(start.partition(":")[0]);
    startMin = int(start.partition(" ")[0].partition(":")[2]);
    meridian = str(start.partition(" ")[2]);
    originalMeridian = str(start.partition(" ")[2]);
    durationHour = int(duration.partition(":")[0]);
    durationMin = int(duration.partition(":")[2]);

    #Defining a dicitonary and list for the days of the week
    dayOfWeekDict = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6};
    dayOfWeekArray = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];    
    
    #Finding the final result minute
    resultMin = startMin + durationMin;
    if (resultMin >= 60):
        durationHour += 1;
        resultMin = resultMin % 60;
    else:
        resultMin = resultMin;

    if resultMin >= 10:
        resultMin = resultMin;
    else:
        resultMin = "0" + str(resultMin);
    
    resultHour = (startHour + durationHour) % 12; 

    #Finding the correct meridian    
    numMeridianChanges = int((startHour + durationHour) / 12);
    meridianRef = numMeridianChanges % 2;

    if meridianRef == 1 and meridian == "AM":
        meridian = "PM";
    elif meridianRef == 1 and meridian == "PM":
        meridian = "AM";
    elif meridianRef == 0:
        meridian = meridian;
    
    #Finding the final result hour and number of days past
    numDays = int(durationHour / 24);
    remainderHours = durationHour % 24;
    
    if originalMeridian == "PM" and meridian == "AM":
        numDays += 1;
    
    if resultHour == 0:
        resultHour = 12;
    else:
        resultHour = resultHour;

    new_time = str(resultHour) + ":" + str(resultMin) + " " + str(meridian);

    #Compute returned function output
    if dayOfWeekIn:
        dayOfWeekIn = dayOfWeekIn.lower();
        count = int((dayOfWeekDict[dayOfWeekIn]) + numDays) % 7;
        dayOfWeekOut = dayOfWeekArray[count];
        
        new_time = str(resultHour) + ":" + str(resultMin) + " " + str(meridian) + ", " + str(dayOfWeekOut);
    
    if numDays == 1:
        new_time += " " + "(next day)";
    elif numDays > 1:
        new_time += " (" + str(numDays) + " days later)";
    
    return new_time;


