import json

from flask import Flask, render_template, Response
from getData import parseExcelDataByName

app = Flask(__name__)


@app.route('/')
def issue_relattion_page():
    # related_issue = {
    #     "nodes": [
    #         {
    #             "name": "5536",
    #             "symbolSize": 30,
    #             "url": "https://github.com/botpress/botpress/issues/5423"
    #         },
    #         {
    #             "name": "1227",
    #             "symbolSize": 30,
    #             "url": "https://github.com/botpress/botpress/issues/5423"
    #         },
    #         {
    #             "name": "5592",
    #             "symbolSize": 30,
    #             "url": "https://github.com/botpress/botpress/issues/5423"
    #         }],
    #     "links": [{
    #         "source": "5536",
    #         "target": "1227"
    #     },
    #         {
    #         "source": "5536",
    #         "target": "5592"
    #     }]
    # }

    related_issue = parseExcelDataByName('botpress')
    return render_template("index.html", related_issue=related_issue)


if __name__ == '__main__':
    app.run()
