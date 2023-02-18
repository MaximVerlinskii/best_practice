# text = 'hello'
# parts = ['<p>', text, '</p>']
# print(''.join(parts))
#
# words = ['yo', 'ye']
# parts = ['<ul>']
# for w in words:
#     parts.append(f' <li>{w}</li>')
# parts.append('</ul>')
# print('\n'.join(parts))


class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []

    def _str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e._str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self._str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self._root = HtmlElement(name=root_name)

    def add_child(self, child_name, child_text):
        self._root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self._root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self._root)


if __name__ == '__main__':
    builder = HtmlBuilder('ul')
    builder.add_child('li', 'yo')
    builder.add_child('li', 'ye')
    print('Ordinary builder:')
    print(builder)

    builder = HtmlElement.create('ul')
    builder.add_child_fluent('li', 'yo').add_child_fluent('li', 'ye')
    print('Ordinary builder 2:')
    print(builder)
