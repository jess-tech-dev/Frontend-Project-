from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

stripe.api_key = "your_stripe_secret_key"

@app.route("/pay", methods=["POST"])
def pay():
    try:
        data = request.json
        charge = stripe.Charge.create(
            amount=int(data["amount"] * 100),  # Convert to cents
            currency="usd",
            source=data["token"],  # Token from frontend
            description="E-commerce Payment"
        )
        return jsonify({"status": "Payment Successful"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)