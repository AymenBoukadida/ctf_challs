from flask import Flask, render_template, jsonify, session, request, abort
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Secure secret key for session management

# Route to render the index page
@app.route('/')
def index():
    # Reset session variables when the game starts
    session['can_access_flag'] = False
    return render_template('index.html')

# Route to serve the flag (restricted access)
@app.route('/get_flag', methods=['GET'])
def get_flag():
    if session.get('can_access_flag', False):  # Check if access is granted
        flag = "SecurinetsEPS{Qu33n_4nd_Jc4ks}"
        return jsonify({"flag": flag})
    else:
        return jsonify({"error": "Access denied"}), 403

# Route to grant access to the flag (called when the Queen is found)
@app.route('/grant_flag_access', methods=['POST'])
def grant_flag_access():
    session['can_access_flag'] = True  # Grant access to the flag
    return jsonify({"message": "Access granted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
