from django.shortcuts import render, redirect
from .modules import Drug


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        disease = request.POST.get('disease')
        referencenum = request.POST.get('referencenum')
        quantity = request.POST.get('quantity')
        dosage = request.POST.get('dosage')
        price = request.POST.get('price')

        query = Drug.objects.create(name=name, disease=disease, referencenum=referencenum, quantity=quantity,
                                    dosage=dosage, price=price)
        query.save()
        return redirect("/")
    return render(request, "index.html")


# function to delete data
def deleteData(request, id):
    d = Drug.objects.get(id=id)
    d.delete()
    return redirect("/")

    return render(request, "index.html")


# Function to update the records

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        disease = request.POST.get('disease')
        referencenum = request.POST.get('referencenum')
        quantity = request.POST.get('quantity')
        dosage = request.POST.get('dosage')
        price = request.POST.get('price')

        edit_data = Drug.objects.get(id=id)
        edit_data.name = name
        edit_data.disease = disease
        edit_data.referencenum = referencenum
        edit_data.quantity = quantity
        edit_data.dosage = dosage
        edit_data.price = price
        edit_data.save()

        return redirect("/")

    dta = Drug.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)


def indexpage(request):
    data = Drug.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)
