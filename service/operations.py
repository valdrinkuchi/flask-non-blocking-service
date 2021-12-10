import asyncio
import time

class MathOperations:
  async def async_add(self,a,b):
    """
    Add two numbers in an async method and return the result after sleeping
    for 3 seconds.
    """
    await asyncio.sleep(3)
    return a + b

  async def async_multiply(self,a,b):
    """
    Multiply two numbers in an async method and return the result after sleeping
    for 3 seconds.
    """
    await asyncio.sleep(3)
    return a * b

  def add(self,a,b):
    """Add two numbers and return the result after sleeping for 3 seconds."""
    time.sleep(3)
    return a + b

  def multiply(self,a,b):
    """Multiply two numbers and return the result after sleeping for 3 seconds"""
    time.sleep(3)
    return a * b