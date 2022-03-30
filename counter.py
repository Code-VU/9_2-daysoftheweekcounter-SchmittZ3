
def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")   
    x = open(file_name)
    days = dict()
    for line in x:
        y = line.split()
        if len(y) < 3 or y[0] != 'From':
            continue
        else:
            if y[2] not in days:
                days[y[2]] = 1
            else:
                days[y[2]] += 1
    print(days)

    
     # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
countDayOfTheWeek()