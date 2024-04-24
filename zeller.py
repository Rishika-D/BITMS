# Python3 program to  Find the Day
# for a Date
 

def switch(h) :

    return {

        0 : "Saturday",

        1 : "Sunday",

        2 : "Monday",

        3 : "Tuesday",

        4 : "Wednesday",

        5 : "Thursday",

        6 : "Friday",

    }[h]
 

def Zellercongruence(day, month, year) :

    if (month == 1) :

        month = 13

        year = year - 1
 

    if (month == 2) :

        month = 14

        year = year - 1

    q = day

    m = month

    k = year % 100;

    j = year // 100;
    
    if year in range(1900,9999):
        
        h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j

        h = h % 7

        print(switch(h))
    else:
        print("Invalid")
month=int(input("enter the month"))
day=int(input("enter the date"))
year=int(input("enter the year"))
#if (month<0 and month>12) and (day<0 or day>31) and (year<1900 or year>9999):
if (month<0 or month>12) or (day<0 or day>31) or (year<1900 or year>9999):
    print("Invalid format")
else:
    Zellercongruence(day,month,year)
