import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from tablib import Dataset
from .forms import SignupUser, LoginForm
from .models import Phase1, Phase2, Phase3, Phase4, Phase5


def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "index.html")
    return redirect("login")


def user_signup(request):
    if request.method == "POST":
        form = SignupUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SignupUser()
    return render(request, "signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")

    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def upload_marks(request):
    if request.method == "POST":
        # phase marks file
        file = request.FILES["file"]
        extension = os.path.splitext(file.name)[-1].lower()
        print(extension)
        if extension not in [".csv", ".xlsx", ".xls"]:
            return redirect("upload_marks")

        # phase number
        phase_choice = request.POST.get("phase_choice")

        phase_models = {
            "phase1": Phase1,
            "phase2": Phase2,
            "phase3": Phase3,
            "phase4": Phase4,
            "phase5": Phase5,
        }
        model_class = phase_models.get(phase_choice)
        if not model_class:
            return HttpResponse("Invalid phase selected", status=400)

        dataset = Dataset()
        imported_data = dataset.load(file.read(), format="xlsx")

        for data in imported_data:
            try:
                if phase_choice == "phase1":
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        criteria_e=data[6],
                        criteria_f=data[7],
                        score=data[8],
                        year=data[9],
                    )
                elif phase_choice == "phase2":
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        criteria_e=data[6],
                        score=data[7],
                        year=data[8],
                    )
                elif phase_choice == "phase3":
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        criteria_e=data[6],
                        score=data[7],
                        year=data[8],
                    )
                elif phase_choice == "phase4":
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        criteria_e=data[6],
                        criteria_f=data[7],
                        score=data[8],
                        year=data[9],
                    )
                elif phase_choice == "phase5":
                    value = model_class(
                        usn=data[0],
                        name=data[1],
                        criteria_a=data[2],
                        criteria_b=data[3],
                        criteria_c=data[4],
                        criteria_d=data[5],
                        score=data[6],
                        year=data[7],
                    )

                value.save()
            except IndexError as e:
                print(f"Error processing row {data}: {e}")
                continue
            
        return redirect("view_marks")

    return render(request, "upload.html")


def view_marks(request):
    return render(request, "view_marks.html")


def search(request):
    """
    TODO: REPLACE THE DUMMY DATA AND FETCH DATA FROM THE MODELS DECALRED IN MODELS FILE
    """
    dummy_data = [
        {"name": "Alice Johnson", "usn": "USN001", "marks": "85"},
        {"name": "Bob Smith", "usn": "USN002", "marks": "78"},
        {"name": "Charlie Brown", "usn": "USN003", "marks": "92"},
        {"name": "Diana Green", "usn": "USN004", "marks": "67"},
    ]
    if request.method == "GET":
        query = request.GET.get("usn")
        if query:
            results = [
                record
                for record in dummy_data
                if query.lower() in record["usn"].lower()
            ]
        else:
            results = []

        return render(request, "view_marks.html", {"results": results})
