import time
import asyncio
from service.operations import MathOperations

class RequestProcessor:
  """
  This class provides methods to process the request in sync and async way.
  """
  def __init__(self,a,b, action):
      self.action = action
      self.a = a
      self.b = b
      self.ops = MathOperations()
      self.result = {}

  def process_request(self):
    """
    Choose the method of computing between synchronous and asynchronous.
    If the action is sync then the synchronous call will take place.
    """
    if self.action == 'sync':
      return self.__compute_sync()
    else:
      return self.__compute_async()
  def __compute_sync(self):
    """
    Executing the add() and multiply() methods in a sync way.
    """
    start = time.perf_counter()
    self.result["addition"] = self.ops.add(self.a,self.b)
    self.result["multiply"] = self.ops.multiply(self.a,self.b)
    end = time.perf_counter()
    self.result["elapsed_time"] = end - start

    return self.result

  async def __compute_async(self):
    """
    Executing the add() and multiply() methods in an async way.
    """
    start = time.perf_counter()
    self.result["addition"], self.result["multiply"] = await asyncio.gather(
      self.ops.async_add(self.a,self.b),self.ops.async_multiply(self.a,self.b)
    )
    end = time.perf_counter()
    self.result["elapsed_time"] = end - start

    return self.result