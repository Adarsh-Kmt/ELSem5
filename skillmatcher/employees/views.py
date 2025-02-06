from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import numpy as np

@api_view(['GET'])
def search_employee(request):
    skills_query = request.GET.get('skills', '').strip().lower()
    if not skills_query:
        return Response({"message": "No skills provided"})

    employees = list(Employee.objects.all())  

    if not employees:
        return Response({"message": "No matching employees found"})
    
    skills_list = [emp.skills.lower() for emp in employees]
    vectorizer = TfidfVectorizer()
    skill_vectors = vectorizer.fit_transform(skills_list)
    query_vector = vectorizer.transform([skills_query])
    
    knn = NearestNeighbors(n_neighbors=5, metric='cosine')
    knn.fit(skill_vectors)
    distances, indices = knn.kneighbors(query_vector)

    matched_employees = [
        employees[int(i)] for idx, i in enumerate(indices[0]) if distances[0][idx] < 2
    ]

    if matched_employees:
        return Response(EmployeeSerializer(matched_employees, many=True).data)
    else:
        return Response({"message": "No matching employees found"})
