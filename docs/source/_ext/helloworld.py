from docutils import nodes
from docutils.parsers.rst import Directive

class HelloWorld(Directive):
    """Declares directive, extends docutils Directive class

    Args:
        Directive (_type_): _description_
    """
    def run(self):
        # create new paragraph node
        paragraph_node = nodes.paragraph(text="Hello World!")
        # return list of docutil nodes
        return [paragraph_node]

def setup(app):
    """Function to plug the new directive into Sphinx

    Args:
        app (_type_): _description_

    Returns:
        _type_: _description_
    """
    app.add_directive("helloworld", HelloWorld)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
