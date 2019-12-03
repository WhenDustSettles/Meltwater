import requests
import pandas as pd

url = 'https://dip.goa.gov.in/accreditation-of-journalists.php'
html = requests.get(url).content
df_list = pd.read_html(html)
