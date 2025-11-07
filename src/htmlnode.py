

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
        