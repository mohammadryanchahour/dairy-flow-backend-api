from flask import jsonify

def success_response(data=None, message="", status_code=None):
    """
    Generate a custom JSON success response with optional data, error message, and status code.
    
    Parameters:
    - data (any): Data to be included in the response.
    - error (str): Error message, if any.
    - message (str): Additional message, if any.
    - status_code (int): HTTP status code for the response.
    
    Returns:
    - Flask response: JSON response containing data, error, message, and status code.
    """
    response = {
        "error": False,
        "message": message,
        "data": data if data is not None else {}
    }
    return jsonify(response), status_code


def error_response(message="", status_code=None):
    """
    Generate a custom JSON error response with optional data, error message, and status code.
    
    Parameters:
    - error (str): Error message, if any.
    - message (str): Additional message, if any.
    - status_code (int): HTTP status code for the response.
    
    Returns:
    - Flask response: JSON response containing error, message, and status code.
    """
    response = {
        "error": True,
        "message": message
    }
    return jsonify(response), status_code
