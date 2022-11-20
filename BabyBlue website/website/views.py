from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import  login_required,current_user
from .models import Note
from . import db,data
import json

views = Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
	if(request.method=='POST'):
		text=request.form.get('note')

		if len(text)< 2:
			flash('Text too short!',category='Error')
		else:
			new_note=Note(text=text.upper(), user_id=current_user.id)
			db.session.add(new_note)
			db.session.commit()
			flash('Product added', category='Success')

	return render_template("home.html",user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
	note =json.loads(request.data)
	noteId=note['noteId']
	note=Note.query.get(noteId)
	if note:
		if note.user_id == current_user.id:
			db.session.delete(note)
			db.session.commit()
	
	return jsonify({})

@views.route('/checkout')
def checkout():
	price=0
	user=current_user
	lista=[]

	for note in user.notes:
		minPrice=1000.0
		minName=str
		for product in data:
			if note.text in product['name']:
				if minPrice > product['price']:
					minPrice=product['price']
					minName=product['name']
		if minPrice!=1000:
			lista.append([minName,minPrice])
			price+=minPrice
		

		

	return render_template("checkout.html",user=current_user,price=price,lista=lista)