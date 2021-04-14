olympians = [("John Aalberg", 31, "Cross Country Skiing"),
            ("Minna Maarit Aalto", 30, "Sailing"),
            ("Win Valdemar Aaltonen", 54, "Art Competitions"),
            ("Wakako Abe", 18, "Cycling")]

with open("reduced_olympics.csv", "w") as outFile:
    outFile.write("Name,Age,Sport\n")
    for olympian in olympians:
        row_string = ",".join([olympian[0], str(olympian[1]), olympian[2]])
        # if you turn the ages to string, then no need to convert and the join would be:
        # ",".join(olympian)
        # row_string = "{},{},{}".format(olympian[0],olympian[1],olympian[2])
        outFile.write(row_string + "\n")

