from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.material import Material
from flask_app.models.user import User








@app.route('/new_material')
def show_blank_material_form():
    user = User.fetch_account_info({'id': session['logged_in']})
    return render_template('add-material.html', user = user)


@app.route('/add_material', methods=['POST'])
def add_material():
    Material.add_new_material(request.form)
    return redirect('/dashboard')
    



@app.route('/view_material/<int:material_id>')
def view_material(material_id):
    data = {
        'id': material_id
    }
    material = Material.get_one_material(data)
    user = User.fetch_account_info({'id': session['logged_in']})
    return render_template('view-material.html', user = user, material = material)



@app.route('/edit_material/<int:material_id>')
def show_edit_page(material_id):
    data = {
        'id': material_id
    }
    user = User.fetch_account_info({'id': session['logged_in']})
    return render_template('edit-material.html', material = Material.get_one_material(data), user = user)



@app.route('/save_material_changes', methods=['POST'])
def save_material_changes():
    Material.update_material(request.form)
    return redirect('/dashboard')



@app.route('/delete_material/<int:material_id>')
def delete_material(material_id):
    data = {
        'id':material_id
    }
    Material.delete_material(data)
    return redirect('/dashboard')