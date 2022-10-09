import pandas as pd
import json


def parseExcelDataByName(projectName):

    df = pd.read_excel (r'/Users/yuzuqiang/Desktop/Accessbility-analyzer/issue_track_data.xlsx',keep_default_na=False)

    project_name = 'botpress'

    data_list = []
    last_row = ''
    current_row = ''

    related_issue = {"nodes": [], "links": []}
    # read data from excel (line-by-line)
    for i in range(1,7000):
        row_data = df.iloc[i].values

        if row_data[0] == project_name:
            if i == 1:
                temp_node = {'name': row_data[3], 'type': row_data[2], 'symbolSize' :30,
                        'url': row_data[8]}
                related_issue["nodes"].append(temp_node)
            else:
                # current row issue number
                current_row = row_data[3]
                if current_row == last_row:
                    # check links

                    if row_data[7] != '':
                        temp_link = {"source": current_row, "target": row_data[7]}
                        related_issue["links"].append(temp_link)
                else:
                    temp_node = {'name': row_data[3], 'type': row_data[2], 'symbolSize': 30,
                                 'url': row_data[8]}
                    related_issue["nodes"].append(temp_node)

            # update last issue name
            last_row = row_data[3]



    with open('data.json' ,"w") as f:

        json.dump(related_issue,f,indent=4,ensure_ascii=False)

    return json.dumps(related_issue)


print(parseExcelDataByName('botpress'))
