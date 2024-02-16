from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial/<int:n>", methods=["GET"])
def factorial(n):
	r = calculate(n)
	return {"result": r}, 200

def calculate(n):
	if n <= 1: #Both 0 and 1 have the same factorial result so this is recursive base
		return 1
	else:
		return n * calculate(n-1) #Recursive step

if __name__ == "__main__":
	app.run(host="localhost", port=6023)
