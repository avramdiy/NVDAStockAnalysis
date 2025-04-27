from flask import Flask, render_template_string, Response
import pandas as pd
import matplotlib.pyplot as plt
import io

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
            <h1 class="mt-4">NVDA Data Table for 2000 and 2010</h1>
            {table_html}
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

@app.route("/plot")
def plot_monthly_open():
    # File path
    csv_file = r"C:\Users\Ev\Desktop\TRG Week 21\nvda.us.txt"

    # Load the CSV directly into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Filter for the years 2000 and 2010
    df_2000 = df[df['Date'].dt.year == 2000]
    df_2010 = df[df['Date'].dt.year == 2010]

    # Add 'Month' column
    df_2000['Month'] = df_2000['Date'].dt.month
    df_2010['Month'] = df_2010['Date'].dt.month

    # Aggregate monthly data for 2000
    monthly_open_2000 = df_2000.groupby('Month')['Open'].mean()
    monthly_close_2000 = df_2000.groupby('Month')['Close'].mean()
    monthly_high_2000 = df_2000.groupby('Month')['High'].mean()
    monthly_low_2000 = df_2000.groupby('Month')['Low'].mean()

    # Aggregate monthly data for 2010
    monthly_open_2010 = df_2010.groupby('Month')['Open'].mean()
    monthly_close_2010 = df_2010.groupby('Month')['Close'].mean()
    monthly_high_2010 = df_2010.groupby('Month')['High'].mean()
    monthly_low_2010 = df_2010.groupby('Month')['Low'].mean()

    # Plot the data
    plt.figure(figsize=(14, 10))

    # 2000 Plots (Blue)
    plt.plot(monthly_open_2000.index, monthly_open_2000.values, linestyle='-', color='blue', label='2000 Average Open Price')
    plt.plot(monthly_close_2000.index, monthly_close_2000.values, linestyle='-', color='blue', label='2000 Average Close Price')
    plt.plot(monthly_high_2000.index, monthly_high_2000.values, linestyle='--', color='blue', label='2000 Average High Price')
    plt.plot(monthly_low_2000.index, monthly_low_2000.values, linestyle='--', color='blue', label='2000 Average Low Price')

    # 2010 Plots (Green)
    plt.plot(monthly_open_2010.index, monthly_open_2010.values, linestyle='-', color='green', label='2010 Average Open Price')
    plt.plot(monthly_close_2010.index, monthly_close_2010.values, linestyle='-', color='green', label='2010 Average Close Price')
    plt.plot(monthly_high_2010.index, monthly_high_2010.values, linestyle='--', color='green', label='2010 Average High Price')
    plt.plot(monthly_low_2010.index, monthly_low_2010.values, linestyle='--', color='green', label='2010 Average Low Price')

    # Customize the plot
    plt.title('Aggregate Monthly Prices (Open, Close, High, Low) for 2000 and 2010', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Price', fontsize=14)
    plt.xticks(range(1, 13))
    plt.legend(fontsize=12)
    plt.grid(True)

    # Save the plot to a BytesIO stream
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return Response(img, mimetype='image/png')



if __name__ == "__main__":
    app.run(debug=True)
