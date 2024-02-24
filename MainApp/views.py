from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    text = """<h1>"Изучаем django"</h1> 
           <strong>Автор</strong>: <i>Горшков В.В.</i>"""
    return HttpResponse(text)

author = {
      "Имя":" Иван",
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
         "телефон": "8-923-600-01-02",
         "email": "vasya@mail.ru"}

items = [
      {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
      {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
      {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
      {"id": 7, "name": "Картофель фри" ,"quantity":0},
      {"id": 8, "name": "Кепка" ,"quantity":124}
     ]

def about(request):

    text=f"""<p>Имя:<strong>{author["Имя"]} </strong></p>
              <p>Отчество:<strong>{author["Отчество"]} </strong></p>
              <p>Фамилия:<strong>{author["Фамилия"]} </strong></p>
              <p>Телефон:<strong>{author["телефон"]} </strong></p>
              <p>e-mail:<strong>{author["email"]} </strong></p>
          
    """
    return HttpResponse(text)

def fnames(request,id):
    text = "<b>Нет такого товара</b>"
    for t in items:
        #text += str(t["id"]==id)
         if t["id"]==id:
             text = f'<b>name={t["name"]}, quantity={t["quantity"]}</b>'
  
    return HttpResponse(text)


