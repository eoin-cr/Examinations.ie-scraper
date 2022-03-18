# script.py
import requests
import webbrowser
from flask import Flask, render_template, request


# TODO: Use js to save selected inputs

app = Flask(__name__)


def scrape(subject, paper_type, exam_type, level, year, language):
    url = ""
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


@app.route('/')
def index():
    return render_template('index.html', test="Testing")


@app.route('/', methods=['POST'])
def getvalue():
    subject = request.form['subject']
    paper_type = request.form['type']
    exam_type = request.form['exam']
    level = request.form['level']
    year = request.form['year']
    language = request.form['language']
    print(subject)

    url = scrape(subject, paper_type, exam_type, level, year, language)
    return render_template('index.html', url=url)


if __name__ == '__main__':
    app.run(debug=True)
