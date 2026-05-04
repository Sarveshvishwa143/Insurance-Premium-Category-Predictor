from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from typing import Literal , Annotated
import pickle
import pandas as pd

with open("model1.pkl" , "rb") as f:
    model = pickle.load(f)

app = FastAPI()


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

class UserInput(BaseModel):
    age:        Annotated[int, Field(..., gt=0 , lt = 129 , discription = "Age of the use")]
    weight:     Annotated[float , Field(... , gt = 0 , description='Weight of the user')]
    height:     Annotated[float , Field(...,gt=0 , lt=250 , description='height of the user')]
    income_lpa: Annotated[float , Field(..., gt=0 , description='Annual salary  of the user')]
    smoker:     Annotated[bool , Field(..., description='is user a smoker')]
    city:       Annotated[str , Field(..., description='use city')]
    occupation: Annotated[Literal['Factory Worker', 'Businessman', 'Sales Manager', 'Banker',
       'Marketing Manager', 'Insurance Agent', 'HR Manager', 'Pharmacist',
       'Teacher', 'Software Engineer', 'Consultant', 'Driver',
       'Shop Owner', 'Nurse', 'Accountant', 'Government Employee',
       'Architect', 'Engineer', 'Real Estate Agent', 'Civil Servant',
       'Plumber', 'Retail Manager', 'Chef', 'Electrician', 'Carpenter',
       'Doctor', 'Lab Technician', 'Data Analyst', 'Lawyer',
       'Content Writer'], Field(...,description='occupation of the user')]
        
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/((self.height/100)**2)

    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi >30:
            return "high"
        elif self.smoker and self.bmi >27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self) ->str:
        if self.age< 25:
            return "young"
        elif self.age< 45:
            return "adult"
        elif self.age<60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1 
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
    @computed_field
    @property
    def income_category(self)->int:
        if self.income_lpa < 6:
            return 4
        elif self.income_lpa < 12:
            return 3
        elif self.income_lpa < 22:
            return 2
        else:
            return 1
    
@app.post('/predict')
def predict_premium(data: UserInput):

    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk' : data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_category': data.income_category,
        'occupation' : data.occupation
    }])

    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200 ,content={'predicted_category': prediction} )