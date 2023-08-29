import csv
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from change_csv.forms import SdelkaForm, UploadFileForm
import psycopg2
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.validators import MaxValueValidator, MinValueValidator
from change_csv.models import CounterAgent, Sdelka


def create_csv_model(request, ddata):
    context = {'ddata': ddata}
    return render(request, 'change_csv/creating_csv_model.html', context)

class SomeText(forms.Form):
    text = forms.CharField(required=False)
    number = forms.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)], required=False )
    # class Meta:
    #     model = Person
    #     fields = ['text', 'number']

def read_file_create_model(request):
    
    filename  = 'telephone_spravochnik.csv'
    # print('8888888888888888888')
    conn = psycopg2.connect(
                database="change_csv1",
                user='andrey_mazo',
                password='123456',
                host='localhost',
                port='5432'
            )
    #psql -h /tmp
    conn.autocommit = True
            # Creating a cursor object
    cursor = conn.cursor()

            # query to create a table
            # sql = '''drop table locations'''
            # sql = ''' CREATE TABLE locations (zip INT, latitude FLOAT, longtitude FLOAT, city VARCHAR(50), state VARCHAR(50)); '''
            # sql = '''truncate table locations restart identity cascade'''

            # cursor.execute(sql)
            ##################################################################

    # with open(filename, 'r', encoding='utf-8') as f:
    #         data = csv.reader(f, delimiter=',')
    #         context = {}
    #         lst_context  = []
    #         index = 1
    #         for i in next(data):  ##Zapoliaem suppliers
    #             context.update({f'{index}':i})
    #             lst_context.append({index:i})
    #             index += 1
    #         print(context)
    #         print(lst_context)
            #####################################################################

    import pandas as pd
# Load the xlsx file
    excel_data = pd.read_excel('telephone_spravochnik2.xls', engine='xlrd')
    print('len(excel_data.columns), len(excel_data, )', len(excel_data.columns), len(excel_data))
    # Read the values of the file in the dataframe
    # data = pd.DataFrame(excel_data, columns=['1', '2 Тип', '3 Этап', '4 Контрагент', '5(1) Номер договора','6(1) Дс №', '7(1) ДС (текстовый формат для документов)' ,'8(1) Должник/Собственник' ,'9 Название' ,'10 Примечание' ,'11(1) Задание' ,'12(1) Запросы', '13 Сумма' ,'14(2) Номер отчета' ,'15(2) Дата льчета' , '16(2) Дата оценки' , '17(3) Наличие титула' , '18(2) РС', '19(2) Оценщик', '20', '21', '22', '23', '24', '25', '25', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56'])
    # Print the content

    # print("The content of the file is:\n", excel_data.columns)
    H=set()
    ############################Zapolnyaem CounterAgent############################
    # for i in range(len(excel_data.columns)):
    #     print(excel_data.loc[i][3])
    #     if not excel_data.loc[i][3] in H:
    #         H.add(excel_data.loc[i][3])
    #         counteragent = CounterAgent.objects.create(name=excel_data.loc[i][3])
    #         counteragent.save()
    #############################Zapolnyaem Sdelka##############
    for i in range(len(excel_data.columns)):
        print(excel_data.loc[i][4])
        if not excel_data.loc[i][4] in H:
            H.add(excel_data.loc[i][4])
            sdelka = Sdelka.objects.create(name=excel_data.loc[i][4])
            sdelka.save()

        
    # print(H)
    


    # print(excel_data.loc[3][3]) # Тип
            # print(context.get('1'))#{'1': 'FIO', '2': ' Organization', '3': ' tel number 1', '4': 'tel number 2'}
                # cursor.execute(
                #     'INSERT INTO locations( "zip", "latitude", "longtitude", "city", "state") VALUES (%s, %s, %s, %s, %s)',
                #     (i[0], i[1], i[2], i[3], i[5].split(',')[0]))

            # sql = '''insert into table locations '''
            # executing above query

    # print("Table has been created successfully!!")
    # context = {'context':context.get('1')}

            # Closing the connection
    conn.close()
    # form_some_text = SomeText(request.POST)
    form = SomeText(request.POST)
    context = {
                #'lst_context':lst_context,
                'object_list': Sdelka.objects.all,
                'form': form,
                # 'form_some_text':form_some_text
                }
    if request.method == "POST":
        
        # print('form.errors', form.errors )
        # some_text.fields['number'].required = False
        # some_text.fields['text'].required = False
        if form.is_valid():
            
            cc = form['number'].value()
    
            # c = some_text['text'].value()#.cleaned_data.get('text')
            # c = some_text['text'].value()#
            c = form.cleaned_data.get('text')
            # context = {'lst_context':lst_context,
            #     'object_list': Person.objects.all,
            #     # 'some_text': some_text,
            #     'c':c}
            # print('c c c c c c c c c c c ', c)
            # print('cc cc cc ', cc)
        else:
            form = SomeText()
        # print('4c c c c c c c c c c c ', c)
        # print('4cc cc cc ', cc)

    return render(request, "change_csv/creating_csv_model.html", context)
def get_form(request):
     if request.method == "POST":
        form_some_text = SomeText(request.POST)
        if form_some_text.is_valid():
            # c = some_text['text'].value()#.cleaned_data.get('text')
            c = form_some_text.cleaned_data['text']
            # print('ccccccccccc', c)
            context= {'c': c}
    
        return render(request, "change_csv/creating_csv_model.html", context)

# class NumberQuestion(forms.Form):
#     number = forms.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)], )

# def render_api_question(request):
#     number_form = NumberQuestion(request.POST)
#     queryset = {'object_list': Question.objects.all,
#                 'number_form': number_form}
#     if request.method == "POST":
#         # form = NumberQuestion(request.POST)
#         if number_form.is_valid():
#             c = number_form['number'].value()
#             url = f'https://jservice.io/api/random?count={c}'
#             response = requests.get(
#                 url,
#                 params={'count': f'{c}'},
#             )
#             if response.status_code == 200:
#                 a = response.json()
#                 for i in range(0, int(c)):
#                     values = Question.objects.create(
#                         body=a[i].get('question'),
#                         answer=a[i].get('answer'),
#                         question_value=a[i].get('value'), )
#                     print('values.body', values.body)
#                     if proverka_unik(values.body):
#                         raise ValueError("Вопроc уже был")
#                     values.save()

#         else:
#             number_form = NumberQuestion()

#     return render(request, 'spa_table/users.html', queryset)


class CreateField(CreateView):
    model = Sdelka
    queryset = Sdelka.objects.all()
    form_class = SdelkaForm
    success_url = reverse_lazy('change_csv:read_file_create_model')
# def create_field(request):
     
#      if request.method == "POST":
#         # form = NumberQuestion(request.POST)
#         if some_text.is_valid():
#             c = number_form['number'].value()
#         pass

class UpdateField(UpdateView):
    model = Sdelka
    form_class = SdelkaForm
    success_url = reverse_lazy('change_csv:read_file_create_model')
    # template_name = 'catalog/product_form.html'
    
class DeleteField(DeleteView):
    model = Sdelka
    form_class = SdelkaForm
    success_url = reverse_lazy('change_csv:read_file_create_model')
    template_name = 'change_csv/field_confirm_delete.html'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)



def add_field(request):
    pass
def delete_field(request):
    pass


# Imaginary function to handle an uploaded file.
def handle_uploaded_file(f):
    with open("telephone_spravochnik.csv", "rb+") as destination:
        # print('----------------------')
        with open("telephone_spravochnik2.xls", "wb+") as destination2:
            for chunk in f.chunks():
                # print('----------------------', type(chunk))
                destination2.write(chunk)


def upldfile(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("read_file_create_model/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


# def handle_uploaded_file(f):
#     with open("telephone_spravochnik.csv", "wb+") as destination:
#         print('----------------------')
#         for chunk in f.chunks():
#             print('----------------------', chunk)
#             destination.write(chunk)


# def upldfile(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES["file"])
#             return HttpResponseRedirect("/")
#     else:
#         form = UploadFileForm()
#     return render(request, "upload.html", {"form": form})