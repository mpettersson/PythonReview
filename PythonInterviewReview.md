
Python Interview Review
=======================

[//]: # (This file is layedout this way so that it can be printed, then folded in half and studied)

This file is meant as a very quick study guide for the polyglot programmer who needs to make sure that
they don't forget something foolish in an interview.  



Numbers & Math
--------------
-[ ] Max/Min size      
                                        import sys  
                                        sys.maxsize  
                                        -sys.maxsize - 1  
-[ ] Infinity/NAN  
                                        import math  
                                        math.inf  
                                        math.nan  # math.inf - math.inf is nan   
-[ ] Max/Min/Power  
                                        num_list = [0, 121, -42, 69, 3, 22]  
                                        max(num_list)  
                                        min(num_list)  
                                        2**10   
-[ ] Sqrt/Log/Floor/Ceiling/Abs  
                                        import math  
                                        num = -4.2  
                                        base = 2  
                                        math.sqrt(num)  
                                        math.log(num, base)  
                                        math.floor(num)                                         
                                        math.ceil(num)  
                                        abs(num)  
-[ ] Random  
                                        import random  
                                        random.seed(10)                         # How to seed random.  
                                        random.random()                         # Random float:  0.0 <= x < 1.0  
                                        random.uniform(2.5, 10.0)               # Random float:  2.5 <= x < 10.0  
                                        random.randrange(10)                    # Random Integer:  0 to 9 inclusive  
                                        random.randrange(0, 101, 2)             # Random (Even) Integer from 0 to 100 inclusive  
                                        random.choice(['win', 'lose', 'draw'])  # Single random element from a sequence  
                                        l = [0, 1, 2, 3, 4]  
                                        random.shuffle(l)                       # (In place) shuffled the list l.  
-[ ] Decimal/Binary/Hex/Octal  
                                        -42  
                                        -0b1000101  
                                        -0x45  
                                        -0o105  
-[ ] int --> 
     Decimal/Binary/Hex/Octal String  
                                        str(-42)  
                                        bin(-42)  
                                        hex(-42)  
                                        oct(-42)  
-[ ] Decimal/Binary/Hex/Octal String 
     --> int  
                                        int('-42')
                                        int('-0b1000101', 2)
                                        int('-0x45', 16)
                                        int('-0o105', 8)  

Formatting & I/O
----------------
-[ ] User Input  
                                        var = input("Enter input text:")  
-[ ] Formatting  
                                        print(4, 1, 1982, sep='/')
                                        print("Print w/o trailing newline.", end='')
                                        print("\n%04d %s %.2f %c" % (1, "Matt", 3.14, 'A'))
                                        x = 2
                                        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
                                        print(f"{x} + {x} = {x + x}")  # Added in python 3.6
-[ ] Get Directory/script file  
                                        import os
                                        os.getcwd()                     # Current working directory. 
                                        __file__                        # File name of the executing script. 
                                        os.path.realpath(__file__)      # Full path (following symlinks) of exe script.
                                        os.path.dirname(__file__)       # Directory only of executing script.   
-[ ] Create file (if d.n.e.)  
                                        import os
                                        if not os.path.exists('my_file.txt'):
                                            with open('my_file.txt', 'w'): 
                                                pass
-[ ] Open/Read/Write File  
                                        # The modes are:
                                        #   r  - Open for reading plain text
                                        #   w  - Open for writing plain text
                                        #   a  - Open an existing file for appending plain text
                                        #   rb - Open for reading binary data
                                        #   wb - Open for writing binary data
                                        with open("my_file.txt", mode="w", encoding="utf-8") as f:
                                            f.write("Some Random\nText, blah, blah, blah,\nLet's get schwifty baby!")
                                        with open("mydata.txt", encoding="utf-8") as f:
                                            print(f.read())     # f.readline() would just read one line.
                                        print(my_file.closed)   # Check if file is closed
-[ ] Delete File  
                                        try:
                                            if not os.path.exists('my_file.txt'):
                                                os.remove("my_file.txt")
                                        except OSError as e:  # if failed, report it back to the user ##
                                            print("Error: %s - %s." % (e.filename, e.strerror))

String Manipulation
-------------------                          
-[ ] Strip  
                                        s = "    M a tthew \t  \n Pettersson    \n"  
                                        s.strip()                       # ONLY rm leading/trailing non-visible char.
                                        "".join(s.split())              # Remove all non-visible chars, fast.
                                        import re                       # Via REGEX  
                                        re.sub(r'\s+', '', s)           # Remove all non-visible chars, slower.  
-[ ] Replace  
                                        s = "Ohhhhhhh Myyyyyyyyyyy"  
                                        count = 1  
                                        s.replace("hh", "HH", count)    # Only one set is replaced
                                        count = -1                      # Replace ALL sets, (-1 is default value).  
                                        s.replace("hh", "HH", count)    # Replace ALL sets.
                                        s.replace("yy", "YY")           # Same as using -1 count.  
-[ ] Find  
                                        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ, now I know my ABC's..."  
                                        i = s.find("C")                 # Find FIRST match.
                                        start = 1; end = len(s) - 1  
                                        i = s.find("C", start, end)     # Find FIRST match in range start to end.
                                        i = s.rfind("C", start, end)    # Find RIGHT most match in range start to end.  
-[ ] Substring  
                                        s = "SayMayHeyHayBayWay"  
                                        s[3:6]                          # "May"  
                                        s[3:12:3]                       # "MHH" (every 3rd char from 3 to 12)  
                                        s[5:2:-1]                       # "yaM" (going BACKWARDS, from y(5) to M(2))  
                                        s[::-1]                         # REVERSE String: "yaWyaByaHyeHyaMyaS"
-[ ] Upper/Lower  
                                        s.upper()  
                                        s.lower()  
-[ ] Digit/Alpha  
                                        s.isdecimal()  
                                        s.isalpha()
                                        s.isdigit()
                                        s.isalnum()
-[ ] list --> string (join)  
                                        l = [1, "two", 6, 33, "zero", -12]  
                                        str(l)                          # will produce "[1, 'two', 6, 33, 'zero', -12]"  
                                        ", ".join([str(i) for i in l])  # Join expects str instance.  
                                        "".join(map(str, l))  
-[ ] string --> list (split)  
                                        s = "I'm a str.\n"
                                        l = s.split()                   # ["I'm", 'a', 'str.']
                                        l = s.split('\'')               # ['I', 'm a str.\n']                                 
-[ ] string --> list of 1 len strings  
                                        s = "I'm a str.\n"
                                        l = list(s)                     # ['I', "'", 'm', ' ', 'a', ' ', 's', 't', 'r', '.', '\n']
-[ ] Sort  
                                        s = "aB0 \t"
                                        s_s = sorted(s)                 # CAN use sorted on string (CANT use s.sort())  

List Manipulation
-----------------
-[ ] List Properties  
                                        Are Mutable, Mixed Types, Un-Hashable  
-[ ] List Operations  
                                        l = []  
                                        l = list()  
                                        l = [1, 3.14, "Matt", True]  
                                        l = list([1, 3.14, "Matt", True])  
                                        l.append("new string at end of list")  
                                        l.insert(2, "new string at index 2")  
                                        l[4:4] = ["Adding new string to index 4"]
                                        l.pop(2)                            # Remove item at index (default index = -1).
                                        l.remove("new string at index 2")   # Remove first matched value or raise ValueError.
                                        l.index(True)                       # Return first value index, else raise ValueError. 
                                        l.sort()  
                                        l.reverse()  
                                        l = l[::-1]  
                                        l.extend([False, 99])  
                                        l += [False, 99]  
-[ ] Fill  
                                        l = [None] * 10  
                                        l = [0] * 10 
                                        l = [[None] * 10 for _ in range(10)]
-[ ] Shallow Copy  
                                        l = [1, 2, 3]  
                                        copy = l  
                                        copy = l.copy()  
-[ ] Deep Copy    
                                        l = [1, 2, 3]  
                                        import copy  
                                        deep_copy = copy.deepcopy(l)  
-[ ] Sort  
                                        l = [4, 2, 0]
                                        s_l = sorted(l)                 # Return sorted list.
                                        l.sort()                        # sort() is LIST ONLY, sorts in place, returns None.  
                                        tup_l = [(0, "C", 0.125), (1, "A", 0.25), (2, "B", 0.0)]  
                                        s_t = sorted(tup_l, key=lambda x: x[1]) # Sort and return tup_l by second item.
                                        tup_l.sort(key=lambda x: x[1])          # Sort (IN PLACE) tup_l by second item.
                                        tup_l.sort(key=lambda x: (x[0], x[1]))  # Sort (IN PLACE) by first THEN second item.

Dict. Manipulation
------------------
-[ ] Dict. Properties  
                                        Mutable, NO duplicate keys, Mixed types (keys & values), Un-Hashable,
                                        NO Un-Hashable types (list/dict/set) as keys.  
-[ ] Misc. Operations  
                                        d = dict()                                     
                                        d = {}                                       
                                        d = dict([("old_key", "old_value"), (1, 1)])   
                                        d = {"old_key":"old_value", 1:1}   
                                        len(d)  
                                        d["new_key"] = "new_value"  
                                        d.get("new_key", default="value returned if key not in d")    
                                        d["new_key"]  
                                        del d["new_key"]  
                                        d["old_key"] = "updated_value"  
                                        d.update("old_key") = "another_updated_value" 
                                        d.pop("old_key")  
                                        d.popitem()       
                                        d.keys()  
                                        d.values()  
                                        d.items()  
                                        for k, v in d.items():  
-[ ] Sort  
                                        d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}  
                                        s_v_d = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}  # sort d by VALUE  
                                        s_k_d = {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}  # sort d by KEY  
-[ ] Tuple List <--> Dict  
                                        d_from_t = dict([("key0", "value0"),("key1", "value1")])  
                                        tl_from_d = list(d_from_t.items())  

Set Manipulation
----------------
-[ ] Set Properties   
                                        Unordered List, Unique & Immutable Values (CAN'T Re-Assign Value), Mixed Types,
                                        Un-Hashable, Optional: frozenset.  
                                        Set Operations: - (Diff.), | (Union), & (Intersection), ^ (Symmetric Diff.)   
-[ ] Set Operations  
                                        s = set()  
                                        s = {0.0, 1, "two"}  
                                        s = set([0.0, 1, "two"])  
                                        sc = s.copy()  
                                        fs = frozenset(s)
                                        fs = frozenset({0.0, "one", 2})
                                        fs = frozenset([0.0, "one", 2])
                                        len(s)  
                                        s.add("new_value")  
                                        s.discard("new_value")  
                                        s.difference(fs); s - fs  
                                        s.symmetric_difference(fs); s ^ fs  
                                        s.intersection(fs); s & fs  
                                        s.union(fs); s | fs  
                                        s.isdisjoint(fs)    # Return True if two sets have a null intersection.   
                                        s.issubset(fs)      # Report whether another set contains this set.  
                                        s.issuperset(fs)    # Report whether this set contains another set.  
                                        s.clear()  

Tuple Manipulation
------------------                 
-[ ] Tuple Properties     
                                        Immutable (NO Re-Assignment), Mixed Types & Duplicates Allowed, Hashable  
-[ ] Tuple Operations                                          
                                        t = (0.0, 1, "two")         # Create tuple.
                                        t = tuple([0.0, 1, "two"])  # Tuple from list.
                                        t[0]                        # Get first item in t.
                                        t[-1]                       # Get last item in t.
                                        t[0:-1:2]                   # Get a tuple with every other item in t.
                                        t[::-1]                     # Get a reversed copy of t  
                                        t.count(1)                  # Return number of occurrences of value (1 here).  
                                        t.index("two")              # Return first index of value, ValueError if not found.  
                                        
Data Structures
---------------
-[ ] Stack  
                                        SEE ./Review/DataStructures/Stack.py.  
                                        Variable(s): top.  
                                        Methods: push(element), pop(), is_empty(), search(object).  
                                        Node Variable(s): value, next.  
-[ ] Queue  
                                        SEE ./Review/DataStructures/Queue.py.  
                                        Variable(s): first, last.  
                                        Methods: add(element), remove(), peek(), is_empty().  
                                        Node Variable(s): value, next.                                         
-[ ] LinkedList  
                                        SEE ./Review/DataStructures/SLinkedList.py.  
                                        Variable(s): head.  
                                        Methods: add(element), remove(object), clear(), equals(object), get(index), 
                                        set(index, element), index_of(object).  
                                        Node Variable(s): value, next.  
-[ ] HashMap  
                                        SEE ./Review/DataStructures/HashMap.py.  
                                        Variable(s): array, capacity, size, threshold.  
                                        Methods: add(e), get_index(key), remove(key), get(key), put(key, value), 
                                        size(), is_empty().  
                                        Node Variable(s): key, value, next.  
-[ ] Graph  
                                        SEE ./Review/DataStructures/Graph.py.  
                                        NOTE: It's easier for interviews just to have a list of nodes (no Graph Class).  
                                        Node Variable(s): name, value, neighbors.   
                                        Node Method(s): add_neighbor(n), remove_neighbor(n), get_neighbors().  
-[ ] Tree  
                                        SEE ./Review/DataStructures/BST.py.  
                                        NOTE: During interviews it's easier to just use a list of nodes (no Tree Class).  
                                        Node Variable(s): value, children.  
                                        Node Method(s): add_child(n), remove_child(n), get_children().  

Classes
-------
-[ ] Variables & Methods  
                                        Variables - All instance variables are defined in the init method.  
                                                    Vars defined outside init are CLASS vars; are shared by ALL instances.  
                                        Method - Methods are implicitly passed the obj on which they are invoked (via self).  
                                                 Can have @classmethod (passed the class not obj inst), or @staticmethod 
                                                 (no class or obj instance passed in) decorators.  
-[ ] Single Leading Underscore  
                                        Methods/vars with single leading underscores indicate private use.  
                                        Are a weak "internal use" indicator, does not prevent use of methods/vars.  
-[ ] Double Leading Underscores  
                                        Methods/vars with double leading underscores are used to ensure that subclasses 
                                        don't accidentally override the private methods/vars of their superclasses.   
                                        Not designed to prevent deliberate access from outside.  
-[ ] Importing w.r.t. Underscores  
                                        CAN'T access single/double leading underscores with "from MyModule import *".  
                                        CAN access single/double leading underscores with "import MyModlue".  
-[ ] Dunder/Special/Magic Methods  
                                        __init__ - Class instance initializer (NOT constructor), python runtime provides 
                                                   constructor which calls __init__.  
                                        __del__ - Class finalizer, called before instance is destroyed (not a destructor).  
                                        __new__ - Called (before __init__) to create a new instance of a class, used for 
                                                  custom and immutable types.  
                                        __name__ - Evaluates to __main__ or the actual module name depending on how the 
                                                   enclosing module is being used.  
                                        __repr__ - Unambiguous output for devs; if not defined a default __class__.__name__ 
                                                   instance at id(self) is used.  
                                        __str__  - Intended for readable end user output; if not defined print/str will 
                                                   use the result of __repr__.  
                                        __setitem__ - Called to implement assignment to self[key] (only use if the object 
                                                      supports change to values for key).  
                                        __getitem__ - Called to implement evaluation of self[key].  
                                        __getattr__ - Only invoked if the attribute wasn't found in usual way. Good as a 
                                                      fallback for missing attributes, or to provide lazy initialization.   
                                        __getattribute__ - Same as __getattr__ but is invoked before looking at the 
                                                           attributes; can easily cause infinite recursion.  
                                        __hash__ - Called by built-in hash() function; for members of hashed collections 
                                                   should return an int.  
                                        __iter__ - This method is called when an iterator is required for a container.   
                                                   This method should return a new iterator object that can iterate over 
                                                   all the objects in the container.  
                                        __next__ - For use on iterator objects; return the next item from the container.  
                                        __call__ - Called when the instance is “called” as a function; x(arg1, arg2, ...) 
                                                   is shorthand for x.__call__(arg1, arg2, ...).   
                                        __len__ - Called to implement the built-in function len().  
-[ ] Class Example  
                                        class MyClass(SuperClass, SC2):  
                                            shared_by_all = 42
                                            
                                            # Remember, can't have nondefault after default arg.
                                            def __init__(self, arg_1, arg_2, arg_n="default"):  
                                                SuperClass.__init__(self, arg_1)
                                                SC2.__init__(self)
                                                self.arg_2 = arg_2
                                                self.arg_n = n
                                                
                                            @property  # Getter
                                            def arg_2(self):
                                                return self.__arg_2
                                            
                                            @arg_2.setter
                                            def arg_2(self, value):
                                                self.__arg_2 = value
                                            
                                            @arg_2.deleter
                                            def arg_2(self):
                                                del self.__arg_2
                                                
Common Interview Functions & Algorithms
---------------------------------------
-[ ] isPrime  
-[ ] Fibonacci  
-[ ] Factorial  

-[ ] Russian Peasant Alg (A * B)   
-[ ] Sieve of Eratosthenes (primes 2 to N)  
-[ ] Euclidean or Euclid's Alg (GDD)  
-[ ] Pollard's Rho (Prime Factorization Alg)  
                                        
-[ ] Towers of Hanoi  
-[ ] Floyd Cycle Detection  
-[ ] Quick Select Alg (kth sm/lg num in arr)  
-[ ] Rabin-Karp Alg (Substring Search)  

-[ ] Bubble Sort  
-[ ] Insertion Sort  
-[ ] Selection Sort  
-[ ] Quick Sort  
-[ ] Merge Sort  
-[ ] Topological Sort  

-[ ] Binary Search  
-[ ] In-Order Tree Traversal  
-[ ] Pre-Order Tree Traversal  
-[ ] Post-Order Tree Traversal  
-[ ] Breath First Tree Traversal  
-[ ] Depth First Search  
-[ ] Breadth First Search  

-[ ] Dijkstra's Algorithm  
-[ ] Bellman-Ford Algorithm  
-[ ] Floyd-Warshall algorithm  

Miscellaneous Python 
--------------------
-[ ] pass (keyword)
                                        A no-operation statement.  
-[ ] What is PEP8  
                                        PEP stands for Python Enhancement Proposals.  
                                        PEP8 is the "Style Guide for Python Code"  
-[ ] Docstring  
                                        A Python documentation string is known as docstring, it is a way of documenting 
                                        Python functions, modules and classes.  
-[ ] Namespace  
                                        The place where a variable is stored. 
                                        Namespaces are implemented as dictionaries. 
                                        There are the local, global and built-in namespaces as well as nested namespaces 
                                        in objects (in methods).  
                                        Provide modularity, readability, and maintainability by preventing naming 
                                        conflicts (i.e., builtins.open and os.open()).  
-[ ] Mutable & Immutable Types  
                                        Mutable:  
                                            - List  
                                            - Set  
                                            - Dictionary  
                                        Immutable:  
                                            - String  
                                            - Number  
                                            - Tuple  
-[ ] Pickling & Unpickling  
                                        Pickling is the process where a Python obj is converted into a byte stream.
                                        Unpickling is the inverse of Pickling.
                                        Pickling is alternatively known as serialization, marshalling, or flattening.  
-[ ] How to make Python script exe?  
                                        1.  The script file's mode must be executable.  
                                        2.  The first line must begin with # ( #!/usr/local/bin/python)  
-[ ] Module vs. Package  
                                        Module - An object that serves as an organizational unit of Python code. 
                                                 Modules have a namespace containing arbitrary Python objects. 
                                                 Modules are loaded into Python by the process of importing. 
                                        Package - A Python module which can contain submodules or recursively, subpackages.  
                                                  Technically, a package is a Python module with an __path__ attribute.  
-[ ] @classmethod vs @staticmethod  
                                        Normal Method - The instance (self) is passed as the first arg.  
                                        @classmethod - The class (not instance) is passed as first arg (not self).  
                                            Can be called w/o class instance (or with class instance): cls.classmethod().  
                                        @staticmethod - Neither the class nor instance (self) are passed as first arg.
                                            These act like normal functions, but are grouped in a class.  
-[ ] global vs nonlocal  
                                        global - The global keyword can change or create a global variable from a local 
                                            context/scope. Variables that are only referenced in a function/class scope 
                                            are implicitly global. If a var is assigned a value in a function/class it’s 
                                            assumed to be a local unless explicitly declared as global.  
                                        nonlocal - A nonlocal variable (e.g., nonlocal x) refers to previously bound var 
                                            (i.e., x) in the nearest enclosing scope, excluding globals.  The variable
                                            must be defined in a non-global scope or there will be a SyntaxError (so the 
                                            nonlocal keyword, unlike global, cannot create a nonlocal variable.                                
-[ ] Exceptions  
                                        # RAISE EXCEPTION  
                                        try:   
                                            raise Exception('arg1', 'arg2')  
                                        except Exception as inst:  
                                                print(type(inst))   # the exception instance  
                                                print(inst.args)    # arguments stored in .args  
                                                print(inst)         # __str__ allows args to be printed  
                                                x, y = inst.args    # unpack args  
                                        # CATCH/EXCEPT EXCEPTION  
                                        import sys  
                                        try:  
                                            f = open('myfile.txt')  
                                            s = f.readline()  
                                            i = int(s.strip())  
                                        except OSError as err:  
                                            print("OS error: {0}".format(err))  
                                        except (ValueError, TypeError) as er:  
                                            print("Could not convert data to an integer.")  
                                        except:  
                                            print("Unexpected error:", sys.exc_info()[0])  
                                            raise  # This will raise the exception if the other 2 excepts didn't catch it.  
                                        else:  
                                            print("The else clause (for a try) only get's printed if there was NO EXCEPTION")  
                                            f.close()  
                                        finally:  
                                            print("The finally cause always executes, exceptions or no exceptions!!!") 
                                        # NOTE: There is no Python equivalent to Java's (statically typed) "throws" 
                                        # keyword because Python doesn't have statically typed arguments.                        
-[ ] Lambda  
                                        (lambda x : x * x)(2)  
-[ ] Map  
                                        # Map returns an iterable map object.                                       
                                        list(map(lambda x: x * x, range(0,6)))  
-[ ] Filter  
                                        # Filter returns an iterable filter object.  
                                        list(filter(lambda x: x % 2 == 0, range(1, 11)))  
-[ ] Reduce  
                                        # Returns value NOT iterable. 
                                        import functools  # Need to import functools!   
                                        lambda_max = lambda *l: functools.reduce(lambda a, b: a if a > b else b, iter(l))  
-[ ] Comprehensions   
                                        # List Comprehension (use square brackets):  
                                        cc = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]  
                                        ifc = ["Even" if i % 2 == 0 else "Odd" for i in range(8)]  
                                        # Nested (same as for i in range(7,9): for j in range(1,11): i*j):  
                                        nc = [[i*j for j in range(1, 11)] for i in range(7, 9)]   
                                        # Set Comprehension (use curly braces):  
                                        s = {x for x in int_list if x % 2 == 0}  
                                        # Dict. Comprehension (use curly braces with key : value):  
                                        d = {str(i): i for i in [0, 1, 2, 3, 4]}  
                                        d = {value: key for key, value in d.items()}  # Switch keys with values.  
                                        NOTE: Generator Expression isn't technically a Comprehension.  
-[ ] Iterable  
                                        An object capable of returning its members one at a time.   
                                        Examples of iterables include all sequence types (such as list, str, and tuple) 
                                        and some non-sequence types like dict, file objects, and objects of any classes 
                                        you define with an __iter__() method or with a __getitem__() method that 
                                        implements Sequence semantics.  
                                        NOT every Iterable is an Iterator (i.e., list IS iterable, but ISN'T a iterator).  
                                        # Function to test if an object is iterable.  
                                        def iterable(object):  
                                            try:  
                                                iter(object)  
                                                return True  
                                            except TypeError:  
                                                return False   
-[ ] Iterator  
                                        An object representing a stream of data.   
                                        Repeated calls to the iterator’s __next__() method return successive items in 
                                        the stream. When no more data are available a StopIteration exception is raised 
                                        instead. At this point, the iterator object is exhausted and any further calls 
                                        to its __next__() method just raise StopIteration again.  
                                        Iterators are required to have an __iter__() method that returns the iterator 
                                        object itself so EVERY ITERATOR IS ALSO ITERABLE and may be used in most places 
                                        where other iterables are accepted.  
                                        NOTE: next(object) calls object.__next__() method.   
                                        NOTE: next(object, None) will prevent StopIteration exception (default=None).  
-[ ] Generators  
                                        A function which returns a generator iterator.  Has state, lazily evaluated.    
                                        It looks like a normal function except that it contains yield expressions for 
                                        producing a series of values usable in a for-loop or that can be retrieved one 
                                        at a time with the next() function.  
                                        Every Generator is an Iterator (but not every Iterator is a Genrator).    
                                        def zero_to_n(n):  
                                            i = 0  
                                            while i < n:  
                                                yield i  
                                                i += 1  
                                        NOTE: Can call iter(zero_to_n) even though __iter__() wasn't explicitly defined.  
-[ ] Generator Expression  
                                        An expression, in parentheses, returning an iterator.  
                                        (i for i in range(10) if i % 2 == 0)   
-[ ] Logging  
                                        SEE https://docs.python.org/3/howto/logging-cookbook.html  
                                        import logger  
                                        Has multiple parts:  
                                            1. logger - Allows messages to be passed into the logging chain.  
                                                    logger = logging.getLogger('my_application')  
                                            2. handlers - dictate what happens to messages. 
                                                    file_handler = logging.FileHandler('my.log')  
                                                    file_handler.setLevel(logging.DEBUG)   
                                                    console_handler = logging.StreamHandler()   
                                                    console_handler.setLevel(logging.ERROR)  
                                            3. formatter - Specifies the formatting strings.   
                                                    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
                                                    file_handler.setFormatter(formatter)  
                                                    console_handler.setFormatter(formatter)  
                                                    # Add handlers to logger  
                                                    logger.addHandler(fh)  
                                                    logger.addHandler(ch)  
-[ ] REGEX  
                                        Metacharacters:  
                                            ^   Matches the beginning.  
                                            $   Matches the end.  
                                            .   Matches any character except newline.  
                                            ?   Matches zero or one occurrence.   
                                            |   Means OR (Matches with any of the characters separated by it.  
                                            *   Any number of occurrences (including 0 occurrences).  
                                            +   One ore more occurrences.  
                                            {}  Indicate number of occurrences of a preceding RE to match.  
                                            []  Represent a character class.  
                                            ()  Enclose a group of REs.  
                                            \   Used to drop the special meaning of character following it.  
                                            \d  Matches any decimal digit, this is equivalent to the set class [0-9].  
                                            \D  Matches any non-digit character.  
                                            \s  Matches any whitespace character.  
                                            \S  Matches any non-whitespace character.  
                                            \w  Matches any alphanumeric character, is equivalent to the [a-zA-Z0-9_].  
                                            \W  Matches any non-alphanumeric character.  
                                        Methods:  
                                            match(p, s)     Returns only 1 Match obj, else None, matches at BEGINNING of str.  
                                            search(p, s)    Returns only 1 Match obj, else None, matches ANYWHERE in str.  
                                            findall(p, s)   Returns List of all matches from str ([] if None).  
                                            finditer(p, s)  Returns Match Iterator, Iterator MAY NOT have next (no match).  
                                            split(p, s)     Returns List of str split on matches, [] if no match.  
                                            sub(p, r, s)    Returns s with all matched p replaced with r, r can be a 
                                                            string or a function, if no match return s.  
                                            subn(p, r, s)   Same as sub() but returns a tuple (new_s, #_of_subs_made), 
                                                            if no matches returns (s, 0)  
                                            fullmatch(p, s) Return ONLY 1 Match obj if ALL of s matches p, None if no match.  
                                            escape(s)       Return str with all non-alphanumerics escaped with backslash.  
                                        Examples:  
                                        import re  
                                        print(re.findall('\d+', "I went to him at 11 A.M. on 4th July 1886"))  
                                        print(re.split('[aeiou]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))  
                                        # The next two lines are essentially the same:  
                                        compiled_pattern = re.compile(pattern); result = compiled_pattern.match(input)  
                                        result = re.match(pattern, input)  
-[ ] Closures  
                                        A closure occurs when a function has access to a local var from an enclosing 
                                        scope that has finished its execution.  
                                        Closures can return functions:   
                                        def outer_function(msg):  
                                            def inner_function():  
                                                print(msg)  
                                            return inner_function  
                                        # The next two lines:  
                                            function = outer_function('hi')  
                                            function()  
                                        # Are the same as: outer_function('hi')()  
-[ ] Decorator  
                                        # Decorators are functions which modify the functionality of other functions.  
                                        # TYPE CHECKER FUNCTION DECORATOR EXAMPLE:  
                                        def type_check(T):  
                                            def decorator(f):  
                                                import functools  
                                                @functools.wraps(f)  
                                                def wrapped(*args):  
                                                    if any([not isinstance(i, T) for i in args]):  
                                                        raise TypeError(f"Parameters not all of type {T.__name__}!")  
                                                    else:  
                                                        return f(*args)  
                                                return wrapped  
                                            return decorator  
                                        
                                        @type_check(int)  
                                        def add_ints(*ints):  
                                            return sum(ints)  
                                        
                                        print(add_ints(1, 2, 3))  
                                        print(add_ints(1, '2', 3))  
                                        
                                        # TIMER CLASS DECORATOR EXAMPLE  
                                        class Timer:  
                                            def __init__(self, fn, *params):  
                                                self.function = fn  
                                                self.params = params  
                                            def __call__(self, *args, **kwargs):  
                                                import time  
                                                start_time = time.time()  
                                                result = self.function(*args, **kwargs)  
                                                end_time = time.time()  
                                                print("Execution of {} took {} seconds".format(self.function.__name__, end_time - start_time))  
                                                return result  
                                        
                                        @Timer  
                                        def sleepy_function():  
                                            import time  
                                            time.sleep(random.random())  
                                        sleepy_function()  

Concurrency
-----------
-[ ] GIL  
                                        Global Interpreter Lock
                                        The mechanism used by the CPython interpreter to assure that only one thread 
                                        executes Python bytecode at a time. This simplifies the CPython implementation 
                                        by making the object model (including critical built-in types such as dict) 
                                        implicitly safe against concurrent access. Locking the entire interpreter makes 
                                        it easier for the interpreter to be multi-threaded, at the expense of much of 
                                        the parallelism afforded by multi-processor machines.
-[ ] Threads/Threading   
                                        # Threading Examples
                                        from threading import Thread
                                        Thread(target=print, args=("I'm a thread!",)).start()
                                        # Run multiple statements in one line via map:
                                        Thread(target=map, args=(lambda x: x, (print("hello"), print("world"))))
                                        # ThreadPoolExecutor creates a reusable pool of threads, CAN return Future objs.  
                                        with ThreadPoolExecutor(max_workers=2) as executor_context_manager:
                                            returned_future = executor_context_manager.submit(my_function)
                                            executor_context_manager.submit(print, "I'm a ThreadPoolExecutor Thread!")
-[ ] Future Object  
                                        A Future represents an eventual result of an asynchronous operation. 
                                        Not thread-safe.
                                        Future instances are created by Executor.submit().
                                        Future methods include:
                                            cancel()                Attempt to cancel the call; return False if done or 
                                                                    executing, else cancel and return True.
                                            cancelled()             Return True if the call was cancelled.
                                            running()               Return True if the call is currently being executed 
                                                                    and cannot be cancelled.
                                            done()                  Return True if the call was successfully cancelled 
                                                                    or finished.
                                            result(timeout=None)    BLOCKING, Return the value returned by the call, 
                                                                    timeout (seconds) can be int or float.
                                            add_done_callback(fn)   Attaches the callable fn to the future. fn will be 
                                                                    called with the future as its only argument, when 
                                                                    the future is cancelled or finishes running.
-[ ] Locks, Semaphore, 
     & Condition (variable)  
                                        (Primitive) Lock - Synchronization primitive, has two states: locked & unlocked.  
                                                           Can only acquire a primitive lock once.  
                                                           Methods: locked(), release(), acquire()
                                        Re-entrant Lock - Lock that can be acquired multiple times by one thread.  
                                                           Methods: release(), acquire()
                                        Semaphore - Internal counter, decremented by acquire(), incremented by release(),
                                                    can't go below zero (it blocks aqcuire() if zero).  
                                                    Methods: acquire(), release()  
                                        Condition (Variable) - Represents state change, associated with lock (either a 
                                                               lock can be passed in or it will create one).  
                                                               Methods: acquire(), release(), wait(), wait_for(), 
                                                                        notify(), notify_all().   
-[ ] Processes  
                                        Python processes (use Thread-like API) sidestep the GIL issue.  
                                        Multiprocessing communication is supported via Queues and Pipes.  
                                        Can be Synchronized via Locks and Connection Objects.  
                                        Can share State via shared memory, or server process.  
                                        ProcessPoolExecutor creates a reusable pool of process, CAN return Future objs.  
                                        # Process Examples:  
                                        from multiprocessing import Process  
                                        Process(target=print, args=("I'm a Process!",)).start()  
                                        # ProcessPoolExecutor Example  
                                        with ProcessPoolExecutor(max_workers=2) as executor_context_manager:  
                                            future_obj = executor_context_manager.submit(nap_time)  
                                            executor_context_manager.submit(print, "I'm a ProcessPoolExecutor Thread!")  

Memory Model & Garbage Collecting
---------------------------------
-[ ] Python Memory Manager  
                                        A private heap contains all the Python objects and data structures.  
                                        Python memory manager manages heap, the user has no control over it.  
                                        There is a Python/C API.  
-[ ] Python Garbage Collector  
                                        Python gc works by reference count.   
                                        The gc module (import gc) contains helpful methods.  
                                        Some gc Methods:  
                                            gc.enable() - Enables automatic garbage collection.  
                                            gc.disable() - Disables automatic garbage collection.  
                                            gc.isenabled() - Return True if automatic collection is enabled.  
                                            gc.collect(generation=2) - Run a full collection (generation can be 0-2).  
                                            gc.set_debug(flags) - Set the gc flags (info is written to sys.stderr).  
                                            gc.get_debug() - Return the debugging flags currently set.   
                                            gc.get_stats() - Return a list of the 3 generation dictionaries containing 
                                                collection statistics since interpreter start.  
                                            gc.get_threshold() - Returns current garbage collection thresholds.    
                                            gc.get_count() - Return current collection counts: (count0, count1, count2).  
                                            gc.freeze() - Freeze all objects tracked by gc - move them to a permanent 
                                                generation and ignore all the future collections.  
                                            gc.unfreeze() - Unfreeze the objects in the permanent generation, put them 
                                                back into the oldest generation.  




