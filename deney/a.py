# Ahmet Arda Çelik 2220356065
# Computer Science
# Assignment 2

from tabulate import tabulate 
import copy 

output = ""
f = open("doctors_aid_inputs.txt", "r", encoding="utf8")
list1 = []
write= open("doctors_aid_outputs.txt","w",encoding="utf8" )

#This function checks if the patient in the input already exists in the system or not.
def look(r):
  for i in list1:
    if r == i[0].strip():
      return True

#This function creates the patient, records them into the system.
def create(x):
  if look(x[0]):
      write.write(x[0]+" profile already exists.\n")
  else:
      list1.append(x)
      write.write(x[0]+" profile has been created.\n")

#This function removes the patient off the system.
def remove(x):
  if look(x[0]):
    for a in list1:
      if x[0] in a:
        write.write(str(a[0]) + " has been removed.\n")
        list1.remove(a)
  else:
    write.write("Patient " + str(a) +" does not exist.\n")

#This function converts the value of the disease incidence into float.
def convert(x):
    calc = x.split("/")
    a,b=float(calc[0]),float(calc[1])
    result=a/b
    return result

#This function calculates the probability.
def calcprobability(x):
  if look(x[0]):
    for a in list1:
      if x[0] in a:
        
        num1= convert(a[3])
        num2=float(a[1])
        p = round(num1/(1-num2 +num1), 2) 
        return [p, a[2]]
      else:
        pass
  else:
    pass

#This function gives the probability value to the output.
def probability(x):
  if look(x[0].strip()):
    probability_patient = calcprobability(x)
    s = float((probability_patient[0]))*100
    if s == int(s):
       s = int(s)
    write.write("Patient " + str(x[0]) + " has a probability of " + str(s) +"%"+ " of having "+ str(probability_patient[1] + "\n"))
  else:
    write.write("The probability cannot be calculated due to absence.\n")

#This function gives the list to the output.
def list():
  global list1
  tablelist=copy.deepcopy(list1)
  for i in tablelist:
    acc=100*float(i[1])
    if acc == int(acc):
      acc = int(acc)
    a= str(acc) + "%"
    i[1] = a
    risk=100*float(i[5])
    if risk == int(risk):
       risk = int(risk)
    r= str(risk) + "%"
    i[5] = r



#This part of the code is for tabulating the list.
  head=['Patient'+'\n' +'Name', 'Diagnosis '+'\n' +'Accuracy','Disease'+'\n' +' Name','Disease '+'\n' +'Incidence','Treatment'+'\n' +' name','Treatment'+'\n' +' Risk']
  table= tabulate(tablelist, headers=head)
  write.write(table)
  write.write("\n")

#This function recommends if the patient should have the treatment or not.
def recommendation(x):
  if look(x[0]):
    for a in list1:
      if x[0] in a:
        if calcprobability(a)[0] > float(a[5]):
          write.write('The system recommends '+ str(x[0]) +' to have the treatment.\n')
        else:
          write.write('The system does not recommend ' + str(x[0]) + ' to have the treatment.\n')
  else:
    write.write("Patient does not exist.\n")
   


#This part of the code is for calling the functions.

for x in f:
  inputfile = x.split(" ", 1)
  if(inputfile[0]=="create"):
    patient_name = inputfile[-1].split(", ")
    patient_name[-1]=patient_name[-1].replace("\n", "")
    create(patient_name)


  elif(inputfile[0]=="remove"):
    patient_name = inputfile[-1].split(", ")
    patient_name[-1]=patient_name[-1].replace("\n", "")
    remove(patient_name)

    
  elif(inputfile[0]=="probability"):
    patient_name = inputfile[-1].split(", ")
    patient_name[-1]=patient_name[-1].replace("\n", "")
    probability(patient_name)


  elif(inputfile[0]=="recommendation"):
    patient_name = inputfile[-1].split(", ")
    patient_name[-1]=patient_name[-1].replace("\n", "")
    recommendation(patient_name)


  elif(inputfile[0]=="list\n"):
    list()


        
        



