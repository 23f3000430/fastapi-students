
import csv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
def get_students(class_: list[str] = Query(default=[], alias="class")):
    with open("q-fastapi.csv", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    for student in students:
        student["studentId"] = int(student["studentId"])

    if class_:
        students = [
            student for student in students
            if student["class"] in class_
        ]

    return students


