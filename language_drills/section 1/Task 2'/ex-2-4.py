from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def set_comprehension():
    """
    Extract unique vowels from a string using set comprehension.
    """
    sentence = "hello world"
    vowels = {char for char in sentence if char in "aeiou"}
    return jsonify({"vowels": list(vowels)})

if __name__ == '__main__':
    app.run(debug=True)
