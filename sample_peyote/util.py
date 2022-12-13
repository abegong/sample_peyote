def indent(text, amount, ch=' '):
    padding = amount * ch
    return ''.join(padding+line for line in text.splitlines(True))

assert indent("hello", 2) == "  hello"
assert indent("hello\ngoodbye", 2) == "  hello\n  goodbye"
assert indent("""maybe
maybe
  maybe not""", 2) == """  maybe
  maybe
    maybe not"""
