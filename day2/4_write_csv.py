
import pandas as pd
import json
json_arr = [
    {
        "name":"aryan jaswal",
        "roll":"1"
    },
    {
        "name":"ram",
        "roll":"2"
    }
]
csv_data = pd.DataFrame(json_arr)

csv_data.to_csv("file.csv")