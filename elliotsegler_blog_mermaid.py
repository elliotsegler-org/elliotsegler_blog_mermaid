from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

import re
import json

MermaidRegex = re.compile(r"^(?P<mermaid_sign>[\~\`]){3}[\ \t]*[Mm]ermaid[\ \t]*$")


# ------------------ The Markdown Extension -------------------------------

class MermaidPreprocessor(Preprocessor):

    def _render_config(self):
        return json.dumps(self.config)

    def run(self, lines):
        new_lines = []
        mermaid_sign = ""
        m_start = None
        m_end = None
        in_mermaid_code = False
        is_mermaid = False
        for line in lines:
            # Wait for starting line with MermaidRegex (~~~ or ``` following by [mM]ermaid )
            if not in_mermaid_code:
                m_start = MermaidRegex.match(line)
            else:
                m_end = re.match(r"^["+mermaid_sign+"]{3}[\ \t]*$", line)
                if m_end:
                    in_mermaid_code = False

            if m_start:
                in_mermaid_code = True
                mermaid_sign = m_start.group("mermaid_sign")
                if not re.match(r"^[\ \t]*$", old_line):
                    new_lines.append("")
                if not is_mermaid:
                    is_mermaid = True
                    #new_lines.append('<style type="text/css"> @import url("https://cdn.rawgit.com/knsv/mermaid/0.5.8/dist/mermaid.css"); </style>')
                new_lines.append('<div class="mermaid">')
                m_start = None
            elif m_end:
                new_lines.append('</div>')
                new_lines.append("")
                m_end = None
            elif in_mermaid_code:
                new_lines.append(line.strip())
            else:

                new_lines.append(line)

            old_line = line

        if is_mermaid:
            new_lines.append('')
            #new_lines.append('<script src="https://cdn.rawgit.com/knsv/mermaid/0.5.8/dist/mermaid.min.js"></script>')
            new_lines.append('<script>mermaid.initialize('+self._render_config()+');</script>')

        return new_lines


class MermaidExtension(Extension):
    """ Add source code hilighting to markdown codeblocks. """

    def __init__(self, **kwargs):
        self.config = {
            'theme' : ['default', 'description1'],
            'startOnLoad' : [True, 'description2']
        }
        super(MermaidExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        """ Add HilitePostprocessor to Markdown instance. """
        # Insert a preprocessor before ReferencePreprocessor
        mermaid = MermaidPreprocessor(md)
        print(self.getConfigInfo())
        mermaid.config = self.getConfigs()
        md.preprocessors.register(mermaid, 'mermaid', 35)
        md.registerExtension(self)

def makeExtension(**kwargs):  # pragma: no cover
    return MermaidExtension(**kwargs)
