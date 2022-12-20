from django.shortcuts import render
import pandas as pd
from django.core.paginator import Paginator

def homePage(request):

    return render(request, 'home.html')

def count(drug):

    df = pd.read_csv('data.csv')
    count = 0

    for i in list(df['취급마약']):
        if drug in i:
            count += 1

    return count


def search(drugs):

    df = pd.read_csv('data.csv')
    tmp = []
    for i in range(len(df)):
        drugTmp = set(df['취급마약'][i].split(','))
        drugs = set(drugs)
        if drugs == drugTmp:
            tmp.append(i)

    return df.loc[tmp].reset_index(drop=True)

def list_to_str(list):

    result = list[0]
    list = list[1:]
    if len(list) != 0:
        for i in list:
            result += "," + i

    return result

def dataPage(request):

    df = pd.read_csv('data.csv')

    labels = ['필로폰', '대마', '엑스터시', '야바', '케타민', '코카인', 'LSD', '프로포폴', 'GHB', '펜타닐']
    data = [count('필로폰'), count('대마'), count('엑스터시'), count('야바'), count('코카인'), count('LSD'), count('프로포폴'), count('GHB'), count('펜타닐')]

    context = {

        'labels': labels,
        'data' : data

    }


    return render(request, 'data.html', context)



def searchPage(request):

    request.session.flush()

    return render(request, 'search.html')


def piePage(request):

    request.session.flush()

    drugs = request.GET.getlist('drug')

    if len(drugs) == 0:
        return render(request, 'error.html')

    request.session['drugs'] = drugs

    df = search(drugs)

    if len(df) != 0:
        a, b, c = [], [], []
        for i in range(len(df)):
            if df['형종'][i] == '징역형':
                a.append(i)
            elif df['형종'][i] == '집행유예형':
                b.append(i)
            elif df['형종'][i] == '벌금형':
                c.append(i)
        labels = ['징역형', '집행유예형', '벌금형']
        data = [len(a), len(b), len(c)]

        drugs = list_to_str(drugs)

        context = {
            'drugs': drugs,
            'labels': labels,
            'data': data
        }

        return render(request, 'pie.html', context)

    else:

        return render(request, 'none.html')

def chartPage(request):

    drugs = request.session['drugs']
    type = request.GET.get('type')

    if type == None:

        try:
            type = request.session['type']
            labels = request.session['labels']
            data = request.session['data']

            if type == "징역형":

                drugs = list_to_str(drugs)

                context = {
                    'drugs': drugs,
                    'type': type,
                    'labels': labels,
                    'data': data
                }

                return render(request, 'chartA.html', context)

            elif type == "집행유예형":

                drugs = list_to_str(drugs)

                context = {
                    'drugs': drugs,
                    'type': type,
                    'labels': labels,
                    'data': data
                }

                return render(request, 'chartB.html', context)

            else:

                drugs = list_to_str(drugs)

                context = {
                    'drugs': drugs,
                    'type': type,
                    'labels': labels,
                    'data': data
                }

                return render(request, 'chartC.html', context)

        except:

            return render(request, 'error.html')




    request.session['type'] = type

    df = search(drugs)

    result = []
    if type == "징역형":
        for i in range(len(df)):
            if df['형종'][i] == '징역형':
                result.append(df['형량범위'][i])
        if len(result) == 0:
            return render(request, 'none.html')
        labels = ['1년미만', '1년-2년', '2년-3년', '3년-5년', '5년-7년', '7년-10년', '10년이상']
        data = [result.count('1년미만'), result.count('1년-2년'), result.count('2년-3년'), result.count('3년-5년'), result.count('5년-7년'), result.count('7년-10년'), result.count('10년이상')]

        request.session['labels'] = labels
        request.session['data'] = data

        drugs = list_to_str(drugs)

        context = {
            'drugs': drugs,
            'type': type,
            'labels': labels,
            'data': data
        }

        return render(request, 'chartA.html', context)

    elif type == "집행유예형":
        for i in range(len(df)):
            if df['형종'][i] == '집행유예형':
                result.append(df['형량범위'][i])
        if len(result) == 0:
            return render(request, 'none.html')
        labels = ['1년미만', '1년', '2년', '3년', '4년', '5년이상']
        data = [result.count('1년미만'), result.count('1년'), result.count('2년'), result.count('3년'), result.count('4년'), result.count('5년이상')]

        request.session['labels'] = labels
        request.session['data'] = data

        drugs = list_to_str(drugs)

        context = {
            'drugs': drugs,
            'type': type,
            'labels': labels,
            'data': data
        }

        return render(request, 'chartB.html', context)

    elif type == "벌금형":
        for i in range(len(df)):
            if df['형종'][i] == '벌금형':
                result.append(df['형량범위'][i])
        if len(result) == 0:
            return render(request, 'none.html')

        labels = ['1백만원미만', '1백만원-2백만원', '2백만원-3백만원', '3백만원-5백만원', '5백만원-7백만원', '7백만원-1천만원', '1천만원이상']
        data = [result.count('1백만원미만'), result.count('1백만원-2백만원'), result.count('2백만원-3백만원'), result.count('3백만원-5백만원'), result.count('5백만원-7백만원'), result.count('7백만원-1천만원'), result.count('1천만원이상')]

        request.session['labels'] = labels
        request.session['data'] = data

        drugs = list_to_str(drugs)

        context = {
            'drugs': drugs,
            'type': type,
            'labels': labels,
            'data': data
        }

        return render(request, 'chartC.html', context)

def precedent(request):

    drugs = request.session['drugs']
    type = request.session['type']
    sentence = request.GET.get('sentence')

    if sentence == None:
        return render(request, 'error.html')

    request.session['sentence'] = sentence

    df = search(drugs)

    facts = []
    precedent = []
    page = 1

    for i in range(len(df)):
        if df['형종'][i] == type and df['형량범위'][i] == sentence:
            precedent.append(df['판례원본'][i])
            facts.append(df['범죄사실'][i])

    if len(precedent) == 0:
        return render(request, 'none.html')

    drugs = list_to_str(drugs)

    request.session['precedent'] = precedent
    request.session['facts'] = facts
    request.session['page'] = page
    request.session['total'] = len(precedent)


    context = {
        'drugs': drugs,
        'facts': facts[page-1],
        'type': type,
        'sentence': sentence,
        'precedent': precedent[page-1],
        'page': page,
        'total': len(precedent)
    }

    return render(request, 'precedent.html', context)

def nextPage(request):

    drugs = request.session['drugs']
    type = request.session['type']
    sentence = request.session['sentence']
    precedent = request.session['precedent']
    facts = request.session['facts']
    page = request.session['page']

    page += 1

    if len(precedent) < page:
        return render(request, 'done.html')

    else:

        drugs = list_to_str(drugs)

        request.session['page'] = page
        request.session['total'] = len(precedent)

        context = {
            'drugs': drugs,
            'type': type,
            'sentence': sentence,
            'precedent': precedent[page-1],
            'facts': facts[page-1],
            'page': page,
            'total': len(precedent)
        }

        return render(request, 'precedent.html', context)




