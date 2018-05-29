# Dev330x
# Python: Creating Scalable, Robust, Interactive Code
# I am learning python

from datetime import datetime, date, timedelta

now = datetime.today()
today = date(year=now.year, month=now.month, day=now.day)
bdate = date(year=1998, month=3, day=4)
about = {"name": "Mike Angelo Saraus", "age": today.year-bdate.year, "sex": "Male", "Hobbies": ["Writing codes, Solving Math Problems, Doing something new!"]}

print("Hello, my name is {:s}, {:s} year old.\nMy hobbies are: {:}".format(str(about['name']), str(about['age']), list(map(lambda x: x,about['Hobbies']))))
