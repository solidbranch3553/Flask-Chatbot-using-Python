from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    q = request.get_json().get("userInput")
    
    if "hi" in q:
        user = "Hello, How are you"
    elif "what is your name" in q:
        user = "My name is Venom Zpotica"
    else:
        pass
    return str(user)

if __name__ == '__main__':
    app.run(debug=True)