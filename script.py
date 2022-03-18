# script.py
import requests
from flask import Flask, render_template, request


app = Flask(__name__)


def scrape(subject, paper_type, exam_type, level, year, language):
    url = ""

    # Checks if any of the inputs are empty
    if not subject or not paper_type or not exam_type or not level or not year or not language:
        url = "Invalid input, please try again"
        return url

    # Now we can make the request for the papers as we have all the info the user
    # wants
    # Notice how the url here is different.  That was a fucking pain to debug.
    subject_url = "https://www.examinations.ie/exammaterialarchive/?i=110.112.93.101.96.94.111.103"
    subject_data = {"MaterialArchive__noTable__cbv__AgreeCheck": "Y", "MaterialArchive__noTable__cbh__AgreeCheck": "N",
                    "MaterialArchive__noTable__sbv__ViewType": paper_type,
                    "MaterialArchive__noTable__sbh__ViewType": "id",
                    "MaterialArchive__noTable__sbv__YearSelect": year,
                    "MaterialArchive__noTable__sbh__YearSelect": "id",
                    "MaterialArchive__noTable__sbv__ExaminationSelect": exam_type,
                    "MaterialArchive__noTable__sbh__ExaminationSelect": "id",
                    "MaterialArchive__noTable__sbv__SubjectSelect": subject,
                    "MaterialArchive__noTable__sbh__SubjectSelect": "id"}
    subject_request = requests.post(subject_url, data=subject_data)

    print(subject_request.text)
    subject_request = subject_request.text.split('\n')
    counter = 0
    for line in subject_request:
        counter += 1

    # Just looking for the lines that match the level and language the user wants
    # and taking that exam paper
    for i in range(counter):
        if language in subject_request[i] and level in subject_request[i]:
            url += subject_request[i + 2]
            url = url[8:-31]

    if url == "":
        return "Unable to find exam paper"
    url = "https://www.examinations.ie/exammaterialarchive/" + url
    return url


def val_to_display(value):
    # Opens the template file
    with open("templates/index.html") as f:
        file = f.read()

    print(file)
    file = file.split('\n')
    for line in file:
        # if the value is in the line, get rid of all the html around it, and just get the displayed
        # text for that value
        if value in line:
            line = line.replace(value, "")
            # print(line)
            line = line.replace("<option value=\"", "").replace("\">", "").replace("</option>", "")
            # print(line)
            return line


# print(val_to_display("10"))

@app.route('/')
def index():
    return render_template('index.html', test="Testing",  # sets the default selected options as descriptors
                           S_exam="[Select Exam]", S_lang="[Select Language]", S_level="[Select Exam Level]",
                           S_subject="[Select Subject]", S_type="[Select Exam Type]", S_year="[Select Year]",
                           S_exam_V="", S_lang_V="", S_level_V="",
                           S_subject_V="", S_type_V="", S_year_V="")


@app.route('/', methods=['POST'])
def getvalue():
    # takes the inputs from the form submitted in index.html
    subject = request.form['subject']
    paper_type = request.form['type']
    exam_type = request.form['exam']
    level = request.form['level']
    year = request.form['year']
    language = request.form['language']
    print(subject)

    url = scrape(subject, paper_type, exam_type, level, year, language)
    # sets the default selected options as the value of the last thing submitted, and display the
    # proper name of the input
    return render_template('index.html', url=url, S_exam=val_to_display(exam_type), S_lang=val_to_display(language),
                           S_level=val_to_display(level), S_subject=val_to_display(subject),
                           S_type=val_to_display(paper_type), S_year=year,
                           S_exam_V=exam_type, S_lang_V=language, S_level_V=level,
                           S_subject_V=subject, S_type_V=paper_type, S_year_V=year)


if __name__ == '__main__':
    app.run(debug=True)
