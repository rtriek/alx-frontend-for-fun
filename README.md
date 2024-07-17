# ALX frontend for fun
# Markdown to HTML
## Description
Markdown is awesome! All your README.md files are made in Markdown, but do you know how GitHub renders them?
It’s time to code a Markdown to HTML converter!

## Overview
In this project, you will create a program that converts Markdown files to HTML files. This will help you understand how Markdown is parsed and rendered into HTML, similar to how GitHub processes README.md files.

## Learning Objectives
By the end of this project, you are expected to be able to:
- Understand the syntax and structure of Markdown.
- Parse Markdown files and convert them to HTML.
- Implement a Markdown to HTML converter using Python.
- Handle different Markdown elements such as headings, lists, links, images, and more.
- Ensure your converter produces well-formed and valid HTML.

## Resources
Read or watch:
- [Markdown Guide](https://www.markdownguide.org/)
- [CommonMark Specification](https://spec.commonmark.org/)
- [Python Documentation](https://docs.python.org/3/)
- [HTML Living Standard](https://html.spec.whatwg.org/multipage/)

## Key Features to Implement

1. **Headings**: Convert Markdown headings to HTML headings (`<h1>`, `<h2>`, etc.).
2. **Paragraphs**: Convert plain text and newlines to HTML paragraphs (`<p>`).
3. **Bold and Italics**: Convert Markdown bold (`**text**`) and italics (`*text*`) to HTML tags (`<strong>`, `<em>`).
4. **Lists**: Convert Markdown lists to HTML lists (`<ul>`, `<ol>`, `<li>`).
5. **Links**: Convert Markdown links (`[text](url)`) to HTML anchor tags (`<a>`).
6. **Images**: Convert Markdown images (`![alt text](url)`) to HTML image tags (`<img>`).
7. **Code Blocks**: Convert Markdown code blocks (``` code ```) to HTML `<pre><code>` blocks.
8. **Blockquotes**: Convert Markdown blockquotes (`> text`) to HTML blockquote tags (`<blockquote>`).

## Example
### Input (Markdown):
```markdown
# Sample Document
This is a sample document.

## Subheading
- Item 1
- Item 2
- Item 3

**Bold Text** and *Italic Text*.

[Link to Google](https://www.google.com)

![Sample Image](https://www.example.com/image.jpg)
```

### Output (HTML):
```html
<h1>Sample Document</h1>
<p>This is a sample document.</p>
<h2>Subheading</h2>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
<p><strong>Bold Text</strong> and <em>Italic Text</em>.</p>
<p><a href="https://www.google.com">Link to Google</a></p>
<p><img src="https://www.example.com/image.jpg" alt="Sample Image"></p>
```

## How to Run
1. Implement the Markdown to HTML converter in a Python script.
2. Save the Markdown content in a file (e.g., `sample.md`).
3. Run your Python script to convert the Markdown file to an HTML file (e.g., `output.html`).

## Conclusion
By completing this project, you will gain a deeper understanding of both Markdown and HTML. You'll also improve your skills in parsing and converting text, as well as working with file input/output in Python.