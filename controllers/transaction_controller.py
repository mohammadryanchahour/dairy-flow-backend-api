from flask import Blueprint, json
from helpers.custom_responses import error_response, success_response
from services.transaction_services import get_all_transactions, get_transaction_by_id


transaction_routes = Blueprint('transaction_routes', __name__)

@transaction_routes.route('/get-all-transactions', methods=['GET'])
def get_transactions():
    try:
        transactions, error = get_all_transactions()

        if error:
            return error
        
        transactions = json.loads(transactions.to_json())

        return success_response(transactions, "All Transactions Retrieved Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
    
@transaction_routes.route('/get-transaction/<string:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    try:
        transaction, error = get_transaction_by_id(transaction_id)

        if error:
            return error
        
        transaction = json.loads(transaction.to_json())

        return success_response(transaction, "Transaction Retrieved Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
        
@transaction_routes.route('/delete-transaction/<string:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    try:
        transaction, error = get_transaction_by_id(transaction_id)

        if error:
            return error

        transaction.delete()

        return success_response("Transaction Deleted Successfully", 200)
    
    except Exception as e:
        return error_response(f"Internal Server Error => {str(e)}", 500)
