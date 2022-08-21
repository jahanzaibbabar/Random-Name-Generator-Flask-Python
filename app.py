import names
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def name_generator():
    name = names.get_full_name(gender='female')
    return render_template("index.html", Name = name)
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)


