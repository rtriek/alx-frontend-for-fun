#!/usr/bin/python3
""" A script markdown2html.py that takes an argument 2 strings """
import sys
import os.path
import re
import hashlib


if __name__ == '__main__':
    """Check if number of arguments is less than 2"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    """Check if markdown file exist"""
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
    else:
        with open(sys.argv[1], "r") as r:
            with open(sys.argv[2], "w") as w:
                start_ul, start_ol, start_p = False, False, False
                for line in r:

                    # Bold and emphasis text
                    line = line.replace("**", "<b>", 1)
                    line = line.replace("**", "</b>", 1)
                    line = line.replace("__", "<em>", 1)
                    line = line.replace("__", "</em>", 1)

                    # convert in MD5 (lowercase)
                    md5 = re.findall(r'\[\[.+?\]\]', line)
                    md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
                    if md5:
                        line = line.replace(md5[0], hashlib.md5(
                            md5_inside[0].encode()).hexdigest())

                    # Remove all c (case insensitive)
                    remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
                    remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
                    if remove_letter_c:
                        remove_c_more = ''.join(
                            c for c in remove_c_more[0] if c not in 'Cc')
                        line = line.replace(remove_letter_c[0], remove_c_more)

                    length = len(line)
                    heading_content = line.lstrip('#')
                    heading_nbr = length - len(heading_content)
                    unordered_content = line.lstrip('-')
                    unordered_nbr = length - len(unordered_content)
                    ordered_content = line.lstrip('*')
                    ordered_nbr = length - len(ordered_content)

                    # headings
                    if heading_nbr in range(1, 7):
                        # close Unordered Listing
                        if start_ul:
                            w.write('</ul>\n')
                            start_ul = False
                        # close Ordered Listing
                        if start_ol:
                            w.write('</ol>\n')
                            start_ol = False
                        # close paragraph
                        if start_p:
                            w.write('</p>\n')
                            start_p = False

                        html_line = '<h{}>{}</h{}>\n'.format(
                                heading_nbr, heading_content.strip(),
                                heading_nbr)
                        w.write(html_line)

                    # Unordered Listing
                    if unordered_nbr and unordered_nbr == 1:
                        if not start_ul:
                            w.write('<ul>\n')
                            start_ul = True
                        html_line = '<li>{}</li>\n'.format(
                                unordered_content.strip())
                        w.write(html_line)
                    if start_ul and not unordered_nbr:
                        w.write('</ul>\n')
                        start_ul = False

                    # Ordered Listing
                    if ordered_nbr and ordered_nbr == 1:
                        if not start_ol:
                            w.write('<ol>\n')
                            start_ol = True
                        html_line = '<li>{}</li>\n'.format(
                                ordered_content.strip())
                        w.write(html_line)
                    if start_ol and not ordered_nbr:
                        w.write('</ol>\n')
                        start_ol = False

                    # Simple text
                    if not (heading_nbr or start_ul or start_ol):
                        if length > 1 and not start_p:
                            w.write('<p>\n')
                            w.write("{}\n".format(line.strip()))
                            start_p = True
                        elif length > 1 and start_p:
                            w.write("<br/>\n")
                            w.write("{}\n".format(line.strip()))
                        if length == 1 and start_p:
                            w.write('</p>\n')
                            start_p = False

                # close Unordered Listing
                if start_ul:
                    w.write('</ul>\n')
                    start_ul = False

                # close Ordered Listing
                if start_ol:
                    w.write('</ol>\n')
                    start_ol = False

                # close paragraph
                if start_p:
                    w.write('</p>\n')
                    start_p = False
        exit(0)
