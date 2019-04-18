import xlrd
from collections import OrderedDict
import simplejson as json


# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('sentiment-project.xlsx')
sh = wb.sheet_by_index(0)

# List to hold dictionaries
sentiment_proj = []

# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    form = OrderedDict()
    row_values = sh.row_values(rownum)
    form['phone-no'] = row_values[0]
    form['age'] = row_values[1]
    form['gender'] = row_values[2]
    form['location'] = row_values[3]
    form['response'] = row_values[4]
    form['comments'] = row_values[5]

    sentiment_proj.append(form)
# Serialize the list of dicts to JSON
j = json.dumps(sentiment_proj)
# Write to file
with open('data.json', 'w') as f:
    f.write(j)