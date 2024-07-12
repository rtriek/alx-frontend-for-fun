#!/usr/bin/python3
"""
markdown2html module
Converts a markdown file to HTML.
"""

import sys
import os


def convert_markdown_to_html(markdown_file, html_file):
    """
    Converts the content of a markdown file to HTML.
    """
    try:
        with open(markdown_file, 'r') as md_file:
            with open(html_file, 'w') as html_file:
                in_list = False
                for line in md_file:
                    line = line.rstrip()
                    if line.startswith("#"):
                        heading_level = line.count("#", 0, 6)
                        if heading_level <= 6:
                            line_content = line[heading_level:].strip()
                            start_tag = f"<h{heading_level}>"
                            end_tag = f"</h{heading_level}>"
                            line = f"{start_tag}{line_content}{end_tag}"
                        if in_list:
                            html_file.write("</ul>\n")
                            in_list = False
                    elif line.startswith("- "):
                        if not in_list:
                            html_file.write("<ul>\n")
                            in_list = True
                        line_content = line[2:].strip()
                        line = f"<li>{line_content}</li>"
                    else:
                        if in_list:
                            html_file.write("</ul>\n")
                            in_list = False
                    html_file.write(line + '\n')
                if in_list:
                    html_file.write("</ul>\n")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(markdown_file, html_file)