from numpy.random import choice, randint, shuffle, random
import datetime 
import calendar
import csv

def randgender():
    if(random() < 0.5):
        return "M"
    else:
        return "F"

def randomdate(year, month):
    dates = calendar.Calendar().itermonthdates(year, month)
    return choice([date for date in dates if date.month == month])


def readdiseases():
    file_dis = open("data/disease.txt", 'r')
    disease = file_dis.readlines()
    for i in range (len(disease)):
        disease[i] = disease[i].replace("\r","").replace("\n","")
    file_dis.close()
    return disease

year = 2021
month = 10

# read diseases
diseases = readdiseases()

fields = ["Age", "Gender", "Admission", "Dimission", "Disease"]
dataset_lemo = []
dataset_go = []
dataset_ver = []

### Diagnostic Centre Levi-Montalcini ###

## Others record Gen ##
for i in range(150):
    dimission = randomdate(year, month)
    delta = int((random()**2.3)*11.5)+1
    admission = dimission + datetime.timedelta(days=-delta)
    #age
    e = randint(1,90)
    #generalization
    dec = str(int(e/10))
    record = [dec+"*", randgender(), admission.isoformat(), dimission.isoformat(), choice(diseases)]
    dataset_lemo.append(record)
    # print(record)

## Alex record Gen ##  

alex_dimission = randomdate(year, month)
delta = int((random()**2.3)*5.5)+1
admission = dimission + datetime.timedelta(days=-delta)
# alex_record = ["1*", "M", admission.isoformat(), dimission.isoformat(), "diabete"]
alex_record = ["1*", "M", admission.isoformat(), dimission.isoformat(), choice(diseases)]
print(alex_record)
dataset_lemo.append(alex_record)

shuffle(dataset_lemo)

csvfile = open('data/anonim_levi-montalcini.csv', 'w')
wr = csv.writer(csvfile)
wr.writerow(fields)
wr.writerows(dataset_lemo)
csvfile.close()

### Diagnostic Centre Umberto Veronesi ###

## Others record Gen ##
for i in range(120):
    dimission = randomdate(year, month)
    delta = int((random()**2.6)*12.5)+1
    admission = dimission + datetime.timedelta(days=-delta)
    #age
    e = randint(1,90)
    #generalization
    dec = str(int(e/10))
    record = [dec+"*", randgender(), admission.isoformat(), dimission.isoformat(), choice(diseases)]
    dataset_ver.append(record)

shuffle(dataset_ver)

csvfile = open('data/anonim_umberto-veronesi.csv', 'w')
wr = csv.writer(csvfile)
wr.writerow(fields)
wr.writerows(dataset_ver)
csvfile.close()

### Diagnostic Centre Camillo Golgi ###

## Others record Gen ##
for i in range(180):
    dimission = randomdate(year, month)
    delta = int((random()**2)*12.7)
    admission = dimission + datetime.timedelta(days=-delta)
    #age
    e = randint(1,90)
    #generalization
    dec = str(int(e/10))
    record = [dec+"*", randgender(), admission.isoformat(), dimission.isoformat(), choice(diseases)]
    dataset_go.append(record)

shuffle(dataset_go)

csvfile = open('data/anonim_camillo-golgi.csv', 'w')
wr = csv.writer(csvfile)
wr.writerow(fields)
wr.writerows(dataset_go)
csvfile.close()