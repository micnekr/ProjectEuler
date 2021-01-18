days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeap(year):
    return year%4==0 and year%400!=0

if __name__ == '__main__':
    count = 0
    recording=False

    mounth = 0
    day = 0
    dOfWeek=0
    year = 1900
    while True:
        dOfWeek=(dOfWeek+1)%7
        day+=1
        if day+1>days[mounth]:
            day=0
            mounth+=1
            #next year
            if mounth>11:
                mounth=0
                year+=1

        #print(day, mounth, year, "   ", dOfWeek, recording)


        if year==1901:
            recording=True

        if year>2000:
            print(count)
            break

        if recording and dOfWeek==6 and day==0:
            count+=1
            print(day, mounth, year, count)
        # if mounth==0 and day==22 and year==2019:
        #     print(dOfWeek+1)
        #     break
