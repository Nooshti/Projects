from hash_table import DSAHashTable
import timeit as t

try:    # demonstrates collision handling, correct insertion, duplicate insertion
        # prints load factor after every 10 inserts
        # validates input for
        # 22 passengers and 23 drivers inserted
        # shows successful searches and misses
        # shows successful deletions and attempts to delete non existent record
        # shows successful searches and attempts to search non existent and deleted records
    start = t.default_timer()
    table = DSAHashTable(46)    # a size of 46 was given on purpose to trigger resize once table > 70% full
    print("*" * 80)
    print("Module 2: Hash-Based Passenger and Driver Lookup Test")
    print("*" * 80)

    print("INSERTING RECORDS\n")
    start = t.default_timer()
    table.read_csv("passenger_driver_records.csv")  # puts every line into hash table slot
        # test for duplicate
    table.put(14495655, "Passenger", "Sofia Bonfiglio", "Mall", 4)

    end = t.default_timer()
    print(f"Time taken to insert: {round(end-start, 10)} seconds")
    print("DELETING RECORDS\n")
    start_1 = t.default_timer()
    table.remove(14495655)  # deleted Passenger Sofia Bonfiglio
    table.remove(14210394)  # deleted Driver Lonnie Traxson
    table.remove(39390000)  # trying to delete non-exiting key
    end_1 = t.default_timer()
    print(f"Time taken to delete: {round(end_1 - start_1, 10)} seconds")
    table.save_csv("test_module2.csv")
    print("\nSEARCHING RECORDS\n")
    start_2 = t.default_timer()
    print(table.get(14147356))     # Passenger  Elinor Raco (successful search)
    print(table.get(14770506))     # Passenger Christian Durall (successful search)
    print(table.get(9475))  # trying to search non-exiting key  (unsuccessful search)
    print(table.get(14495655))  # deleted Passenger Sofia Bonfiglio (show effect of searching for a deleted record)
    end_2 = t.default_timer()
    print(f"Time taken to search: {round(end_2 - start_2, 10)} seconds")
        # displays wrong record type
    table.put(11234087, "Seller", "Chloe Cheng", "Harbor", 1)
except Exception as err:
    print(err)

try:
    table_10 = DSAHashTable(20) # 3 different tables
    table_30 = DSAHashTable(60)
    table_45 = DSAHashTable(90)
    print()
    print("*" * 80)
    print("Performance Analysis")
    print("*" * 80)
    print()
    print("INSERTING RECORDS\n")
    print("INSERTING 10 RECORDS\n")
    start_3 = t.default_timer()

    table_10.put(14495655, "Passenger", "Sofia Bonfiglio", "Mall",4)
    table_10.put(14224671, "Passenger", "Ashlee Capellan","School",5)
    table_10.put(14707100,"Passenger","Dona Mcinnes","Suburbs",3)
    table_10.put(14644633,"Passenger","Maricela Landreneau","Park",1)
    table_10.put(14147356,"Passenger","Elinor Raco","Supermarket",2)
    table_10.put(14210394,"Driver","Lonnie Traxson","Park","Busy")
    table_10.put(14088484,"Driver","Khalilah Dittrick","Zoo","Offline")
    table_10.put(14481609,"Passenger","Amal Moznett","Mall",4)
    table_10.put(14778665,"Passenger","Cornell Uhri","School",2)
    table_10.put(14905261,"Driver","Yuriko Stimer","Supermarket","Available")
    lf = table_10.get_load_factor()
    lf = round(lf * 100, 2)
    print(f"The load factor every 10 inserts is {lf}%")
    end_3 = t.default_timer()

    print("INSERTING 30 RECORDS\n")
    start_4 = t.default_timer()

    table_30.put(14495655, "Passenger", "Sofia Bonfiglio", "Mall", 4)
    table_30.put(14224671, "Passenger", "Ashlee Capellan", "School", 5)
    table_30.put(14707100, "Passenger", "Dona Mcinnes", "Suburbs", 3)
    table_30.put(14644633, "Passenger", "Maricela Landreneau", "Park", 1)
    table_30.put(14147356, "Passenger", "Elinor Raco", "Supermarket", 2)
    table_30.put(14210394, "Driver", "Lonnie Traxson", "Park", "Busy")
    table_30.put(14088484, "Driver", "Khalilah Dittrick", "Zoo", "Offline")
    table_30.put(14481609, "Passenger", "Amal Moznett", "Mall", 4)
    table_30.put(14778665, "Passenger", "Cornell Uhri", "School", 2)
    table_30.put(14905261, "Driver", "Yuriko Stimer", "Supermarket", "Available")
    lf = table_30.get_load_factor()
    lf = round(lf * 100, 2)
    print(f"The load factor every 10 inserts is {lf}%")
    table_30.put(14393910,"Passenger","Cody Mcmartin","Suburbs",3)
    table_30.put(14799737,"Passenger","Katy Vacek","Suburbs",2)
    table_30.put(14431660,"Passenger","Mathew Mercedes","Suburbs",1)
    table_30.put(14541837,"Passenger","Karina Rossin","Zoo",3)
    table_30.put(14593654,"Passenger","Mathew Milian","Zoo",1)
    table_30.put(14492026,"Passenger","Christian Mullarkey","Park",2)
    table_30.put(14397374,"Passenger","Esmeralda Radovich","Church",1)
    table_30.put(14824429,"Passenger","Nelson Tooker","Park",5)
    table_30.put(14929292,"Passenger","Neil Brabant","Park",1)
    table_30.put(14786148,"Passenger","Clinton Blumer","Church",2)
    lf = table_30.get_load_factor()
    lf = round(lf * 100, 2)
    print(f"The load factor every 10 inserts is {lf}%")
    table_30.put(14354152,"Driver","Max Plain","Church","Available")
    table_30.put(14338567,"Driver","Earnestine Croswell","Park","Busy")
    table_30.put(14277290,"Driver","Clayton Ricard","Suburbs","Offline")
    table_30.put(14476919,"Driver","Ted Tallmadge","Park","Available")
    table_30.put(14032266,"Driver","Kelly Cheatam","Mall","Available")
    table_30.put(14094113,"Driver","Jessie Leandro","School","Available")
    table_30.put(14490422,"Driver","Guy Kadel","Mall","Busy")
    table_30.put(14650254,"Driver","Althea Warring","University","Busy")
    table_30.put(14355490,"Driver","Tania Mogensen","Suburbs","Offline")
    table_30.put(14478629,"Driver","Ted Makuch","School","Available")
    lf = table_30.get_load_factor()
    lf = round(lf * 100, 2)
    print(f"The load factor every 10 inserts is {lf}%")
    end_4 = t.default_timer()

    print("INSERTING 45 RECORDS\n")
    start_5 = t.default_timer()
    table_45.read_csv("passenger_driver_records.csv")  # puts every line into hash table slot
    end_5 = t.default_timer()

    duration_10 = end_3 - start_3
    duration_30 = end_4 - start_4
    duration_45 = end_5 - start_5
    print(f"Time taken to insert 10 records: {round(duration_10, 10)} seconds")
    print(f"Time taken to insert 30 records: {round(duration_30, 10)} seconds")
    print(f"Time taken to insert 45 records: {round(duration_45, 10)} seconds\n")
    if round(duration_10, 2) == round(duration_30, 2) == round(duration_45, 2):
        print("Time Complexity for insertion is O(1) since the time taken are almost the same\n")

    print("DELETING RECORDS")
    print("DELETING 5 RECORDS\n")
    start_6 = t.default_timer()
    table_10.remove(14495655)  # Passenger,Sofia Bonfiglio
    table_10.remove(14224671)  # Passenger,Ashlee Capellan
    table_10.remove(14707100)  # Passenger,Dona Mcinnes
    table_10.remove(14644633)  # Passenger,Maricela Landreneau
    table_10.remove(14147356)  # Passenger,Elinor Raco
    end_6 = t.default_timer()
    duration_5 = end_6 - start_6
    print("DELETING 10 RECORDS\n")
    start_7 = t.default_timer()
    table_30.remove(14210394)  # Driver,Lonnie Traxson
    table_30.remove(14088484)  # Driver,Khalilah Dittrick
    table_30.remove(14481609)  # Passenger,Amal Moznett
    table_30.remove(14778665)  # Passenger,Cornell Uhri
    table_30.remove(14905261)  # Driver,Yuriko Stimer
    table_30.remove(14393910)   # Passenger,Cody Mcmartin
    table_30.remove(14799737)   # Passenger,Katy Vacek
    table_30.remove(14431660)   # Passenger,Mathew Mercedes
    table_30.remove(14541837)   # Passenger,Karina Rossin
    table_30.remove(14593654)   # Passenger,Mathew Milian
    end_7 = t.default_timer()
    duration_10 = end_7 - start_7

    print("DELETING 20 RECORDS\n")
    start_8 = t.default_timer()
    table_45.remove(14397374)   # Passenger,Esmeralda
    table_45.remove(14824429)   # Passenger,Nelson Tooker
    table_45.remove(14929292)   # Passenger,Neil Brabant
    table_45.remove(14786148)   # Passenger,Clinton Blumer
    table_45.remove(14973358)   # Passenger,Julio Degroat 16
    table_45.remove(14557200)   # Passenger,Elinor Greig
    table_45.remove(14472268)   # Passenger,Malinda Dodgen
    table_45.remove(14359796)   # Passenger,Mathew Eslick
    table_45.remove(14770506)   # Passenger,Christian Durall
    table_45.remove(14354152)   # Driver,Max Plain
    table_45.remove(14338567)   # Driver,Earnestine Croswell
    table_45.remove(14277290)   # Driver,Clayton Ricard
    table_45.remove(14476919)   # Driver,Ted Tallmadge
    table_45.remove(14032266)   # Driver,Kelly Cheatam
    table_45.remove(14094113)   # Driver,Jessie Leandro
    table_45.remove(14490422)   # Driver,Guy Kadel
    table_45.remove(14650254)   # Driver,Althea Warring
    table_45.remove(14355490)   # Driver,Tania Mogensen
    table_45.remove(14478629)   # Driver,Ted Makuch
    table_45.remove(14827960)   # Driver,Katy Callier
    end_8 = t.default_timer()
    duration_20 = end_8 - start_8
    print(f"\nTime taken to delete 5 records: {round(duration_5, 10)} seconds")
    print(f"Time taken to delete 10 records: {round(duration_10, 10)} seconds")
    print(f"Time taken to delete 20 records: {round(duration_20, 10)} seconds\n")
    if round(duration_5, 2) == round(duration_10, 2) == round(duration_20, 2):
        print("Time Complexity for deletion is O(1) since the time taken are almost the same")

    print("\nSEARCHING RECORDS")
    print("SEARCHING 5 RECORDS\n")
    start_9 = t.default_timer()
    # searches key and returns whole entry
    print(table_10.get(14210394)) # Driver,Lonnie Traxson
    print(table_10.get(14088484))  # Driver,Khalilah Dittrick
    print(table_10.get(14481609))  # Passenger,Amal Moznett
    print(table_10.get(14778665))  # Passenger,Cornell Uhri
    print(table_10.get(14905261))  # Driver,Yuriko Stimer
    end_9 = t.default_timer()
    duration_s5 = end_9 - start_9
    print()
    print("SEARCHING 10 RECORDS\n")
    start_10 = t.default_timer()
    print(table_30.get(14492026))  # Passenger,Christian Mullarkey
    print(table_30.get(14397374))  # Passenger,Esmeralda Radovich
    print(table_30.get(14824429))  # Passenger,Nelson Tooker
    print(table_30.get(14929292))  # Passenger,Neil Brabant
    print(table_30.get(14786148))  # Passenger,Clinton Blumer

    print(table_30.get(14495655))  # Passenger,Sofia Bonfiglio
    print(table_30.get(14224671))  # Passenger,Ashlee Capellan
    print(table_30.get(14707100))  # Passenger,Dona Mcinnes
    print(table_30.get(14644633))  # Passenger,Maricela Landreneau
    print(table_30.get(14147356))  # Passenger,Elinor Raco
    end_10 = t.default_timer()
    duration_s10 = end_10 - start_10

    print()
    print("SEARCHING 20 RECORDS\n")
    start_11 = t.default_timer()
    print(table_45.get(14495655))  # Passenger,Sofia Bonfiglio
    print(table_45.get(14224671))  # Passenger,Ashlee Capellan
    print(table_45.get(14707100))  # Passenger,Dona Mcinnes
    print(table_45.get(14644633))  # Passenger,Maricela Landreneau
    print(table_45.get(14147356))  # Passenger,Elinor Raco

    print(table_45.get(14210394))  # Driver,Lonnie Traxson
    print(table_45.get(14088484))  # Driver,Khalilah Dittrick
    print(table_45.get(14481609))  # Passenger,Amal Moznett
    print(table_45.get(14778665))  # Passenger,Cornell Uhri
    print(table_45.get(14905261))  # Driver,Yuriko Stimer
    print(table_45.get(14607868))  # Driver,Jamie Seager
    print(table_45.get(14080040))  # Driver,Guy Loredo
    print(table_45.get(14286103))  # Driver,Dollie Dignan
    print(table_45.get(14030930))  # Driver,Jessie Mayville
    print(table_45.get(14973623))  # Driver,Christian Busbee
    print(table_45.get(14158835))  # Driver,Jamie Shake
    print(table_45.get(14129722))  # Driver,Edwina Esters
    print(table_45.get(14207712))  # Driver,Harriett Zollinger
    print(table_45.get(14151577))  # Driver,Nannie Mcgown
    print(table_45.get(14393910))  # Passenger,Cody Mcmartin

    end_11 = t.default_timer()
    duration_s20 = end_11 - start_11

    print(f"\nTime taken to search 5 records: {round(duration_s5, 10)} seconds")
    print(f"Time taken to search 10 records: {round(duration_s10, 10)} seconds")
    print(f"Time taken to search 20 records: {round(duration_s20, 10)} seconds\n")
    if round(duration_s5, 2) == round(duration_s10, 2) == round(duration_s20, 2):
        print("Time Complexity for searching is O(1) since the time taken are almost the same")
except Exception as err:
    print(err)