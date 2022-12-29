from enum import IntEnum
from typing import Any, Optional

from docutils.statemachine import StringList
from sphinx.application import Sphinx
from sphinx.ext.autodoc import ClassDocumenter, bool_option


class IntEnumDocumenter(ClassDocumenter):
    """Auto Documenter class

    Derivated form ClassDocumenter
    """
    objtype = "intenum"  # determines the auto directive name.(in this case the auto directive will be autointenum)
    directivetype = ClassDocumenter.objtype  # sets the generated directive name (here :py:class::)
    priority = 10 + ClassDocumenter.priority  # the larger the number, the higher the prio. 
                                              # documenter be highter then the parents prio
    option_spec = dict(ClassDocumenter.option_spec)  # coppy parents option specifications 
    option_spec["hex"] = bool_option  # add new option hex

    @classmethod
    def can_document_member(
        cls, member: Any, membername: str, isattr: bool, parent: Any
    ) -> bool:
        """Checks if the extension can document the passed object and returns True in that 
        case.

        This member is important to override.

        Args:
            member (Any): _description_
            membername (str): _description_
            isattr (bool): _description_
            parent (Any): _description_

        Returns:
            bool: _description_
        """
        try:
            return issubclass(member, IntEnum)
        except TypeError:
            return False

    def add_directive_header(self, sig: str) -> None:
        """Generates the directive header.

        We add :final: directive option.
        Remember to call super no directive will be generated.

        Args:
            sig (str): _description_
        """
        super().add_directive_header(sig)
        self.add_line("   :final:", self.get_sourcename())

    def add_content(
        self, more_content: Optional[StringList], no_docstring: bool = False
    ) -> None:
        """This method generates the body of the class documentation. After calling the super method 
        we generate lines for enum description.

        Args:
            more_content (Optional[StringList]): _description_
            no_docstring (bool, optional): _description_. Defaults to False.
        """
        super().add_content(more_content)
        source_name = self.get_sourcename()
        enum_object: IntEnum = self.object
        use_hex = self.options.hex
        self.add_line("", source_name)
        for the_member_name, enum_member in enum_object.__members__.items():
            the_member_value = enum_member.value
            if use_hex:
                the_member_value = hex(the_member_value)

            self.add_line(f"**{the_member_name}**: {the_member_value}", source_name)
            self.add_line("", source_name)


def setup(app: Sphinx) -> None:
    # pull autodoc extension, because new extension depends on autodoc.add_autodocumenter()
    app.setup_extension("sphinx.ext.autodoc")  # Require autodoc extension
    app.add_autodocumenter(IntEnumDocumenter)
