import math

# Get month, day, year of person 1
p1_mon = int(input('Person 1: Enter month born (1-12): '))
p1_day = int(input('Person 1: Enter day born (1-31): '))
p1_yea = int(input('Person 1: Enter year born (4-digit): '))
# Get month, day, year of person 2
p2_mon = int(input('Person 2: Enter month born (1-12): '))
p2_day = int(input('Person 2: Enter day born (1-31): '))
p2_yea = int(input('Person 2: Enter year born (4-digit): '))

# Determine number of seconds in day, mon, yea
sec_day = 24 * 60 * 60
sec_yea = (365*3 + 366) * sec_day
avge_sec_yea = sec_yea // 4
avge_sec_mon = avge_sec_yea // 12

# Calculate person 1
p1_sec_1900 = (p1_yea - 1900) * avge_sec_yea + \
              (p1_mon - 1) * avge_sec_mon + \
              p1_day * sec_day
# Calculate person 2
p2_sec_1900 = (p2_yea - 1900) * avge_sec_yea + \
              (p2_mon - 1) * avge_sec_mon + \
              p2_day * sec_day

# Calculate age difference
diff_age = int(math.fabs(p1_sec_1900 - p2_sec_1900))

print('Age difference in seconds:', diff_age)
