# import unittest
# import json
#
# from utils.broker.message import (
#     BaseMessage,
#     FriendAddedMessage,
#     DevAccessMessage,
#     OwnerAccessMessage,
#     ClientActivationMessage,
#     DevActivationMessage,
# )
# from utils.broker.rabbitmq import RabbitMQ
#
#
# class TestBaseMessage(unittest.TestCase):
#     def test_create_base_message(self):
#         message = {"Hello": "world!"}
#         exchange_name = 'test_exchange'
#         routing_key = 'test_queue'
#         base_message = BaseMessage(
#             exchange_name=exchange_name, routing_key=routing_key, message=message
#         )
#         self.assertEqual(base_message.exchange_name, exchange_name)
#         self.assertEqual(base_message.routing_key, routing_key)
#         self.assertEqual(base_message.message, message)
#
#
# class TestRabbitMQ(unittest.TestCase):
#     def setUp(self) -> None:
#         self.rabbitmq = RabbitMQ()
#
#     def test_send_and_receive_message(self):
#
#         self.rabbitmq.__enter__()
#         self.rabbitmq._channel.queue_declare(queue='test_queue')
#         message = BaseMessage(
#             exchange_name='', routing_key='test_queue', message={'test': 'test message'}
#         )
#
#         self.rabbitmq.send_message(message)
#         method, properties, body = self.rabbitmq._channel.basic_get(
#             queue='test_queue', auto_ack=True
#         )
#
#         self.assertIsNotNone(body)
#         message_dict = json.loads(body)
#         self.assertIsInstance(message_dict, dict)
#         self.assertEqual(message_dict['test'], 'test message')
#
#     def test_send_and_receive_dev_activation_message(self):
#         with self.rabbitmq:
#             dev_activation_message = DevActivationMessage(
#                 exchange_name='',
#                 routing_key='test_queue',
#                 message={'user_id': '123', 'is_active': True},
#             )
#             self.rabbitmq.send_message(dev_activation_message)
#             method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
#                 queue='test_queue', auto_ack=True
#             )
#             received_message = json.loads(body)
#             self.assertEqual(received_message, dev_activation_message.message)
#
#     def test_send_and_receive_client_activation_message(self):
#         with self.rabbitmq:
#             client_activation_message = ClientActivationMessage(
#                 exchange_name='',
#                 routing_key='test_queue',
#                 message={'user_id': '456', 'is_active': True},
#             )
#             self.rabbitmq.send_message(client_activation_message)
#             method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
#                 queue='test_queue', auto_ack=True
#             )
#             received_message = json.loads(body)
#             self.assertEqual(received_message, client_activation_message.message)
#
#     def test_send_and_receive_owner_access_message(self):
#         with self.rabbitmq:
#             owner_access_message = OwnerAccessMessage(
#                 exchange_name='',
#                 routing_key='test_queue',
#                 message={'user_id': '789', 'access_level': 'admin'},
#             )
#             self.rabbitmq.send_message(owner_access_message)
#             method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
#                 queue='test_queue', auto_ack=True
#             )
#             received_message = json.loads(body)
#             self.assertEqual(received_message, owner_access_message.message)
#
#     def test_send_and_receive_dev_access_message(self):
#         with self.rabbitmq:
#             dev_access_message = DevAccessMessage(
#                 exchange_name='',
#                 routing_key='test_queue',
#                 message={'user_id': '123', 'access_level': 'developer'},
#             )
#             self.rabbitmq.send_message(dev_access_message)
#             method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
#                 queue='test_queue', auto_ack=True
#             )
#             received_message = json.loads(body)
#             self.assertEqual(received_message, dev_access_message.message)
#
#     def test_send_and_receive_friend_added_message(self):
#         with self.rabbitmq:
#             friend_added_message = FriendAddedMessage(
#                 exchange_name='',
#                 routing_key='test_queue',
#                 message={'user_id': '123', 'friend_id': '456'},
#             )
#             self.rabbitmq.send_message(friend_added_message)
#             method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
#                 queue='test_queue', auto_ack=True
#             )
#             received_message = json.loads(body)
#             self.assertEqual(received_message, friend_added_message.message)
#
#     def test_send_message_with_invalid_format(self):
#         with self.assertRaises(TypeError):
#             invalid_message = "invalid message"
#             message = BaseMessage(
#                 exchange_name='', routing_key='test_queue', message=invalid_message
#             )
#             self.rabbitmq.send_message(message)
#
#     def test_send_message_to_nonexistent_queue(self):
#         with self.assertRaises(Exception):
#             message = BaseMessage(
#                 exchange_name='', routing_key='nonexistent_queue', message={'test': 'test message'}
#             )
#             self.rabbitmq.send_message(message)
#
#     def test_send_message_with_invalid_routing_key(self):
#         with self.assertRaises(Exception):
#             message = BaseMessage(
#                 exchange_name='', routing_key=123, message={'test': 'test message'}
#             )
#             self.rabbitmq.send_message(message)
#
#     def test_send_and_receive_multiple_messages_in_order(self):
#         with self.rabbitmq:
#             queue_name = 'test_queue'
#             self.rabbitmq._channel.queue_declare(queue=queue_name)
#             messages = [
#                 BaseMessage(
#                     exchange_name='', routing_key=queue_name, message={'test': 'test message 1'}
#                 ),
#                 BaseMessage(
#                     exchange_name='', routing_key=queue_name, message={'test': 'test message 2'}
#                 ),
#                 BaseMessage(
#                     exchange_name='', routing_key=queue_name, message={'test': 'test message 3'}
#                 ),
#             ]
#             for message in messages:
#                 self.rabbitmq.send_message(message)
#
#             received_messages = []
#             for i in range(len(messages)):
#                 method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
#                     queue=queue_name, auto_ack=True
#                 )
#                 if body is not None:
#                     received_messages.append(json.loads(body))
#
#             self.assertListEqual(received_messages, [m.message for m in messages])
#
#     def test_receive_message_from_empty_queue(self):
#         with self.rabbitmq:
#             queue_name = 'empty_queue'
#             self.rabbitmq._channel.queue_declare(queue=queue_name)
#             method_frame, header_frame, body = self.rabbitmq._channel.basic_get(
#                 queue=queue_name, auto_ack=True
#             )
#             self.assertIsNone(body)
#
#     def test_send_message_with_invalid_exchange(self):
#         with self.assertRaises(Exception):
#             message = BaseMessage(
#                 exchange_name=123, routing_key='test_queue', message={'test': 'test message'}
#             )
#             self.rabbitmq.send_message(message)
