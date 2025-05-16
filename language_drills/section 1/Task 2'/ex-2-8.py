from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def conditional_assignment_in_comprehension():
    """
    Replace negative numbers with 0 in a list using list comprehension.
    """
    numbers = [-1, 2, -3, 4]
    updated_numbers = [0 if x < 0 else x for x in numbers]
    return jsonify({"updated_numbers": updated_numbers})

if __name__ == '__main__':
    app.run(debug=True)

