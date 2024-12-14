from django.shortcuts import render

# Create your views here.
def process_number(request):
    if request.method == 'POST':
        user_input = request.POST.get('number')  # Get the input from the form
        try:
            number = int(user_input)  # Convert input to integer
            result = f"You entered the number: {number}"
        except ValueError:
            result = "Invalid input. Please enter a valid number."
        return render(request, 'index.html', {'result': result})
    return render(request, 'index.html') 