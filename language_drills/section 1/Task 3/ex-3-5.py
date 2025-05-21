from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/mixed")
def mixed():
    # Get the list of positional arguments (args)
    args = request.args.getlist("arg")

    # Get the keyword arguments (kwargs), excluding the "arg" key
    kwargs = {k: v for k, v in request.args.items() if k != "arg"}

    # Add a "name" field to kwargs if it's passed as a query parameter
    name = request.args.get("name", "Guest")  # Default to "Guest" if name is not provided

    # Combine the args and kwargs into a final response, including name
    return jsonify({"name": name, "args": args, "kwargs": kwargs})


# Entry point to run the app
if __name__ == "__main__":
    app.run(debug=True)
