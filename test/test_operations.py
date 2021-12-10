from service.operations import MathOperations

def test_sync_operations():
    ops = MathOperations()
    assert ops.add(1,2) == 3
    assert ops.multiply(3,3) == 9

def test_async_operations(event_loop):
    ops = MathOperations()
    addition = event_loop.run_until_complete(ops.async_add(5,5))
    multiply = event_loop.run_until_complete(ops.async_multiply(5,5))
    assert addition == 10
    assert multiply == 25