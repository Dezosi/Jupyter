import requests
import xmltodict

url = "https://www.cbr.ru/scripts/XML_val.asp"
response = requests.get(url)

data = xmltodict.parse(response.content)


my_array = []
for item in data['Valuta']['Item']:
    my_set = [item['Name'], item['EngName'], item['Nominal'], item['ParentCode']]
    my_array.append(my_set)
    print(my_set)
