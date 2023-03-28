# Importing OS module for getting current directories for read and write files.
import os

current_dir = os.getcwd()  # We will use this to get the current directory for read and write files
read_file_name = "doctors_aid_inputs.txt"  # The name of the file to read
write_file_name = "doctors_aid_outputs.txt"  # The name of the file to write
read_file_path = os.path.join(current_dir, read_file_name)  # The path to the file to read
write_file_path = os.path.join(current_dir, write_file_name)  # The path to the file to write

pat_list = []  # List of patients, most important list because it holds all the data of the patients
fp = dict()  # Dictionary for "False positive" of patients
dp = dict()  # Dictionary for "Disease probability" of patients
risk = dict()  # Dictionary for risk of treatment
incidence = dict()  # Dictionary for incidence.


# Our write to file function that writes "text" variable to the "write_file".
def write_to_file(text):
    with open(write_file_path, "a") as s:
        s.write(text)


# This is our "Create Patient" function that creates patients and computes their "Disease Probabilities".
def create_pat(x):
    line = x.split()  # First it splits the line into words.
    for i in range(len(line)):  # Gets rid of the ","s.
        line[i] = line[i].strip(',')
    for pat in pat_list:
        if line[1] in pat:
            write_to_file("Patient {} cannot be recorded due to duplication.\n".format(line[1]))
            return
    if line[6] == 'Targeted':  # This is for 'Bugfix', if it sees that there is a word "Targeted", it compiles it with "Therapy" and makes them one word.
        line[6:8] = [' '.join(line[6:8])]
    line[3:5] = [' '.join(line[3:5])]  # This line combines the two words (Cancer name and cancer).
    fp[line[1]] = round(1 - float(line[2]), 4)  # Computes False Positive and rounds it to 4 decimals.
    risk[line[1]] = float(line[6])*100  # Computes risk.
    line[6] = "{:.0%}".format(float(line[6]))  # Turns risk to percentage.
    line[2] = "{:.2%}".format(float(line[2]))  # Turns Diagnosis Accuracy to percentage.
    incidence[line[1]] = line[4]  # Saves incidence for later uses.
    line[4] = line[4].split('/')  # Turns incidence to float number.
    divisor = float(line[4][0])
    dividend = float(line[4][1])
    line[4] = divisor/dividend
    pat_list.append(line[1:])  # Adds patient to the patient list.
    write_to_file("Patient {} is recorded.\n".format(line[1]))  # Writes message to file.
    probability(line)  # Checks probability.


# This is our "Remove Patient" function that removes patients from pat_list.
def remove_pat(x):
    line = x.split()
    counter_r = 0  # Counter for 'Error Messages'.
    for i in range(len(line)):
        line[i] = line[i].strip(',')
    # Searches for patients and if catches, deletes it from all database.
    for pat in pat_list:
        if line[1] in pat:
            write_to_file("Patient {} is removed.\n".format(line[1]))
            pat_list.remove(pat)
            del dp[pat[0]]
            del fp[pat[0]]
            del risk[pat[0]]
            del incidence[pat[0]]
        else:
            counter_r += 1
        if counter_r == len(pat_list):  # Checks if counter is equal to len(pat_list) and if it is equal, then it means that there is no patient in pat_list with that name.
            write_to_file("Patient {} is cannot be removed due to absence. \n".format(line[1]))
            counter_r = 0


# This is our "Probability" function that checks for probability of disease in that patient.
def check_probability(x):
    pat = x.split()[1]
    counter_p = 0
    # Checks for patients name in database and if finds it, then writes its probability to file.
    for i in pat_list:
        if pat in i:
            write_to_file("Patient {} has a probability of {}% of having {}.\n".format(i[0], dp[i[0]], i[2]))
        else:
            counter_p += 1
        if counter_p == len(pat_list):
            write_to_file("Probability for {} cannot be calculated due to absence.\n".format(pat))
            counter_p = 0


# Check Probability Function uses Confusion Matrix to calculate probability of disease in that patient when it has been added to the patient list.
def probability(line):
    tp = float(line[4])
    dp[line[1]] = round(tp / (tp + fp[line[1]]) * 100, 2)
    if float(dp[line[1]]) == int(dp[line[1]]):
        dp[line[1]] = int(dp[line[1]])


# This is our "Recommendation" function that checks for recommendation for we should treat the patient or not.
def recommendation(x):
    line = x.split()
    pat = line[1]
    counter_rc = 0
    # Checks that if "Disease Probability" is higher than the "Treatment Risk". If it is, suggests us to treat.
    for i in pat_list:
        if pat in i:
            if dp[i[0]] > risk[i[0]]:
                write_to_file("System suggests {} to have the treatment.\n".format(pat))
            else:
                write_to_file("System suggests {} NOT to have the treatment.\n".format(pat))
        else:
            counter_rc += 1
        if counter_rc == len(pat_list):
            write_to_file("Recommendation for {} cannot be calculated due to absence.\n".format(pat))


# This function just gets the list of patients. It has exceptions for longer or shorter words.
def getlist():
    write_to_file("Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\nName\tAccuracy\tName\t\t\t"
                  "Incidence\tName\t\t\tRisk\n-------------------------------------------------------------------------\n")
    for pat in pat_list:
        if len(pat[4]) == 16:
            write_to_file("{}\t{}\t\t{}\t{}\t{}{}\n".format(pat[0], pat[1], pat[2], incidence[pat[0]], pat[4], pat[5]))
        elif len(pat[4]) == 7:
            write_to_file("{}\t{}\t\t{}\t{}\t{}\t\t\t{}\n".format(pat[0], pat[1], pat[2], incidence[pat[0]], pat[4], pat[5]))
        elif len(pat[2]) == 11:
            write_to_file("{}\t{}\t\t{}\t\t{}\t{}\t{}\n".format(pat[0], pat[1], pat[2], incidence[pat[0]], pat[4], pat[5]))
        elif len(pat[0]) == 2:
            write_to_file("{}\t\t{}\t\t{}\t{}\t{}\t{}\n".format(pat[0], pat[1], pat[2], incidence[pat[0]], pat[4], pat[5]))
        else:
            write_to_file("{}\t{}\t\t{}\t{}\t{}\t{}\n".format(pat[0], pat[1], pat[2], incidence[pat[0]], pat[4], pat[5]))


def read_file():
    with open(read_file_path, 'r') as f:
        for lines in f:
            if lines.startswith("create "):
                create_pat(lines)
            if lines.startswith("remove "):
                remove_pat(lines)
            if lines.startswith("probability "):
                check_probability(lines)
            if lines.startswith("recommendation "):
                recommendation(lines)
            if lines.startswith("list"):
                getlist()


# This part is our main function, which is responsible for reading the file and leading us to the wanted functions.
if __name__ == "__main__":
    read_file()

# Mert ERGÜN
# b2220356062
