import unittest
from .database import TestDatabase
from .redis import TestRedis
from .rabbitmq import TestRabbitmq

if __name__ == '__main__':
    unittest.main()
