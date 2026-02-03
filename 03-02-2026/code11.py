from flask import Flask,render_template,request,redirect, url_for,flash,jsonify
app = Flask(__name__)


staff_data = {
101: {"name": "Dr. Ravi", "subject": "DAA"},
102: {"name": "Dr. Meena", "subject": "DBMS"},
103: {"name": "Dr. Arun", "subject": "OS"}
}

@app.route("/staff", methods=['GET'])
def get_all_staff():
    try:
        return jsonify(staff_data) 
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        print("get all staff called")
        




if __name__=="__main__":
    app.run(debug=True)