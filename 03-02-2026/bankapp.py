from flask import Flask, request, jsonify
app = Flask(__name__)



accounts = {
    101: {
        "name": "Rahul",
        "balance": 40000,
        "salary": 35000,
        "aadhar": "123456789012",
        "pan": "ABCDE1234F",
        "phone": "9876543210",
        "account_type": "Savings"
    },
    102: {
        "name": "Anita",
        "balance": 20000,
        "salary": 25000,
        "aadhar": "234567890123",
        "pan": "PQRSX5678Y",
        "phone": "9876501234",
        "account_type": "Current"
    },
    103: {
        "name": "Suresh",
        "balance": 80000,
        "salary": 60000,
        "aadhar": "345678901234",
        "pan": "LMNOP6789Q",
        "phone": "9123456780",
        "account_type": "FD"
    },
    104: {
        "name": "Meena",
        "balance": 15000,
        "salary": 20000,
        "aadhar": "456789012345",
        "pan": "ZXCVB1234L",
        "phone": "9001234567",
        "account_type": "Savings"
    },
    105: {
        "name": "Kiran",
        "balance": 55000,
        "salary": 45000,
        "aadhar": "567890123456",
        "pan": "QWERT9876A",
        "phone": "9988776655",
        "account_type": "Current"
    }
}








# {
#   "acc_no": 106,
#   "name": "Amit",
#   "balance": 30000,
#   "salary": 32000,
#   "aadhar": "999888777666",
#   "pan": "ASDFG1234Z",
#   "phone": "9999999999",
#   "account_type": "Savings"
# }

















@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] == "admin" and data["password"] == "admin":
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401






@app.route("/account/<int:acc_no>", methods=["GET"])
def get_account(acc_no):
    if acc_no in accounts:
        return jsonify(accounts[acc_no])
    return jsonify({"error": "Account not found"}), 404





@app.route("/account", methods=["POST"])
def create_account():
    data = request.json
    acc_no = data["acc_no"]

    if acc_no in accounts:
        return jsonify({"error": "Account already exists"}), 400

    accounts[acc_no] = data
    return jsonify({"message": "Account created"}), 201




@app.route("/account/<int:acc_no>/update", methods=["PUT"])
def update_balance(acc_no):
    if acc_no not in accounts:
        return jsonify({"error": "Account not found"}), 404

    amount = request.json["amount"]
    accounts[acc_no]["balance"] += amount

    return jsonify({
        "message": "Balance updated",
        "balance": accounts[acc_no]["balance"]
    })




@app.route("/account/<int:acc_no>", methods=["DELETE"])
def delete_account(acc_no):
    if acc_no in accounts:
        del accounts[acc_no]
        return jsonify({"message": "Account deleted"})
    return jsonify({"error": "Account not found"}), 404




@app.route("/loan/<int:acc_no>", methods=["GET"])
def loan_eligibility(acc_no):
    if acc_no not in accounts:
        return jsonify({"error": "Account not found"}), 404

    salary = accounts[acc_no]["salary"]

    if salary > 30000:
        return jsonify({
            "eligible": True,
            "loan_amount": 50000
        })

    return jsonify({
        "eligible": False,
        "loan_amount": 0
    })



if __name__ == "__main__":
    app.run(debug=True)