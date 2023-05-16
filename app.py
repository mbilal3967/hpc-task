from flask import Flask, render_template, request, redirect, url_for

import re

app = Flask(__name__)

# Mock database
ships = []

# Regular expression pattern for validating ship code
ship_code_pattern = re.compile(r'^[A-Za-z]{4}-\d{4}-[A-Za-z]\d$')

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Create a ship
@app.route('/ships', methods=['POST'])
def create_ship():
    name = request.form['name']
    length = request.form['length']
    width = request.form['width']
    code = request.form['code']
    
    if not ship_code_pattern.match(code):
        return 'Invalid ship code. Please use the format AAAA-1111-A1.'
    
    ship = {'name': name, 'length': length, 'width': width, 'code': code}
    ships.append(ship)
    return redirect(url_for('get_ships'))

# Get all ships
@app.route('/ships', methods=['GET'])
def get_ships():
    return render_template('ships.html', ships=ships)

# Get a single ship by code
@app.route('/ships/<string:code>', methods=['GET'])
def get_ship(code):
    for ship in ships:
        if ship['code'] == code:
            return render_template('ship.html', ship=ship)
    return 'Ship not found'

# Update a ship
@app.route('/ships/<string:code>', methods=['POST'])
def update_ship(code):
    for ship in ships:
        if ship['code'] == code:
            ship['name'] = request.form['name']
            ship['length'] = request.form['length']
            ship['width'] = request.form['width']
            return redirect(url_for('get_ships'))
    return 'Ship not found'

# Delete a ship
@app.route('/ships/<string:code>/delete', methods=['POST'])
def delete_ship(code):
    for ship in ships:
        if ship['code'] == code:
            ships.remove(ship)
            return redirect(url_for('get_ships'))
    return 'Ship not found'

# Edit a ship
@app.route('/ships/<string:code>/edit', methods=['GET'])
def edit_ship(code):
    for ship in ships:
        if ship['code'] == code:
            return render_template('edit_ship.html', ship=ship)
    return 'Ship not found'

if __name__ == '__main__':
    app.run(debug=True)
