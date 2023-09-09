import locale
from pdfquery import PDFQuery
from bs4 import BeautifulSoup
import pandas as pd

pdf = PDFQuery("Nubank_2023-09-11.pdf")
pdf.load()

#convert the pdf to XML
pdf.tree.write('nubank.xml', pretty_print = True)
print(pdf)

with open("nubank.xml", "r") as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")

b_names = Bs_data.find_all('LTTextBoxHorizontal', {'height':'8.0'})
 
list_values = []
list_names = []
for i in range(0,len(b_names)):
    b_name_edited = str(b_names[i]).split(">")[1]
    b_name_edited = b_name_edited.split("<")[0]
    try:
        float_number = float(b_name_edited.replace(".", "").replace(",", "."))
        if float_number:
            
            list_values.append(float_number)
            # print(b_names[i-1])
            list_names.append(str(b_names[i-1]).split(">")[1].split("<")[0])
    except:
        pass
print(list_values)
print(list_names)

df = pd.DataFrame()
df["Names"] = list_names
df["Values"] = list_values
print(df)
df.to_csv("out.csv")
# list_numbers = []

# for i in range(0,len(list_values)):
#     try:
#         list_numbers.append(float(list_values[i]))
#     except:
#         pass
        
# print(list_numbers)
