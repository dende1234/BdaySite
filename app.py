from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'super secret key'

SECRET_CODE = '4509'

@app.route('/')
def home():
    if 'authenticated' in session and session['authenticated']:
        return render_template('success.html')
    return render_template('login.html')

@app.route('/verify', methods=['POST'])
def verify_code():
    entered_code = request.form.get('code')
    if entered_code == SECRET_CODE:
        session['authenticated'] = True
        return redirect(url_for('home'))
    else:
        return render_template('login.html', error=True)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)