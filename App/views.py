from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Crop, Field, Harvest
from datetime import datetime
from . import db
import json
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        field = request.form.get('field')
        crop = request.form.get('crop')
        harvest = request.form.get('harvest')
        date = request.form.get('date')

        user_id =current_user.id

       # Create a new entry in the Crop table associated
        new_entry = Crop(name=crop, user_id=user_id)
        db.session.add(new_entry)
        db.session.commit()
        
        # Create a new entry in the Field table associated with the crop
        new_field = Field(name=field, crop=new_entry)
        db.session.add(new_field)
        db.session.commit()
        
        # Create a new entry in the Harvest table associated with the field
        new_harvest = Harvest(crop_yield=harvest, date=datetime.strptime(date, '%Y-%m-%d'), field=new_field)
        db.session.add(new_harvest)
        db.session.commit()

    crops = Crop.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', crops=crops)