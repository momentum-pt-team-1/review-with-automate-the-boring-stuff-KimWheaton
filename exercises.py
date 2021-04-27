# Please answer the practice questions at the end of chapters 1-6 here under the cooresponding comment:

# Chapter 1

# 1.  * - / + are operators, and 'hello', -88.8 and 5 are values

# 2.  spam is a variable and 'spam' is a string

# 3.  Three data types are: string, interger, and float.

# 4.  Expressions are made up of values (2). All expressions can reduce to a single value (4) (2 + 2 = 4).

# 5.  An assignment statement assigns a value to a variable (spam = 10 means that the variable spam has a value of 10). 
#     An expression uses the values in variables to perform an operation.

# 6.  21

# 7.  'spamspamspam'
#     'spamspamspam'

# 8.  A variable name cannot start with a number

# 9.  int()
#     float()
#     str()

# 10. You cannot mix strings and intergers when adding in an expression. 
#     You could write this as 'I have eaten ' + str(99) + ' burritos'
#         or as 'I have eaten ' + '99' + ' burritos'

##########################################

# Chapter 2

# 1.  True False

# 2.  and, or, not

# 3. and truth table:
#         True and True = True
#         True and False = False
#         False and True = False
#         False and False = False

#     or truth table:
#         True or True = True
#         True or False = True
#         False or True = True
#         False or False = False

#     not truth table:
#         not True = False
#         not False = True

# 4.  False
#     False
#     True
#     True

# 5. The six comparison operators are:
#     ==       !=      <       >       <=      >=

# 6.  The equal to operator (==) asks whether two values are the same as each other.
#     The assignment operator (=) puts the value on the right into the variable on the left.

# 7.  Conditions evaluate expressions down to a Boolean value. 
#     Almost every flow control statement uses a condition to decide what to do.

# 8.  spam = 0
#     if spam == 10:
#         print('eggs') <--- block 1
#         if spam > 5:
#             print('bacon')  <--- block 2
#         else:
#             print('ham')    <--- block 3
#         print('spam')
#     print('spam')            

# 9.  if spam == 1:
#         print('Hello')
#     elif spam == 2:
#         print('Howdy')    
#     else print('Greetings!')

# 10. If code is stuck in an infinite loop, press CONTROL-C

# 11. A break statement exits a while loop. 
#     A continue statement tells the program to go back to the start of the loop and re-evaluate the loop's conditions.

# 12. range(10) and range(0,10) both indicate a sequence of integers starting with 0 and up but not including 10
#     range(0,10,1) indicates a step argument - the third value is how much the variable is increased after each iteration (the interval)

# 13. 

# for num in range(1,11):
#     print(num)

# num = 1
# while num <= 10:
#     print(num)
#     num = num + 1

# 14. spam.bacon()

##########################################

# Chapter 3

# 1. Functions allow you to group code that gets executed multiple times, rather than duplicating code over and over again.

# 2. The code in a function executes when the function is called.

# 3. def with a statement followed by (): creates a function.

# 4. A function is the head plus the body. A function call tells the computer to execute the lines in the function.

# 5. There is only one global scope per program (the scope of the global variable is the entire program).
#     Multiple local scopes can exist at the same time. Local scopes are variables that will only work within the function in which they are called.

# 6. Local scope variables are destroyed when the function call returns and the program terminates.

# 7. A return value is the value or expression a function call evaluates to.
#     A return value can be part of an expression because a return value can be part of an argument in another function call.

# 8. If a function doesn't have a return statement, the return value is None.

# 9. Use a global statement to force a variable in a function to refer to a global variable.

# 10. The None data type is the absence of a value. If you use a function return statement with no value (just the return keyword) then 'None' is returned.

# 11. It would theoretically import a module named areallyourpetsreallynamederic.

# 12. spam.bacon()

# 13. Use try and except clauses. 

# 14. The code that might cause an error goes in a try clause. The execution goes in the except clause.

##########################################

# Chapter 4

# 1. [] is an empty list that contains no values.

# 2. spam[2] = 'hello'

# 3. 'd'

# 4. 'd'

# 5. 'a', 'b'

# 6. 1

# 7. bacon = [3.14, 'cat', 11, 'cat', True, 99]

# 8. bacon = [3.14, 11, 'cat', True]

# 9. + for list concatenation and * for list replication

# 10. append() adds a value to the end of a list and insert() adds a value at the indicated index place

# 11. list.remove() and list.pop()

# 12. Lists and strings are both sequence value types. 
#     A string is immutable, but both can use indexes and slices.

# 13. Lists [] are changeable/mutable and tuples () are unchangeable/immutable

# 14. To type a tuple value with just one interger, use a trailing comma at the end, such as (42,)

# 15. The function list(()) will return a list version of a tuple and tuple([]) will return a tuple version of a list.

# 16. Variables contain _references_ to lists.

# 17. copy.copy() makes a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.
#     Use copy.deepcopy() if the list you need to copy contains nested lists that need to be copied as well.

##########################################

# Chapter 5

# 1. {}

# 2. {'foo':42}

# 3. Unlike in a list, a dictionary has key:value pairs that are unordered (there is no "first" item).
#     Because dictionaries are unordered, they can't be sliced like lists.

# 4. You get a KeyError message

# 5. They are the same because 'cat' in spam checks to see if cat is a key the dictionary, while 'cat' in spam.keys() checks to see if 'cat' is a key in the dictionary

# 6. 'cat' in spam checks to see if 'cat' is a KEY the dictionary, while 'cat' in spam.values() checks to see if 'cat' is a value in the dictionary

# 7. spam.setdefault('color', 'black')

# 8. import pprint and then pprint.pprint(someDictionaryValue)

##########################################

# Chapter 6

# 1. Escape characters let you use characters that otherwise you couldn't put into a string. 
#     An escape character is a backslash (\) followed by the character you wan to add to the string.

# 2. \n is a newline (line break) and \t is a tab

# 3. Create a raw string by placing an r before the beginning of the quotation mark.
#     The r will ignore special characters like \ that you might need for web addresses, etc.

# 4. The single quote will stay because the string was marked with beginning and ending double quotes.

# 5. Instead of \n you can use triple quotes.

# 6.  'e'
#     'Hello'
#     'Hello'
#     'lo, world!'

# 7.  'HELLO'
#     False
#     'hello'

# 8. ['Remember', 'remember', 'the', 'fifth', 'of', 'November.']
#     'There-can-be-only-one.'

# 9.  .rjust()    .ljust()    .center() --  where the number in the parentheses gives the total length of the string including characters and spaces.

# 10. Use the strip() method to trim whitespace characters from the beginning or end of a string.

