from IPython.display import HTML

def scan_sep():
    """
    a generator to scan the 0..8 space
    second return value is True if index == 2 or 5,
    which corresponds to a separator being needed
    """
    for x1 in range(0, 3):
        for x2 in range(0, 3):
            index = 3*x1 + x2
            needs_sep = (x2 == 2) and (x1 != 2)
            yield index, needs_sep
            

def notebook(grid):
    """
    pretty much like Grid.repr 
    but as a html table instead
    for rendering in a notebook
    """
    style = """
.rendered_html tr.sep {
    background-color: #000; 
    width: 3px;
}
.rendered_html td.sep, .rendered_html th.sep {
    background-color: #000; 
    padding-top: 0px;
    padding-bottom: 0px;
} 
.rendered_html td.digit, .rendered_html th.digit{
    text-color: #000;
    padding-top: 0px;
    padding-bottom: 0px;
    font-family: monaco;
}
"""


    html = ""
    html += f"<style>{style}</style>"
    html += "<table><thead>"
    html += "<tr><th></th>"
    for col, colsep in scan_sep():
        html += f"<th class='digit'>{col+1}</th>"
        if colsep:
            html += "<th class='sep'></th>"
    html += "</tr></thead>"
    
    sepline = 10*'-'
    html += "<tbody>"
    for line, linesep in scan_sep():
        html += f"<tr style='color:white;'><th class='digit'>{line+1}</th>"
        for col, colsep in scan_sep():
            html += f"<td class='digit' style='color:white;'>{grid[line, col]}</td>"
            if colsep:
                html += "<td class='sep' style='background-color:black;'></td>"
        html += "</tr>"
        if linesep:
            html += f"<tr class='sep'><td colspan=13></td></tr>"
    html += "</tbody>"

    html += "</table>"
    return HTML(html)
    

def external_link(grid):
    """
    generate a link to one website
    i.e. something like this
    http://www.sudoku-solutions.com/index.php?page=SUDOKU9BY9&puzzle=\
    ...2............91..79..84....56.7....8.4.....1...3..635....9...2...5....4.7..3..
    """
    url = "http://www.sudoku-solutions.com/index.php?page=SUDOKU9BY9&puzzle="
    def digit_or_dot(i, j):
        c = str(grid[i, j])
        return '.' if c == ' ' else c
    contents = "".join(digit_or_dot(i, j) for i in range(9) for j in range(9))
    return url+contents

def external_iframe(grid):
    return HTML(f"<iframe src={external_link(grid)} width='800' height='500'/>")
