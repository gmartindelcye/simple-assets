def generate_html_form(asset_info):
    form_template = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>Asset Information Form</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body>
      <h1>Asset Information Form</h1>
      
      <form action="/submit" method="post">
        {% for key, value in asset_info.items() %}
          <div class="mb-3">
            <label for="{{ key }}" class="form-label">{{ key|title }}:</label>
            <input type="text" id="{{ key }}" name="{{ key }}" value="{{ value }}" class="form-control" required>
          </div>
        {% endfor %}
        
        <input type="submit" value="Submit" class="btn btn-primary">
      </form>
      
    </body>
    </html>
    """

    from jinja2 import Template
    template = Template(form_template)
    return template.render(asset_info=asset_info)
