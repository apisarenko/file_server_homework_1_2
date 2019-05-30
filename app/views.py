import datetime
import os

from django.shortcuts import render
from app import settings


def file_list(request, year=None, month=None, day=None):
    template_name = 'index.html'
    list_of_files = []
    file_name_list = os.listdir(settings.FILES_PATH)
    for file_name in file_name_list:
        file_data = {}
        file_data['name'] = file_name
        file_discript = os.stat('files/' + file_name)
        file_data['ctime'] = datetime.date.fromtimestamp(file_discript.st_ctime)
        file_data['mtime'] = datetime.date.fromtimestamp(file_discript.st_mtime)
        list_of_files.append(file_data)
    context = {
        'files': list_of_files,
        'date': None
    }

    if year is not None:
        context.clear()
        out_file_list = []
        url_date = datetime.date(year, month, day)
        for file in list_of_files:
            if file['mtime'] == url_date:
                out_file_list.append(file)
        context = {
            'files': out_file_list,
            'date': url_date
        }

    return render(request, template_name, context)


def file_content(request, name):
    with open('files/' + name, 'r') as file:
        content = file.read()
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )
