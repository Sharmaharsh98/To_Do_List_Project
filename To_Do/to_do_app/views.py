from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import io



###############################################


def index(request):

	item_list = Todo.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = TodoForm()

	context = {
		"forms": form,
		"list": item_list,
		"title": "TODO LIST",
	}
	return render(request, 'to_do_app/index.html', context)


def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')

def update(request, pk):
	instance = get_object_or_404(Todo, pk=pk)
	if instance.status == 'Completed':
		instance.status = 'Pending'
		instance.save()
		return redirect('todo')
	elif instance.status == 'Pending':
		instance.status = 'Completed'
		instance.save()
		return redirect('todo')


def generate_pdf(request):

	buf = io.BytesIO()
	# Canvas
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# creating object of text
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)
	# data from model
	data = Todo.objects.all()
	
	for item in data:
		textob.textLines(str(item.title))
		textob.textLines(str(item.details))
		textob.textLines(str(item.date))
		textob.textLines(str(item.status))
		textob.textLines("---------------------------------------------------")

	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	return FileResponse(buf, as_attachment=True, filename='data.pdf')
		



# To update data once for all with one button
""" 
def update(request, pk):
    data = get_object_or_404(Todo, id=pk)
    data.status = 'Completed'
    data.save()
    # messages.info(request, "Item Updated")
    return redirect('todo')
"""
    
