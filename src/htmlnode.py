
class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list['HTMLNode'] | None = None, props: dict[str, str] | None = None) -> None:
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list['HTMLNode'] | None = children
        self.props: dict[str, str] | None = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if not self.props:
            return ''
        parts: list[str] = []
        for prop in self.props:
            parts.append(f' {prop}="{self.props[prop]}"')
        to_html: str = ''.join(parts)
        return to_html
    
    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError('LeafNode must have a value!')
        if self.tag is None:
            return self.value
        else:
            props: str = '' if not self.props else self.props_to_html()
            return f'<{self.tag}{props}>{self.value}</{self.tag}>'
        
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str | None, children: list[HTMLNode] | None, props: dict[str, str] | None = None) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError('ParentNode must have a tag!')
        if not self.children:
            raise ValueError('ParentNode is missing children!')
        else:
            child_strings: list[str] = []
            for child in self.children:
                child_strings.append(child.to_html())
            result: str = ''.join(child_strings)
            return f'<{self.tag}>{result}</{self.tag}>'
