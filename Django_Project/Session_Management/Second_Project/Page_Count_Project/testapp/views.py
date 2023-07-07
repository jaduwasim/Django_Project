from django.shortcuts import render

# Create your views here.
def Page_Count_View(request):
    count = request.session.get('count',0)
    new_count = count + 1
    request.session['count'] = new_count
    request.session.set_expiry(60)
    print(f'Age of Expiry: {request.session.get_expiry_age()} Seconds')
    print(f'Date of Expiry: {request.session.get_expiry_date()}')
    return render(request, 'testapp/pagecount.html', {'count':new_count})