from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')
@app.route('/flag')
def flag():
   # Only check for XHR header
   if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
       return "SecurinetsEPS{J5_D0M_M4N1P_Is_FuN}"
   return "Nice Try! ama it ain't that easy sucker ahhahahaha"
if __name__ == "__main__":
   app.run(debug=False)