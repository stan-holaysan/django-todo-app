from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def query_huggingface_api(prompt, retries=5):
    # Replace 'your_hugging_face_api_token' with your actual Hugging Face API token
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {
        "Authorization": "Bearer " + os.getenv("HUGGINGFACE_API_KEY"),
        # "x-wait-for-model": "true"
    }

    # Make the request
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt},
    )

    if response.status_code == 200:
        response = response.json()[0]["generated_text"]
        edited_response = response.split('\n', 1)[1] if '\n' in response else response
        return edited_response
    else:
        return f"Error: {response.status_code}, {response.json()}"

# List all todo items
def todo_list(request):
    form = TodoForm()
    todo_list = Todo.objects.filter(status=False)
    page = {
        "form": form,
        "todo_list": todo_list,
    }
    return render(request, 'todo/index.html', page)

# Create a new todo item
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            prompt = "Create a fun, humorous description for this to-do item: \"" + title + "\"."
            llm_response = query_huggingface_api(prompt)
            print(type(llm_response))
            print(llm_response)

            form = Todo(
                title=title,
                status=False,
                llm_response=llm_response
            )
            form.save()
            return redirect('todo:todo_list')

# Mark todo item as done
def todo_done(request, todo_id):
    Todo.objects.filter(id=todo_id).update(status=True)
    return redirect('todo:todo_list')
