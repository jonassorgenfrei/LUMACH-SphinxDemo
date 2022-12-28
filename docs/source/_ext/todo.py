from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

# Node Classes
# ------------
# Node classes usually don't have anything to do except inherit from the 
# standard docutils classes defined in docutils.nodes
class todo(nodes.Admonition, nodes.Element):
    """Inherites from Admonition because it should be 
    hangled like a note or warning
    """
    pass


class todolist(nodes.General, nodes.Element):
    """Just a 'general' node
    """
    pass


def visit_todo_node(self, node):
    self.visit_admonition(node)


def depart_todo_node(self, node):
    self.depart_admonition(node)


# directive classes
# -----------------
class TodolistDirective(Directive):
    def run(self):
        """Returns a list of nodes
        
        Returns:
            list of nodes: list of docutil nodes
        """
        return [todolist("")]


class TodoDirective(SphinxDirective):
    """

    Subclassing the SphinxDirective helper class to get access to the build environment instance
    (self.env)
    """
    # this enables content in the directive
    has_content = True

    def run(self):
        """Returns a list of nodes
        
        Returns:
            list of nodes: list of docutil nodes
        """
        # in html, this will be the anchor name
        # new_serialno will return a new unique integer on each call 
        # and therefore leads to unique target names
        targetid = "todo-%d" % self.env.new_serialno("todo")
        # target node instanciated without any text
        targetnode = nodes.target("", "", ids=[targetid])
        todo_node = todo("\n".join(self.content))
        todo_node += nodes.title(_("Todo"), _("Todo"))
        # parse content of the body of the directive
        self.state.nested_parse(self.content, self.content_offset, todo_node)
        # create a list of all todos
        if not hasattr(self.env, "todo_all_todos"):
            self.env.todo_all_todos = []

        self.env.todo_all_todos.append(
            {
                "docname": self.env.docname,
                "lineno": self.lineno,
                "todo": todo_node.deepcopy(),
                "target": targetnode,
            }
        )

        # needs to return a target node and a todo node
        return [targetnode, todo_node]


# The event handlers
# ------------------
# one of sphinx most powerfull features, providing a way to do hook into any part of 
# the documentation process
def purge_todos(app, env, docname):
    """Handle for env-purge-doc

    Since we store information from source files in the environment, 
    which is persistent, it may become out of date when the source file changes.
    before each source file is read, the environment’s records of it are cleared


    Args:
        app (_type_): _description_
        env (_type_): _description_
        docname (_type_): _description_
    """
    if not hasattr(env, "todo_all_todos"):
        return

    # clear out all todos whose docname matches the given one from 
    # the todo_all_todos list
    env.todo_all_todos = [
        todo for todo in env.todo_all_todos if todo["docname"] != docname
    ]


def merge_todos(app, env, docnames, other):
    """Handler for env-merge-info

    Used during parallel builds.  During parallel builds all threads have their own env.
    merge todo lists

    Args:
        app (_type_): _description_
        env (_type_): _description_
        docnames (_type_): _description_
        other (_type_): _description_
    """
    if not hasattr(env, "todo_all_todos"):
        env.todo_all_todos = []
    if hasattr(other, "todo_all_todos"):
        env.todo_all_todos.extend(other.todo_all_todos)


def process_todo_nodes(app, doctree, fromdocname):
    """Handler for doctree-resolved
    
    emitted at the end of phase 3 (resolving), allows custom resolving to be done

    Args:
        app (_type_): _description_
        doctree (_type_): _description_
        fromdocname (_type_): _description_
    """
    # if todo_include_todos config value is false, remove all todo and todolist nodes
    if not app.config.todo_include_todos:
        for node in doctree.findall(todo):
            node.parent.remove(node)
    # Replace all todolist nodes with a list of the collected todos.
    # Augment each todo with a backlink to the original location.
    env = app.builder.env
    if not hasattr(env, "todo_all_todos"):
        env.todo_all_todos = []
    for node in doctree.findall(todolist):
        if not app.config.todo_include_todos:
            node.replace_self([])
            continue
        # todolist nodes are replaced by a list of todo entries
        content = []
        for todo_info in env.todo_all_todos:
            para = nodes.paragraph()
            filename = env.doc2path(todo_info["docname"], base=None)
            # paragraph for each entry, contaiing text that gives the location 
            description = _(
                "(The original entry is located in %s, line %d and can be found "
            ) % (filename, todo_info["lineno"])
            para += nodes.Text(description)
            # Create a reference
            newnode = nodes.reference("", "")
            innernode = nodes.emphasis(_("here"), _("here"))
            newnode["refdocname"] = todo_info["docname"]
            # backlinks where the node comes from
            newnode["refuri"] = app.builder.get_relative_uri(
                fromdocname, todo_info["docname"]
            )

            # anchor -> target id
            newnode["refuri"] += "#" + todo_info["target"]["refid"]
            newnode.append(innernode)
            para += newnode
            para += nodes.Text(".)")

            # Insert into the todolist
            content.append(todo_info["todo"])
            content.append(para)
        node.replace_self(content)


def setup(app):
    # add config value to sphinx config. 
    # set default value and indirectly set data type
    # if third argument was html,HTML documents would be full rebuild if the config value changed its value
    app.add_config_value("todo_include_todos", False, "html")
    # adds new node class to the build system
    # can defined visitor functions when the new nodes stay until phase 4 (writing)
    app.add_node(todolist)
    app.add_node(
        todo,
        html=(visit_todo_node, depart_todo_node),
        latex=(visit_todo_node, depart_todo_node),
        text=(visit_todo_node, depart_todo_node),
    )

    # adds new directiyve given by name and class
    app.add_directive("todo", TodoDirective)
    app.add_directive("todolist", TodolistDirective)
    # adds event handler to the event whose name is given by the first argument
    app.connect("doctree-resolved", process_todo_nodes)
    app.connect("env-purge-doc", purge_todos)
    app.connect("env-merge-info", merge_todos)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
