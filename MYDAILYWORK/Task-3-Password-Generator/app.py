from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    error = None
    
    if request.method == 'POST':
        try:
            length = int(request.form.get('length', 12))
            
            if length < 1:
                error = "Password length must be at least 1."
            elif length > 100:
                error = "Password length cannot exceed 100."
            else:
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for _ in range(length))
        except ValueError:
            error = "Please enter a valid number for password length."
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template('index.html', password=password, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5003)

