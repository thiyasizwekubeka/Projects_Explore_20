## CMD to run the script: 'uvicorn logic:app --reload'




from fastapi import FastAPI
import uvicorn
import json

# Init

app = FastAPI(debug=True)



# Data





# Route

@app.get('/survivorCount')
async def x():


        PASSANGERS =  [
        {
            "PassengerId": 123,
            "Survived": 1,
            "Pclass": 3,
            "Name":"Braund, Mr. Owen Harris",
            "Sex": "male",
            "Age": 22, 
            "SibSp": 1,
            "Parch": 0,
            "Ticket": "A/5 21171"
        },
        {
            "PassengerId": 124,
            "Survived": 0,
            "Pclass": 3,
            "Name": "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
            "Sex": "female",
            "Age": 39,
            "SibSp": 1,
            "Parch": 0,
            "Ticket": "A/5 21271"
        }
    ]

        bin_boundaries = [5,10]
        bin_field= "Age"

        survivors = [p for p in PASSANGERS if p["Survived"]]

        left = len([s for s in survivors if s[bin_field] < bin_boundaries[0]])
        middle = len([s for s in survivors if s[bin_field] >= bin_boundaries[0] and s[bin_field] < bin_boundaries[1]])
        right = len([s for s in survivors if s[bin_field] >= bin_boundaries[1]])

        counts = [left, middle, right]

        return{"counts":counts}

# if __name__ == "__main__":
#     univorn.run(app, host == '127.0.0.1' ,port= '8000')
    

# if _name_ == '_main_':
#     univorn.run(app.host == "127.0.0.1",port="8000")





# PASSANGERS =  [
#     {
#         "PassengerId": 123,
#         "Survived": 1,
#         "Pclass": 3,
#         "Name":"Braund, Mr. Owen Harris",
#         "Sex": "male",
#         "Age": 22, 
#         "SibSp": 1,
#         "Parch": 0,
#         "Ticket": "A/5 21171"
#     },
#     {
#         "PassengerId": 124,
#         "Survived": 0,
#         "Pclass": 3,
#         "Name": "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
#         "Sex": "female",
#         "Age": 39,
#         "SibSp": 1,
#         "Parch": 0,
#         "Ticket": "A/5 21271"
#     }
# ]

# bin_boundaries = [5,10]
# bin_field= "Age"

# survivors = [p for p in PASSANGERS if p["Survived"]]

# left = len([s for s in survivors if s[bin_field] < bin_boundaries[0]])
# middle = len([s for s in survivors if s[bin_field] >= bin_boundaries[0] and s[bin_field] < bin_boundaries[1]])
# right = len([s for s in survivors if s[bin_field] >= bin_boundaries[1]])

# counts = [left, middle, right]
# print(counts)
