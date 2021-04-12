from flask import Blueprint, jsonify, request

customer_views = Blueprint('customer_views', __name__, template_folder='../templates')

from App.controllers import (
    get_customers,
    delete_customer_by_id,
)

# get list of all customers and return it to frontend
@customer_views.route('/customers', methods=["GET"])
def display_customers():
    customerList = get_customers()
    return jsonify(customerList)

#Deletes customer from database and returns if it was successful
@customer_views.route('/delete-customer', methods=["DELETE"])
def delete_customer():
    customer_id = request.args.get("id")
    deleted = delete_customer_by_id(customer_id)
    return jsonify({"deleted" : deleted})