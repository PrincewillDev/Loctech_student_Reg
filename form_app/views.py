from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import JsonResponse
import json

# path to the json file for storage
JSON_FILE_PATH = os.path.join(os.path.dirname(__file__), 'storage.json')

# Create your views here.
def home(request):
    return render(request, 'index.html')

print(f"JSON file path: {JSON_FILE_PATH}") 

def load_students():
    """Load students data from the JSON file."""
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_students(data):
    """Save students data to the JSON file."""
    try:
        with open(JSON_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data to JSON file: {e}")

@csrf_exempt
def register_student(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            # Extract and process the data
            student_data = {
                "name": data.get("name"),
                "email": data.get("email"),
                "address": data.get("address"),
                "qualification": data.get("qualification"),
                "next_of_kin": data.get("next_of_kin"),
                "course": data.get("course"),
                "occupation": data.get("occupation"),
                "hear_about_us": data.get("hear_about_us"),
                "amount": data.get("amount"),
                "state_of_origin": data.get("state_of_origin"),
                "course_duration": data.get("course_duration"),
                "start_date": data.get("start_date"),
                "instructor": data.get("instructor"),
                "type_of_training": data.get("type_of_training"),
                "payment_plan": data.get("payment_plan"),
                "registering_officer": data.get("registering_officer"),
                "date": data.get("date")
            }
            students = load_students()
            students.append(student_data)
            save_students(students)

            return JsonResponse({"status": "success",
                                 "student_data": student_data
                                 },
                                status=201)
            # return JsonResponse(student_data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)


def list_students(request):
    students = load_students()
    return JsonResponse(students, safe=False)


