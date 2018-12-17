# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    '''Test addition operator for postfix_eval'''
    def test_postfix_eval_add(self):
        self.assertEqual(postfix_eval("3 5 +"), 8)
        self.assertNotEqual(postfix_eval("4 10 +"), 15)
    
    '''Test subtraction operator for postfix_eval'''
    def test_postfix_eval_subtract(self):
        self.assertEqual(postfix_eval("5 3 -"), 2)
        self.assertNotEqual(postfix_eval("209 1 -"), 207)
        
    '''Test multiplication operator for postfix_eval'''
    def test_postfix_eval_multiply(self):
        self.assertEqual(postfix_eval("20 30 *"), 600)
        self.assertNotEqual(postfix_eval("13 13 *"), 168)
        
    '''Test division operator for postfix_eval'''
    def test_postfix_eval_divide(self):
        self.assertEqual(postfix_eval("15 3 /"), 5)
        self.assertNotEqual(postfix_eval("200 10 /"), 21)
        
    '''Test exponentiation operator for postfix_eval'''
    def test_postfix_eval_pow(self):
        self.assertEqual(postfix_eval("3 2 **"), 9)
        self.assertNotEqual(postfix_eval("4 2 **"), 15)
        
    '''Test bitshift right operator for postfix_eval'''
    def test_postfix_eval_bit_right(self):
        self.assertEqual(postfix_eval("5 1 >>"), 2)
        self.assertNotEqual(postfix_eval("6 2 >>"), 2)
        
    '''Test bitshift left operator for postfix_eval'''
    def test_postfix_eval_bit_left(self):
        self.assertEqual(postfix_eval("21 2 <<"), 84)
        self.assertNotEqual(postfix_eval("14 5 <<"), 447)

    '''Test float operands on all valid operations for postfix_eval'''
    def test_postfix_eval_float(self):
        self.assertAlmostEqual(postfix_eval("22.5 30.1 +"), 52.6)
        self.assertAlmostEqual(postfix_eval("30.45 20.42 -"), 10.03)
        self.assertAlmostEqual(postfix_eval("5.2 2.1 *"), 10.92)
        self.assertAlmostEqual(postfix_eval("4.8 2.0 /"), 2.4)
        self.assertAlmostEqual(postfix_eval("2.3 3 **"), 12.167)

    '''Tests multiple operations on postfix_eval'''
    def test_postfix_eval_multiple_operations(self):
        self.assertEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)
        self.assertEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)
        self.assertEqual(postfix_eval("4 2 * 7 + 2 >>"), 3)
        self.assertEqual(postfix_eval("25 2 << 10 / 7 12 31 5 - + - +"), -21)
        self.assertAlmostEqual(postfix_eval(infix_to_postfix("2 * 45 + ( 2 + 3 * 4 ) / 6")), 92.3333333)

    '''Tests division by 0 exception for postfix_eval'''
    def test_postfix_eval_div_0(self):
        try:
            postfix_eval("4 0 /")
        except ValueError as e:
            self.assertEqual(str(e), "Invalid divisor 0")

    '''Tests illegal bitshift operation exception for postfix_eval'''
    def test_postfix_eval_bitshift_exception(self):
        try:
            postfix_eval("4.2 2 >>")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

        try:
            postfix_eval("7.8 2.1 <<")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    '''Tests insufficient operands exception for postfix_eval'''
    def test_postfix_eval_insufficient_operands(self):
        try:
            postfix_eval("4 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
            
    '''Tests too many operands exception for postfix_eval'''
    def test_postfix_eval_too_many_operands(self):
        try:
            postfix_eval("1 2 3 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    '''Tests invalid token exception for postfix_eval'''
    def test_postfix_eval_invalid_token(self):
        try:
            postfix_eval("blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
    
    '''Tests postfix_eval using the infix to postfix converter'''    
    def test_postfix_eval_using_infix_to_postfix(self):
        self.assertEqual(postfix_eval(infix_to_postfix("1 + ( 3 * 7 ) - 2")), 20)
    
    '''Tests postfix_eval using the prefix to postfix converter'''
    def test_postfix_eval_using_prefix_to_postfix(self):
        self.assertEqual(postfix_eval(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6")), -5.2)
    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("( 6 * 3 ) / 2"), "6 3 * 2 /")
        self.assertEqual(infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"), "5 6 3 + 7 3 * - 2 + * 6 /")
        self.assertEqual(infix_to_postfix("8 + 3 * 4 + ( 6 - 2 + 2 * ( 6 / 3 - 1 ) - 3 )"), "8 3 4 * + 6 2 - 2 6 3 / 1 - * + 3 - +")
        self.assertEqual(infix_to_postfix("8.7 + 3 - ( 4.2 + 2.1 )"), "8.7 3 + 4.2 2.1 + -")
        self.assertEqual(infix_to_postfix("1 + 7 * ( 3 - 4 ) / 6"), "1 7 3 4 - * 6 / +")
        
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* 4.2 2.1"), "4.2 2.1 *")
        self.assertNotEqual(prefix_to_postfix("/ + * 3 2 8 7"), "7 8 2 3 + * /")
        self.assertEqual(prefix_to_postfix("** * 4 2 2"), "4 2 * 2 **")
        self.assertNotEqual(prefix_to_postfix("** * 4 2 2"), "2 4 2 * **")
        self.assertEqual(prefix_to_postfix("/ * + 4 2 21 2"), "4 2 + 21 * 2 /")
        self.assertEqual(prefix_to_postfix("- ** 4 2 / 12 + + 4 2 7"), "4 2 ** 12 4 2 + 7 + / -")

    '''Tests the index error exception for the Stack class to ensure 100% code coverage'''
    def test_stack_array(self):
        s = Stack(2)
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.peek()
        s.push(2)
        s.push(8)
        with self.assertRaises(IndexError):
            s.push(7)
        

if __name__ == "__main__":
    unittest.main()
