# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples in Python are data structures which contain a sequence of objects, with the main difference being that lists are mutable and tuples are immutable. Consequently, only tuples will work as keys in dictionaries because of the requirement for dictionary keys to be immutable. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and sets are data structures which contain a sequence of elements. Some of the main differences include that sets are unordered, don't contain duplicates, and can only contain hashable items. An example of a might be as follows: 
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  *this is a set*  
print(basket)   *Yields different results for lists and sets*  
{'orange', 'banana', 'pear', 'apple'}  *Output (note unique values only)*  
basket = ('apple', 'orange', 'apple', 'pear', 'orange', 'banana')  *this is a list*  
print(basket)   
('apple', 'orange', 'apple', 'pear', 'orange', 'banana') *list output*  
This also means that lists are better for sorting a list of ordered elements, while sets can be more advantageous when you don't want duplicates or care about order. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda function is a way to create an anonymous function which will only be utilized once and then be forgotten. This makes it particularly useful as a parameter in various other functions including Mao, Reduce, and Sorted. When sorting a list for example, we can use a lambda function as the 'key' argument to specify any operation or transformation we would like to make to the items on the list before comparing them. An example would be as follows:   
mylist = [3,6,3,2,4,8,23]  
sorted(mylist, key=lambda, x%2==0)   
3,3,23,6,2,4,8 ##output   
The example above utilizes lambda to check for even numbers and apply the sorted function once this is complete. 



---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is an operator which is Python's way of implementing well-known notations for sets similar to those used by mathematicians. Most common list operations can be expressed as a combination of map, filter and reduce. These are so common that Python provides language features to support them, including list comprehension and a built in function called map. The first example shows list comprehension using map while the second example uses filter.   
*Using Map*  
t = ['Apple','orange','pear','Carrot','potato','pea']  
def capitalize_all(t):  
    res = []  
    for s in t:  
        res.append(s.capitalize())  
    return res
capitalize_all(t)  
['Apple', 'Orange', 'Pear', 'Carrot', 'Potato', 'Pea'] *output*    
*Using Filter*    
def only_upper(t):  
    caps = []  
    for s in t:  
        if s[0].isupper():  
            caps.append(s)  
    return caps  
only_upper(t)  
['Apple', 'Carrot'] *output*

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





