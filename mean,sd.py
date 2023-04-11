import matplotlib.pyplot as plt


with open("result.txt") as r:
    results = r.readlines()
    


#make int
for i in range(len(results)):
	if results[i] == "\n":
		results[i] = 0
	else:
		results[i] = int(results[i])

#calculate mean
suma=0
for i in range(len(results)):
	if i != 200:
		suma += ((i*.5) + 0.25) * results[i]
	else:
		suma+= 100*results[200]

mean = suma/sum(results)


#calculate standard deviation
sd=0
for i in range(len(results)):
	if i != 200:
		sd += (((i*.5) + 0.25 - mean)**2) * results[i]
	else:
		sd += ((100-mean)**2)*results[200]


standard_dev=(sd/sum(results))**0.5


print("mean is " + str(mean))
print("standard deviation is: " + str(standard_dev))
print("average for p4mg is : 93.05")
print("numner of people: 76")
