import requests

# Import the URLLIB for opening and reading URLs 
import urllib


dls = "https://education.ohio.gov/getattachment/Topics/Finance-and-Funding/School-Payment-Reports/District-Profile-Reports/FY2022-District-Profile-Report-1/FY23-District-Profile-Report-Final-12-14-2023.xlsx.aspx?lang=en-US"

urllib.request.urlretrieve(dls, "test.xls")

print('job complete!')
