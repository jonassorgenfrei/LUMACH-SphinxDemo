Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. py:function:: lumache.get_random_ingredients_manual(kind=None)

   MANUAL DEFINITION
   Return a list of random ingredients as strings.

   :param kind: Optional "kind" of ingredients.
   :type kind: list[str] or None
   :raise lumache.InvalidKindError: If the kind is invalid.
   :return: The ingredients list.
   :rtype: list[str]

.. autofunction:: lumache.get_random_ingredients

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

.. py:exception:: lumache.InvalidKindErrorMANUAL

   MANUAL DEFINITION
   Raised if the kind is invalid.

.. cpp:type:: std::vector<int> CustomList

   A typedef-like declaration of a type.

Cross reference to :cpp:type:`CustomList`.

.. autoclass:: lumache.MyClass
   :members:

.. autoclass:: lumache.MyClass2
   :show-inheritance:
   :members:
   :inherited-members:

.. autoclass:: lumache.MyClass3
   :members:

.. autoclass:: lumache.MyClass4
   :members: