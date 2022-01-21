# script.py
import requests
import webbrowser

# Just getting user info
paper_type = input("Do you want exam papers (E) or marking schemes (M)?: ")
year = input("Which year do you want?: ")
exam_type = input("""Do you want Leaving Cert Applied (LB), Leaving Cert (LC)
        or Junior Cert/Cycle (JC)?: """).lower()
subject = input("What subject do you want?: ")
language = "(" + input("Do you want the paper in Irish (IV) or English (EV)?: ") + ")"
level = input("Do you want Higher Level (HL) or Ordinary Level (OL)?: ")


if paper_type == "E":
    paper_type = "exampapers"
else:
    paper_type = "markingschemes"

if level == "HL":
    level = "Higher Level"
else:
    level = "Ordinary Level"

# We need to make this request to get the number of the subject the user wants
exam_type_url = "https://www.examinations.ie/exammaterialarchive/?i=94.113.90.102.105"
exam_data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N", "MaterialArchive__noTable__sbv__ViewType": paper_type, "MaterialArchive__noTable__sbh__ViewType": "id", "MaterialArchive__noTable__sbv__YearSelect": year, "MaterialArchive__noTable__sbh__YearSelect": "id", "MaterialArchive__noTable__sbv__ExaminationSelect": exam_type, "MaterialArchive__noTable__sbh__ExaminationSelect": "id"}
exam_type_request = requests.post(exam_type_url, data=exam_data).text

# There are some subject names in the metadata list at the beginning so we
# just remove the first 5000 chars to be safe
exam_type_request = exam_type_request[5000:]

# We want to add `>` to the search to ensure if the user is looking for say
# Mathematics, it won't return the index of Applied Mathematics
subject = ">" + subject
index = exam_type_request.find(subject)

# Now we add 1 to the index to account for the `>` we added
index += 1

# Just checking the subject can be found
while index == -1:
    subject = input("""Error, subject not found, please try again.  Try writing
out the full name of the subject (no abbreviations): """)
    index = exam_type_request.find(subject)

# Checking how long the subject number is (it ranges from 1 to 3 digits)
if type(exam_type_request[index-5]) == int:
    subject = exam_type_request[index-5:index-2]
    print(subject)
elif type(exam_type_request[index-4]) == int:
    subject = exam_type_request[index-4:index-2]
    print(subject)
else:
    subject = exam_type_request[index-3:index-2]

# Now we can make the request for the papers as we have all the info the user
# wants
# Notice how the url here is different.  That was a fucking pain to debug.
subject_url = "https://www.examinations.ie/exammaterialarchive/?i=110.112.93.101.96.94.111.103"
subject_data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N", "MaterialArchive__noTable__sbv__ViewType": paper_type, "MaterialArchive__noTable__sbh__ViewType": "id", "MaterialArchive__noTable__sbv__YearSelect": year, "MaterialArchive__noTable__sbh__YearSelect": "id", "MaterialArchive__noTable__sbv__ExaminationSelect": exam_type, "MaterialArchive__noTable__sbh__ExaminationSelect": "id", "MaterialArchive__noTable__sbv__SubjectSelect": subject, "MaterialArchive__noTable__sbh__SubjectSelect": "id"}
subject_request = requests.post(subject_url, data=subject_data)

subject_request = subject_request.text.split('\n')
counter = 0
for line in subject_request:
    counter += 1

# Just looking for the lines that match the level and language the user wants
# and taking that exam paper
for i in range(counter):
    if language in subject_request[i] and level in subject_request[i]:
        url = subject_request[i+2]
        url = url[8:-31]

url = "https://www.examinations.ie/exammaterialarchive/" + url
# print(url)

# Now we can open the url in the user's web browser
webbrowser.open_new(url)
