from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    #text = """<h1>"Изучаем django"</h1> 
    #       <strong>Автор</strong>: <i>Горшков В.В.</i>"""
    #return HttpResponse(text)
    context={"name":"Петров иван Николаевич",
              "email":"mymail@mail.ru",}
    return render(request,'index.html',context)



def about(request):
    author = {
      "Имя":" Иван",
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
         "телефон": "8-923-600-01-02",
         "email": "vasya@mail.ru"}
    
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
    try:
       item = Item.objects.get(id = item_id )# next((item for item in items if item.id==item_id),None)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Товар itemid={item_id} не найден')
    else:
        context = {"item":item}
        return render(request,'item.html',context)
    

def get_items(request):
    # """Возвращаем список товаров"""
    # text='<h1>Списко товаров<h1><ol>'
    # for item in items:
    #     text += f"""<li> <a href="/item/{item['id']}">{item['name']}</a></li>"""
    # text+='</ol>'
    # return HttpResponse(text)
    items = Item.objects.all()
    context={"items":items}
    return render(request,'items.html',context)


 


