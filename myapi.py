from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

students ={
    1:{
        "name": "john",
        "age": 17
    }
}

# GET 
# POST 
# PUT 
# DELETE 
#you already know all meaningss hehhehe


class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
@app.get('/')
def index():
    return {"name":"First Data"}

# /get-student/1---> get particular student

@app.get("/get-student/{student_id}")
def get_student(student_id: int ):
    return students[student_id]

@app.get("/get-by-name")
def get_student(name: str = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"error" : "Student not found."}

@app.get("/get-by-age")
def get_student(age: int):
    for student in students:
        if students[student]["age"] == age:
            return students[student]
        return {"error": "no student with this age found"}
        
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "A student with this ID already exists."}
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"error": "The student does not exist."}
    
    if student.name != None:
        student[student_id].name = student.name
    
    if student.age != None:
        student[student_id].age = student.age

    if student.year != None:
        student[student_id].year = student.year


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "The student does not exist."}
    del students[student_id]
    return {"message": "deletion successfull"}