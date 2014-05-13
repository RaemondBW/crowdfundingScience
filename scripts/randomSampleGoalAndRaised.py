import json
import time

f = open("goalAndRaisedAmount.json")
d = json.load(f)
f.close()

#buckets = [(0,0),(10000,0), (634375,0), (1258750,0), (1883125,0), (2507500,0), (3131875,0), (3756250,0), (4380625,0), (5005000,0), (5629375,0), (6253750,0), (6878125,0), (7502500,0), (8126875,0), (8751250,0), (9375625,0),(10000001,0)]
#buckets = [(0,0), (10000,0), (71875,0), (133750,0), (195625,0), (257500,0), (319375,0), (381250,0), (443125,0), (505000,0), (566875,0), (628750,0), (690625,0), (752500,0), (814375,0), (876250,0), (938125,0),(1000001,0)]
b = [10000, 15625, 21250, 26875, 32500, 38125, 43750, 49375, 55000, 60625, 66250, 71875, 77500, 83125, 88750, 94375]

buckets = [(0,0)]
for buck in b:
    buckets.append((buck,0))


minGoal = 100000
maxGoal = 0

minPercent = 1000
maxPercent = 0
i = 0
for project in d:
    i+=1
    goal = float(unicode(project["Goal"]))
    raised = float(unicode(project["Raised"]))

    for i in range(len(buckets)-1):
        if goal>buckets[i][0] and goal<buckets[i+1][0]:
            buckets[i]=(buckets[i][0],buckets[i][1]+1)

            break

    if goal>maxGoal:
        maxGoal = goal
    if goal<minGoal:
        minGoal = goal

    percent = (raised/goal)*100

    if percent<minPercent:
        minPercent = percent
    if percent> maxPercent:
        maxPercent = percent


print "minGoal: %s, maxGoal: %s, minPercent: %s, maxPercent: %s, i=%s"%(minGoal,maxGoal,minPercent,maxPercent,i)
print buckets
# f = open("valuesByCategoryUSD2.json", 'w')
# f.write(json.dumps(categories, indent=4))
# f.close()
