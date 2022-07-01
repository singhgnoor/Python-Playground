""" This is Program that reads a CSV File """

import pandas as pd

# data = pd.DataFrame([["Gurnoor Singh", "Saini", "Good Person"], ["Gurnoor Singh", "Saini", "Good Person"],
#                      ["Gurnoor Singh", "Saini", "Good Person"], ["Gurnoor Singh", "Saini", "Good Person"],
#                      ["Gurnoor Singh", "Saini"], ["Gurnoor Singh"], ],
#                     columns=["Name", "Surname", "More Information"])
#
# data.to_csv("New.csv", index=False)
#
# data = pd.read_csv("New.csv")`
#
# # print(data.to_string(index_names="Index"))
# data.to_csv("New.csv", header=["New_Name", "New_Surname", "New_More_Info"], na_rep='------')

personal_info = pd.DataFrame([['Gurnoor Singh', 'gurnoorsinghsaini07@gmail.com', 9501587214],
                              ['Jatinder Singh', 'jatindersinghgps@gmail.com', 9855045144, "Teacher"],
                              ['Harry', 'harry@codewithharry.com', None, "Programmer"],
                              ['Harsimran Kaur', 'harsimrankaursaini05@gmail.com', 8968152575],
                              ['Sukhbir Kaur', 'sukhbir.ctips@gmail.com', 9814275574, "Officer"], ],
                             columns=["Name", "Email", "PhoneNumber", "Occupation"])

personal_info.to_csv("info.csv", index=False, na_rep="----", )

