f = open("fix.csv")
lines = list(f)
lines = [x.strip() for x in lines]
lines.reverse()
new_lines = []
for line in lines:
    line = line.split(',')
    line[0] = line[0].replace('Nov', '11')
    line[0] = line[0].replace('Oct', '10')
    line[0] = line[0].replace('Sep', '09')
    line[0] = line[0].replace('Aug', '08')
    line[0] = line[0].replace('Jul', '07')
    line[0] = line[0].replace('Jun', '06')
    line[0] = line[0].replace('May', '05')
    line[0] = line[0].replace('Apr', '04')
    line[0] = line[0].replace('Mar', '03')
    line[0] = line[0].replace('Feb', '02')
    line[0] = line[0].replace('Jan', '01')
    line[0] = line[0].replace('Dec', '12')
    line[0] = line[0].split()
    a,b,c = line[0]
    line[0] = f"{c}-{a}-{b}"
    print(','.join(line))
