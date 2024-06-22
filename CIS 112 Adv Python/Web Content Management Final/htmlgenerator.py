# this is a 'script' that generatos the html file to display. Modifies the
# existing HTML file index.html


def gen_html(title, content):
    """
    this function generates the html code to be written to an external html file
    using the parameter values.
    ----
    @title: {string} the title of the website to be set
    @content: {string} the new content of the website to set
    """
    html_out = open("index.html", "w")

    # html code saved as a multiline string with parameter inputs
    html_code = f"""
<!doctype html>
<html lang="eng">
  <head>
    <meta charset="UTF-8" />
    <title>{title}</title>
  </head>

  <body>
      <h1>{title}</h1>
      <p>{content}</p>
  </body>
</html>
"""

    # write out html code to file
    html_out.write(html_code)
    html_out.close()
    return
