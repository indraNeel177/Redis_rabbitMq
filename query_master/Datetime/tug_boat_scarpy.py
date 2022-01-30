import json

from numpy import append
# f = open("", "r")
with open('query_master/Datetime/work_fuel.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

l = []
k = []

for x in mylist:
    if x not in '          EXCEPTION             ':
        m = x.split("          PUBLISH SUCCESS           :")
        l.append(json.loads(m[-1]))
        # 
        if "[" not in m[-1]:
            if "Update Success" not in m[-1]:
                if "values" in m[-1]:
                    print(m[-1])
                    # l.append(m[-1])
            
            
        


print(l)





# print(sorted(l))

# # g = []
# # for y in l:
# #     y = json.loads(y)
# #     for z in y["data"]:
# #         g.append([str(z.get("gps").get("date")+0.0),  str(z.get("gps").get("latitude")),str(z.get("gps").get("longitude")), str(z.get("gps").get("speed") +0.0), '', '', '', ''])

# # print(g)