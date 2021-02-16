import unittest

# This is a sandbox to experiment with CoderPad's execution capabilities.
# It's a temporary, throw-away session only visible to you.

def say_hello():

    print('**********************************************************************')

    msg = 'Hello, World'
    print(msg)
    return msg

# for i in xrange(5):
#     say_hello()



class TestStringMethods(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(say_hello(), 'Hello, World')


unittest.main(exit=False)
