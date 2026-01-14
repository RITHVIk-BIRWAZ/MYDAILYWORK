from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1', 0))
            num2 = float(request.form.get('num2', 0))
            operation = request.form.get('operation', '+')
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error = "Error: Division by zero is not allowed."
            else:
                error = "Invalid operation choice."
        except ValueError:
            error = "Please enter valid numbers."
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

