import asyncio

from views.request_processor import RequestProcessor as rp
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sync', methods=['GET'])
def sync_index():
    """
    This handler will return the result in a synchronous way. The time to
    compute the result should equal the sum of the slepping seconds of the
    add() and multiply() functions. Each operation waits for the previous one to
    finish and then starts execution.
    """
    return jsonify({"output": rp(4,5,'sync').process_request()})

@app.route('/async', methods=['GET'])
async def async_index():
    """
    This handler will return the result in a asynchronous way. The time to
    compute the result should approxiametely equal the time it takes to execute
    the most expensive function that exists in this call.
    Boths async_add() and async_multiply() functions need 3seconds to finish so
    the total time should be equal to 3 seconds as the execution of the methods
    is done in an asynchronous way.
    """
    return jsonify(
      {"output": (await asyncio.gather(rp(4,5,'async').process_request()))[0]})

if __name__ == "__main__":
    app.run(debug=False)