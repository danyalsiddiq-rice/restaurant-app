import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

# Initial empty DataFrame for restaurants
df = pd.DataFrame(columns=["name", "category", "address", "rating", "reviews"])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Restaurant Review App"),
    dbc.Row([
        dbc.Col([
            html.H3("Add a Restaurant"),
            dbc.Input(id="name-input", placeholder="Name", type="text"),
            dbc.Input(id="category-input", placeholder="Category", type="text", className="mt-2"),
            dbc.Input(id="address-input", placeholder="Address", type="text", className="mt-2"),
            dbc.Button("Add", id="add-btn", color="primary", className="mt-2"),
            html.Div(id="add-msg", className="mt-2")
        ], width=4),
        dbc.Col([
            html.H3("Search Restaurants"),
            dbc.Input(id="search-input", placeholder="Search by name or category", type="text"),
            html.Div(id="restaurant-list", className="mt-2")
        ], width=8)
    ]),
    html.Hr(),
    html.Div(id="restaurant-details")
], fluid=True)


# Store restaurants in a global DataFrame (for demo; use persistent storage for production)

@app.callback(
    Output("add-msg", "children"),
    Output("restaurant-list", "children"),
    Input("add-btn", "n_clicks"),
    State("name-input", "value"),
    State("category-input", "value"),
    State("address-input", "value"),
    prevent_initial_call=True
)
def add_restaurant(n_clicks, name, category, address):
    global df
    msg = ""
    if not name or not category or not address:
        msg = dbc.Alert("Please fill all fields.", color="danger")
    else:
        df.loc[len(df)] = {
            "name": name,
            "category": category,
            "address": address,
            "rating": None,
            "reviews": []
        }
        msg = dbc.Alert(f"Added {name} successfully!", color="success")
    # Show updated list
    return msg, render_restaurant_list(df)

def render_restaurant_list(df):
    if df.empty:
        return html.Div("No restaurants yet.")
    cards = []
    for i, row in df.iterrows():
        cards.append(
            dbc.Card([
                dbc.CardBody([
                    html.H5(row["name"], className="card-title"),
                    html.P(f"Category: {row['category']}"),
                    html.P(f"Address: {row['address']}")
                ])
            ], className="mb-2")
        )
    return cards

if __name__ == "__main__":
    app.run(debug=True)
