##########GasPeddlr##########
#Proof of concept
import csv;

F = open('assets/vehicles.csv')
CSV_F = csv.reader(F)

#CLASSIFICATIONS = CSV_F[0]

GAS_PRICE= 2.00 #Constant for now

table = {} #{ make : {model: [city mpg, highway mpg]}}
# 46 = make
# 47 = model
# 58 = UCity
# 60 = UHighway

for row in CSV_F:
	if row[0] != "":
		table[row[46]] = { row[47]: [row[58], row[60]] }
print table

def costOfMeme( people, mpg, distance):
	return (GAS_PRICE * distance)/(mpg*people)
def mpgOfMeme(make, model, typ):
	if type == "City":
		flag = True
	else:
		flag = False
	thisMake = table[make]
	thisModel = thisMake[model]
	if flag:
		return float(thisModel[0])
	else:
		return float(thisModel[1])
#print "I WOKE UP IN A NEW FERRARI"
print "2 guys, 1 Rolls-Royce Continental R, 69 miles, snipars"
print table['Rolls-Royce']
print costOfMeme(2,mpgOfMeme("Rolls-Royce", "Continental R","City"), 69)
#print costOfMeme(2, mpgOfMeme("Ferrari", "Testarossa", "City"), 69)








