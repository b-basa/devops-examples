import requests
from dash import Dash, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            "Submit",
            id="submit-val",
            n_clicks=0,
            style={"width": "100%", "height": "500px", "background-color": "#6495ED"},
        ),
    ]
)


@callback(
    Output("submit-val", "children"),
    Input("submit-val", "n_clicks"),
    prevent_initial_call=True,
)
def update_output(n_clicks):
    response = requests.get("http://backend:5000/random-number")
    random_number = response.text
    return f"Clicked {n_clicks} times! Random number from backend: {random_number}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
