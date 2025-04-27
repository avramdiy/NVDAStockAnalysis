from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route("/")
def load_and_display():
    # File path
    csv_file = r"C:\Users\Ev\Desktop\TRG Week 21\nvda.us.txt"

    # Load the CSV directly into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter for the years 2000 and 2020
    filtered_df = df[(df['Date'].dt.year == 2000) | (df['Date'].dt.year == 2010)]

    # Remove the "OpenInt" column
    filtered_df = filtered_df.drop(columns=["OpenInt"])

    # Convert filtered DataFrame to HTML
    table_html = filtered_df.to_html(classes="table table-bordered", index=False)

    # Render HTML page
    html_template = f"""
    <!doctype html>
    <html>
    <head>
        <title>Filtered Data Table</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1 class="mt-4">NVDA Data Table for 2000 and 2020</h1>
            {table_html}
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
