from views.request_processor import RequestProcessor as rp

def test_request_sync_processor():
    sync_result = rp(4,5, 'sync').process_request()
    assert sync_result["addition"] == 9
    assert sync_result["multiply"] == 20


def test_request_async_processor(event_loop):
    async_result = event_loop.run_until_complete(rp(5,5,'async').process_request())
    assert async_result["addition"] == 10
    assert async_result["multiply"] == 25
