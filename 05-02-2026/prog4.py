from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Aditya123@localhost/bank_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.config["JWT_SECRET_KEY"] = "mysecret"

db = SQLAlchemy(app)
jwt = JWTManager(app)



class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))


class Account(db.Model):
    acc_no = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    account_type = db.Column(db.String(50))
    balance = db.Column(db.Float, default=0)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acc_no = db.Column(db.Integer)
    type = db.Column(db.String(20))
    amount = db.Column(db.Float)
    date = db.Column(db.String(100))



@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()


    if data["username"] == "admin" and data["password"] == "admin":

        token = create_access_token(identity="admin")

        return jsonify(access_token=token)

    return jsonify({"message": "Invalid credentials"}), 401




@app.route("/customers", methods=["POST"])
@jwt_required()
def create_customer():

    data = request.get_json()

    customer = Customer(
        name=data["name"],
        email=data["email"],
        phone=data["phone"]
    )

    db.session.add(customer)
    db.session.commit()

    return jsonify({"message": "Customer created"}), 201


@app.route("/customers", methods=["GET"])
@jwt_required()
def get_customers():

    customers = Customer.query.all()

    result = []

    for c in customers:
        result.append({
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "phone": c.phone
        })

    return jsonify(result)



@app.route("/accounts", methods=["POST"])
@jwt_required()
def create_account():

    data = request.get_json()

    customer = Customer.query.get(data["customer_id"])

    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    account = Account(
        customer_id=data["customer_id"],
        account_type=data["account_type"]
    )

    db.session.add(account)
    db.session.commit()

    return jsonify({"message": "Account created"}), 201


@app.route("/accounts/<int:acc_no>", methods=["GET"])
@jwt_required()
def get_account(acc_no):

    account = Account.query.get(acc_no)

    if not account:
        return jsonify({"message": "Account not found"}), 404

    return jsonify({
        "acc_no": account.acc_no,
        "customer_id": account.customer_id,
        "balance": account.balance,
        "account_type": account.account_type
    })


@app.route("/transactions", methods=["POST"])
@jwt_required()
def transaction():

    data = request.get_json()

    account = Account.query.get(data["acc_no"])

    if not account:
        return jsonify({"message": "Account not found"}), 404

    amount = data["amount"]
    ttype = data["type"]

    if ttype == "Deposit":
        account.balance += amount

    elif ttype == "Withdraw":

        if account.balance < amount:
            return jsonify({"message": "Insufficient balance"}), 400

        account.balance -= amount

    else:
        return jsonify({"message": "Invalid transaction type"}), 400

    trans = Transaction(
        acc_no=account.acc_no,
        type=ttype,
        amount=amount,
        date=str(datetime.now())
    )

    db.session.add(trans)
    db.session.commit()

    return jsonify({"message": "Transaction successful"})


@app.route("/transactions/<int:acc_no>")
@jwt_required()
def history(acc_no):

    trans = Transaction.query.filter_by(acc_no=acc_no).all()

    result = []

    for t in trans:
        result.append({
            "type": t.type,
            "amount": t.amount,
            "date": t.date
        })

    return jsonify(result)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
