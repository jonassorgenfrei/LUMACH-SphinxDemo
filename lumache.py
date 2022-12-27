"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def get_random_ingredients(kind=None):
    """Return a list of random ingredients as strings.

    A more complexe multiline description of the function 
    itself.

    Args:
        kind (list[str] or None): Optional "kind" of ingredients.
    
    Raises: 
        lumache.InvalidKindError: If the kind is invalid.
    
    Returns: 
        list[str]: The ingredients list.
    """
    return ["shells", "gorgonzola", "parsley"]

class MyClass:
    """Summary of class here.

    Longer class information...
    Longer class information...

    Attributes:
        likes_spam (bool): A boolean indicating if we like SPAM or not.
        eggs (int): An integer count of the eggs we have laid.
    """
    def __init__(self, likes_spam: bool = False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""

class MyClass2(MyClass):
    """Summary of class2 here.

    Longer class information...
    Longer class information...
    """

    def public_method2(self):
        """Performs operation 2 blah."""

class MyClass3():
    """Summary of class3 here.

    Longer class information...
    Longer class information...

    Attributes:
        ref (MyClass): A refernce to MyClass
    """

    def __init__(self, ref):
        """Inits SampleClass with blah.
        """
        self.ref = ref

class MyClass4():
    """Summary of class4 here.

    Longer class information...
    Longer class information...

    Attributes:
        ref: A refernce to MyClass
    """

    def __init__(self, ref: MyClass):
        """Inits SampleClass with blah.
        """
        self.ref = ref

class MyClass5():
    """Summary of class5 here.

    Longer class information...
    Longer class information...

    Attributes:
        ref: A refernce to MyClass4
    """

    def __init__(self, ref: MyClass4):
        """Inits SampleClass with blah.
        """
        self.ref = ref