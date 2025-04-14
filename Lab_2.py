from abc import ABC, abstractmethod

# Base Component
class Text(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Component
class PlainText(Text):
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content

# Base Decorator
class TextDecorator(Text):
    def __init__(self, wrapped_text):
        self.wrapped_text = wrapped_text

    def render(self):
        return self.wrapped_text.render()

# Concrete Decorators
class BoldDecorator(TextDecorator):
    def render(self):
        return f"<b>{super().render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self):
        return f"<i>{super().render()}</i>"

class UnderlineDecorator(TextDecorator):
    def render(self):
        return f"<u>{super().render()}</u>"

# Client Code
if __name__ == "__main__":
    text = PlainText("Hello, Decorator Pattern!")

    bold_text = BoldDecorator(text)
    italic_bold_text = ItalicDecorator(bold_text)
    fully_decorated = UnderlineDecorator(italic_bold_text)

    print("Bold:", bold_text.render())
    print("Bold + Italic:", italic_bold_text.render())
    print("Fully Decorated:", fully_decorated.render())
