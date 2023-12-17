from django.shortcuts import render
from joblib import load

model = load('model.joblib')


def irisPredict(request):
    if request.method == "POST":
        sepal_length = request.POST['sepal length']
        sepal_width = request.POST['sepal width']
        petal_length = request.POST['petal length']
        petal_width = request.POST['petal width']
        
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])      

        if prediction[0] == 0:
            result = "Setosa"
        elif prediction[0] == 1:
            result = "Versicolor"
        else:
            result = "Virginica" 
        return render(request, 'main.html', {'result' : result})
    return render(request, 'main.html')


