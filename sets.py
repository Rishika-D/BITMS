'''states={"Goa","MP,"UP","Tamil Nadu","Karnataka","Mumbai","Kashmir"}
print(states)
print(type(states))
print("looping through the set elements...")
for i in states:
    print(i)'''
    


'''#empty curly braces will create a dictionary
set3={}
print(type(set3))'''

'''#empty
set4()
print(type(set4))'''



'''#a set is unordered
set5={10,20,30,40,50,80,90,90,100}
print(set5)'''


'''#printing and modifying the sets
districts=set(["ooty","banglore","manglore","ballari","udupi","chennai"])
print("\nprinting the original set...")
print(districts)
print("\nupdating the original set")
districts.update(["kovai","kanyakumari","madhurai","trichy"]);
print("\nprinting the modified sets")
print(districts)'''


'''days1={"monday","tuesday","wednesday","thursday","sunday"}
days2={"friday","saturday","sunday"}
print(days1|days2) #printing the union of set
print(days1.union(days2))#spliting the union of the set
#output:{'tuesday', 'friday', 'sunday', 'monday', 'saturday', 'wednesday', 'thursday'}
#{'tuesday', 'friday', 'monday', 'sunday', 'saturday', 'wednesday', 'thursday'}'''


'''days1={"monday","tuesday","wednesday","thursday","sunday"}
days2={"friday","saturday","sunday"}
print(days1&days2)#splits the intersection of 2 sets
#output:{'sunday'}

days1={"monday","tuesday","wednesday","thursday","sunday"}
days2={"friday","saturday","sunday"}
print(days1.difference(days2))#prints the difference of the sets
#output:{'thursday', 'monday', 'wednesday', 'tuesday'}

days1={"monday","tuesday","wednesday","thursday","sunday"}
days2={"friday","saturday","sunday"}
print(days1-days2)#days will b substracted when they are same
#output:{'monday', 'tuesday', 'wednesday', 'thursday'}

days1={"monday","tuesday","wednesday","thursday","sunday"}
days2={"friday","saturday","sunday"}
print(days2-days1)
# output:{'saturday', 'friday'}'''


'''a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a^b#common elemets are deleted
print(c)

a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a.symmetric_difference(b)#common elemets are deleted
print(c)'''




'''days1={"monday","tuesday","wednesday","thursday"}
days2={"monday","tuesday"}
days3={"mondaydays1","tuesday","friday"}

# days1 is the superset of days2 hence it will print true.
print(days1>days2)

#prints fals since days1 is not the subset of days2.
print(days1<days2)

#prints false sice days2 and days3 are not eqivalent.
print(days2==days3)'''