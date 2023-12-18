import requests
from bs4 import BeautifulSoup
import json


class ParseFideRating:
    
    def __init__(self, category = "open", data_type="list"):
        self.data_type = data_type
        self.url = f"https://ratings.fide.com/a_top.php?list={category}"
        
        
    def get_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find("table")
        rows = table.findAll("tr")
        
        rows_data = []
        
        for row in rows:
            cols = row.find_all("td")
            for col in cols:
                cols_data = {}
                
                cols = list(str(col.text).strip().replace("\n", "") for col in row.find_all("td"))
                
                cols_data["ranking"] = cols[0]
                cols_data["player"] = cols[1]
                cols_data["country_code"] = cols[2]
                cols_data["rating"] = cols[3]
                cols_data["birth_year"] = cols[5]
                cols_data["avg12m"] = cols[6]
                
                rows_data.append(cols_data)
        print("Success! Print data to check out")
        
        if self.data_type == "list":
            return rows_data
        
        if self.data_type == "file":
            with open('result.json', 'w', encoding='utf-8') as fp:
                json.dump(rows_data, fp)
                print("Success! Data saved in result.json")

