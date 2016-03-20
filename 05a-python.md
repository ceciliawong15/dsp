# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are both data structures. The values in a list can change by appending or removing (mutable). Once you have defined a tuple, you cannot change the values (immutable). The fact that tuples are immutable is the reason why they will work as keys in dictionaries. They can work as keys because they can be hashed without worry that the key value will change. Lists work for looping while tuples work for structuring. Tuples can also be unpacked while lists cannot.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists can contain repeating values while sets can not. If you want to find the position of x in a list and there are two instances, the list will only return the first instance. With a set you can be assured that you are returning the only position of x. 
\\\Example of a list: [1, 1, 2, 3, 3, 4]
\\\Example of a set: [1, 2, 3, 4]

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda's are used to be passed as anonymous functions. This allows you to call a second function within a function while removing the need to define the second function in another line of code. Lambdas can only be used if your second function only has one expression.\\\colors = ['blue', 'purple', 'red', 'pink', 'lavendar']\\\sorted(colors, key=lambda x: len(x))\\\returns ['red', 'blue', 'pink', 'purple', 'lavendar']

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are awesome! If you want to transform or filter a list, list comprehensions allow you to do it within one line of code, instead of using a for-loop. For example, if you have a list\\\ mylist = [1, 2, 3, 4, 5, 6, 7, 8] and you want to get a new list with all the items in the original but multiplied by two, you could use a for loop such as:\\\
modlist = []
for i in mylist:
    j = i * 2
    modlist.append(j)\\\In order to accomplish this using the map function: modlist = map(lambda x: x*2, mylist)\\\in order to filter out values greater than 5,\\\modlist = filter(lambda x: x<5, modlist)\\\In order to accomplish all of the above using a list comprehension, you could do, modlist = [i*2 for i in mylist if i*2 <5]\\\Set Comprehension: set= {x*2 for x in range(10)}\\\Dictionary Comprehension: dict = {'a': 10000, 'b': 20000, 'c': 30000, 'd': 40000}\\\underpaid_ids = [id for (id, salary) in mydict.items() if salary < 25000]\\\Or, underpaid_ids = [i[0] for i in mydict.items() if i[1] < 25000]\\\


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





