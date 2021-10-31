def zeller(dmy):
    century=20
    month = int(dmy[2:4])-2
    year = int(dmy[:2])
    if month<= 0:
        month=month+12
        year-=1
    d = int(dmy[4:])
    w=(13*month-1)//5
    x=year//4
    y=century//4
    z=w+x+y+d-(2*century)+year
    r = z%7
    days =['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    return days[r]

f = open("2015HomicideLog_FINAL.txt",'r')
lines = f.readlines()
days =['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
d=[]
dayscount={'Sunday':0,'Monday':0,'Tuesday':0,'Wednesday':0,'Thrusday':0,'Friday':0,'Saturday':0}
race={}
racep={}
aget={"0-10":0,"10-20":0,"20-30":0,"30-40":0,"40-50":0,"50-60":0,"60-70":0,"70-80":0,"80-90":0,"90<":0}
gender={"M":0,"F":0}
genderp={"M":"%","F":"%"}
timecount={}
for line in lines:
    dmy =line.split('\t')[0].split(' ')[0]
    x=zeller(dmy)
    d.append(x)
    dayscount[x]+=1
print(dayscount) # Number of homicide each day

#print(lines[0].split('\t')[1].split(":")[0])
for line in lines:
    time =line.split('\t')[1].split(":")[0]
    if(time in timecount.keys()):
        timecount[time]=timecount[time]+1
    else:
        timecount[time] =1
print(timecount)

#print(lines[0].split("\t")[4])
for line in lines:
    genrace=""
    age =""
    if(len(line.split("\t"))>5):
        genrace = line.split("\t")[4]
        age = line.split("\t")[5][0:2]
        
    else:
        genrace = line.split("\t")[3]
        age = line.split("\t")[4][0:2]
    rac = genrace[0:1]
    age=int(age)
    if(age>=0 and age<10):aget["0-10"]+=1
    if(age>=10 and age<20):aget["10-20"]+=1
    if(age>=20 and age<30):aget["20-30"]+=1
    if(age>=30 and age<40):aget["30-40"]+=1
    if(age>=40 and age<50):aget["40-50"]+=1
    if(age>=50 and age<60):aget["50-60"]+=1
    if(age>=60 and age<70):aget["60-70"]+=1
    if(age>=70 and age<80):aget["70-80"]+=1
    if(age>=80 and age<90):aget["80-90"]+=1
    if(age>=90):aget["90<"]+=1
    gen=genrace[1:]
    gender[gen]=gender[gen]+1
    if(rac in race.keys()):
        race[rac] = race[rac]+1
    else:
        race[rac] =1
print(race)
print(gender)
print(aget,"Age Total")
for key in race:
    racep[key] = "{:.2f}%".format(race[key]/1.34)
    
for key in gender:
    genderp[key]="{:.2f}%".format(gender[key]/1.34)
    
print("Race Percentage:\t",racep)
print("Gender percentage:\t",genderp)


