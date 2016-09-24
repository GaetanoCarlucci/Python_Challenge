from calendar import weekday, isleap

candidate_years = [i for i in range(1006, 2006, 10) if (weekday(i, 1, 1) == 3) and isleap(i)]

#we should take the not the youngest, but the second.
print "The date should be 27 January " + str(candidate_years[-2])

print "It seems that Mozart has born this day."
print "The url is mozart.html"