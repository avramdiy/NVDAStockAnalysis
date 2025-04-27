from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route("/")
def load_and_display():
    # File path
    csv_file = r"C:\Users\Ev\Desktop\TRG Week 21\nvda.us.txt"

    # Load the CSV directly into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert DataFrame to HTML
    table_html = df.to_html(classes="table table-bordered", index=False)

    # Render HTML page
    html_template = f"""
    <!doctype html>
    <html>
    <head>
        <title>Data Table</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1 class="mt-4">NVDA Data Table</h1>
            {table_html}
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
