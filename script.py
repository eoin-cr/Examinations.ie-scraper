# script.py
import requests
import webbrowser

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

base_url = "https://www.examinations.ie/exammaterialarchive/?i=92.98.109.96.96.103"
# headers = {
#         "Host": "www.examinations.ie",
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Content-Length": "86",
#         "Origin": "https://www.examinations.ie",
#         "Connection": "keep-alive",
#         "Upgrade-Insecure-Requests": "1",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "same-origin",
#         "Pragma": "no-cache",
#         "Cache-Control": "no-cache",
#         "TE": "trailers",
# }
base_data = {"MaterialArchive__noTable__cbv__AgreeCheck": "", "MaterialArchive__noTable__cbh__AgreeCheck": "N"}
# response = requests.post(url, headers=headers, data=data)
# response1 = requests.post(url, data=data)

# headers = {
#         "Host": "www.examinations.ie",
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Language": "en-US,en;q=0.5",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Content-Length": "273",
#         "Origin": "null",
#         "Connection": "keep-alive",
#         "Upgrade-Insecure-Requests": "1",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "same-origin",
#         "Sec-Fetch-User": "?1",
# }
#
# data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N", "MaterialArchive__noTable__sbv__ViewType": paper_type, "MaterialArchive__noTable__sbh__ViewType": "id"}
#
# paper_type_url = "https://www.examinations.ie/exammaterialarchive/?i=115.120.111.100.99"
# data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N", "MaterialArchive__noTable__sbv__ViewType": paper_type, "MaterialArchive__noTable__sbh__ViewType": "id"}
# paper_type_data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N", "MaterialArchive__noTable__sbv__ViewType": paper_type, "MaterialArchive__noTable__sbh__ViewType": "id"}
# response2 = requests.post(url, headers=headers, data=data)
# paper_type_response = requests.post(paper_type_url, data=paper_type_data)

# year_url = "https://www.examinations.ie/exammaterialarchive/?i=120.100.96.113.99"
# year_data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N", "MaterialArchive__noTable__sbv__ViewType": paper_type, "MaterialArchive__noTable__sbh__ViewType": "id", "MaterialArchive__noTable__sbv__YearSelect": year, "MaterialArchive__noTable__sbh__YearSelect": "id"}
# year_request = requests.post(year_url, data=year_data)

# exam_type_url = "https://www.examinations.ie/exammaterialarchive/?i=98.117.94.106.101"

exam_type_url = "https://www.examinations.ie/exammaterialarchive/?i=94.113.90.102.105"
exam_data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N", "MaterialArchive__noTable__sbv__ViewType": paper_type, "MaterialArchive__noTable__sbh__ViewType": "id", "MaterialArchive__noTable__sbv__YearSelect": year, "MaterialArchive__noTable__sbh__YearSelect": "id", "MaterialArchive__noTable__sbv__ExaminationSelect": exam_type, "MaterialArchive__noTable__sbh__ExaminationSelect": "id"}
exam_type_request = requests.post(exam_type_url, data=exam_data).text
exam_type_request = exam_type_request[5000:]
subject = ">" + subject
index = exam_type_request.find(subject)
index += 1

print(f'Index: {index}')
print(f'Index letter: {exam_type_request[index]}')
while index == -1:
    subject = input("""Error, subject not found, please try again.  Try writing
out the full name of the subject (no abbreviations): """)
    index = exam_type_request.find(subject)

if type(exam_type_request[index-5]) == int:
    subject = exam_type_request[index-5:index-2]
    print(subject)
elif type(exam_type_request[index-4]) == int:
    subject = exam_type_request[index-4:index-2]
    print(subject)
else:
    subject = exam_type_request[index-3:index-2]

print(f'Subject surround: {exam_type_request[index-10:index+10]}')

subject_url = "https://www.examinations.ie/exammaterialarchive/?i=110.112.93.101.96.94.111.103"
subject_data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N", "MaterialArchive__noTable__sbv__ViewType": paper_type, "MaterialArchive__noTable__sbh__ViewType": "id", "MaterialArchive__noTable__sbv__YearSelect": year, "MaterialArchive__noTable__sbh__YearSelect": "id", "MaterialArchive__noTable__sbv__ExaminationSelect": exam_type, "MaterialArchive__noTable__sbh__ExaminationSelect": "id", "MaterialArchive__noTable__sbv__SubjectSelect": subject, "MaterialArchive__noTable__sbh__SubjectSelect": "id"}
subject_request = requests.post(subject_url, data=subject_data)
# print(subject_request.text)

subject_request = subject_request.text.split('\n')
counter = 0
for line in subject_request:
    counter += 1

for i in range(counter):
    if language in subject_request[i] and level in subject_request[i]:
        url = subject_request[i+2]
        url = url[8:-31]

url = "https://www.examinations.ie/exammaterialarchive/" + url
print(url)
webbrowser.open_new(url)

# print(f'1: {response1.text}')
# print(f'2: {paper_type_response.text}')
# print(year_request.text)
