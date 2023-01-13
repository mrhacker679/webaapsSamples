from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        # Get the values and operation from the form
        value1 = float(request.form["value1"])
        value2 = float(request.form["value2"])
        operation = request.form["operation"]
        
        # Perform the calculation
        if operation == "add":
            result = value1 + value2
        elif operation == "subtract":
            result = value1 - value2
        elif operation == "multiply":
            result = value1 * value2
        elif operation == "divide":
            result = value1 / value2
        
        # Return the result
        return str(result)
        
    return render_template("calculator.html")

if __name__ == "__main__":
    app.run()
