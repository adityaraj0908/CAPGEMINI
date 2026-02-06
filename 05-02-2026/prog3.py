from flask import Flask,request,jsonify
from datetime import datetime

app = Flask(__name__)


customers = {}
accounts = {}
transactions = []

@app.route("/customers",methods = ["GET"])
def get_customers():
    return jsonify(list(customers.values()))


@app.route("/customers", methods=["POST"])
def create_customer():

    data = request.get_json()

    required = ["name", "email", "phone"]

    for field in required:
        if field not in data:
            return jsonify({"message": f"{field} is required"}), 400

    cid = len(customers) + 1
    data["id"] = cid
    customers[cid] = data

    return jsonify(data), 201



@app.route("/accounts", methods=["POST"])
def create_account():

    data = request.get_json()

    if data["customer_id"] not in customers:
        return jsonify({"message": "Customer not found"}), 404

    acc_no = len(accounts) + 1001

    account = {
        "acc_no": acc_no,
        "customer_id": data["customer_id"],
        "account_type": data["account_type"],
        "balance": 0
    }

    accounts[acc_no] = account

    return jsonify(account), 201


@app.route("/transactions", methods=["POST"])
def transaction():

    data = request.get_json()

    acc_no = data["acc_no"]

    if acc_no not in accounts:
        return jsonify({"message": "Account not found"}), 404

    amount = data["amount"]
    ttype = data["type"]

    if ttype == "Deposit":
        accounts[acc_no]["balance"] += amount

    elif ttype == "Withdraw":

        if accounts[acc_no]["balance"] < amount:
            return jsonify({"message": "Insufficient balance"}), 400

        accounts[acc_no]["balance"] -= amount

    else:
        return jsonify({"message": "Invalid transaction type"}), 400

    transaction = {
        "id": len(transactions) + 1,
        "acc_no": acc_no,
        "type": ttype,
        "amount": amount,
        "date": str(datetime.now())
    }

    transactions.append(transaction)

    return jsonify(transaction), 201




@app.route("/transactions/<int:acc_no>", methods=["GET"])
def get_transactions(acc_no):

    history = [t for t in transactions if t["acc_no"] == acc_no]

    return jsonify(history)




if __name__ == "__main__":
    app.run()