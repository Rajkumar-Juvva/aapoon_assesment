
def giveMinutes(time):
    #This function takes time in format of "HH:MM" and returns an integer which represents minutes
    hours,minutes = map(int,time.split(':'))
    return hours*60+minutes

def giveTime(min):
    #This function takes minutes which is integer and returns a string in format of "HH:MM"
    hours = min//60
    minutes = min%60
    return f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}'

def calendar_matching(c1,db1,c2,db2,duration):
    totalMinutes = (24*60)+1

    #First we create a two arrays for two people, to represent availability
    #1 represents already engaged in other meeting
    #0 represents free availability
    person1 = [0]*totalMinutes
    person2 = [0]*totalMinutes


    for start,end in c1:
        #We mark start minute as 1 and end as -1
        #We use this as we move on time line
        person1[giveMinutes(start)]+=1
        person1[giveMinutes(end)]-=1
    
    for start,end in c2:
        person2[giveMinutes(start)]+=1
        person2[giveMinutes(end)]-=1
    
        
    db1Start = giveMinutes(db1[0])
    db1End = giveMinutes(db1[1])
    db2Start = giveMinutes(db2[0])
    db2End = giveMinutes(db2[1])

    res = []
    start = False
    startMinutes = 0
    durationMinutes = 0

    for minutes in range(24*60):
        if minutes>0:
            person1[minutes]+=person1[minutes-1]
            person2[minutes]+=person2[minutes-1]
        if db1Start<=minutes<db1End and db2Start<=minutes<db2End and person1[minutes]==0 and person2[minutes]==0:
            '''
                If current minutes is within dailyBounds of both people and both the people are free
                start flag represents whether the freetime started or not
                if already started, we increment durationMinutes
            '''
            if not start:
                start = True
                startMinutes = minutes
                durationMinutes = 1
            else:
                durationMinutes += 1
        else:
            '''
                If if condition is not satisfied.
                If start flag is True that means timeline is started and minutes durations is greater than the required duration
                We consider that duration and add that to res array
            '''

            if start and durationMinutes>=duration:
                res.append([giveTime(startMinutes),giveTime(minutes)])
                durationMinutes = 0
            start = False
    
    return res
                    

calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30
output = calendar_matching(calendar1,dailyBounds1,calendar2,dailyBounds2,meetingDuration)
print(output)

    

