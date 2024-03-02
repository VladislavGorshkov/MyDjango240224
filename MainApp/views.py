from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def home(request):
    #text = """<h1>"Изучаем django"</h1> 
    #       <strong>Автор</strong>: <i>Горшков В.В.</i>"""
    #return HttpResponse(text)
    context={"name":"Петров иван Николаевич",
              "email":"mymail@mail.ru",}
    return render(request,'index.html',context)

author = {
      "Имя":" Иван",
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
         "телефон": "8-923-600-01-02",
         "email": "vasya@mail.ru"}

ITEMS = [
      {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
      {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
      {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
      {"id": 7, "name": "Картофель фри" ,"quantity":0},
      {"id": 8, "name": "Кепка" ,"quantity":124}
     ]

def about(request):

    text=f"""
    <header>
        <a href="/"> Домой / <a>
        <a href="/items"> Список товаров / <a>
        <a href="/about">About</a>
    </header>    
    <p>Имя:<strong>{author["Имя"]} </strong></p>
              <p>Отчество:<strong>{author["Отчество"]} </strong></p>
              <p>Фамилия:<strong>{author["Фамилия"]} </strong></p>
              <p>Телефон:<strong>{author["телефон"]} </strong></p>
              <p>e-mail:<strong>{author["email"]} </strong></p>
          
    

    """
    return HttpResponse(text)

def get_item(request,item_id:int):
    # """По указанному ID вернуть имя и количество"""
    item = next((item for item in ITEMS if item['id']==item_id),None)
    if item is not None:
        context = {"item":item}
        return render(request,'item.html',context)
    return HttpResponseNotFound(f'Товар itemid={item_id} не найден')

def get_items(request):
    # """Возвращаем список товаров"""
    # text='<h1>Списко товаров<h1><ol>'
    # for item in items:
    #     text += f"""<li> <a href="/item/{item['id']}">{item['name']}</a></li>"""
    # text+='</ol>'
    # return HttpResponse(text)
    context={"goods":ITEMS}
    return render(request,'items.html',context)


 


