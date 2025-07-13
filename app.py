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

# Callbacks and logic will be added here

if __name__ == "__main__":
    app.run(debug=True)
