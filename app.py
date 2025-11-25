from dash import Dash, html, dcc, Input, Output
import plotly.express as px

external_scripts = ["https://cdn.tailwindcss.com"]
app = Dash(__name__, external_scripts=external_scripts)

df = px.data.gapminder().query("country == 'Panama' and year >= 1980")
fig = px.line(df, x="year", y="gdpPercap", markers=True)
fig.update_layout(
    margin=dict(l=20, r=20, t=40, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

SIDEBAR_BASE_CLASSES = (
    "h-screen bg-slate-950 border-r border-slate-800 p-4 "
    "flex flex-col transition-all duration-200"
)

app.layout = html.Div(
    className="min-h-screen bg-slate-900 text-slate-100 flex",
    children=[
        html.Div(
            id="sidebar",
            className=SIDEBAR_BASE_CLASSES,
            style={"width": "16rem"},
            children=[
                html.Div(
                    id="sidebar-title",
                    className="text-xl font-semibold mb-6 whitespace-nowrap",
                    style={"display": "block"},
                    children=html.Div(
                        className="flex items-center",
                        children=[
                            html.Img(
                                src="/assets/CIHH Logo.png",
                                className="w-8 h-8 mr-3 rounded-full",
                                alt="Logo CIHH",
                            ),
                            html.Span("CIHH"),
                        ]
                    ),
                ),
                
                html.Nav(
                    className="space-y-2 mt-2",
                    children=[
                        html.A(
                            children=[
                                html.Span("🏠", className="text-xl"),
                                html.Span(
                                    "Overview",
                                    id="label-overview",
                                    className="ml-3 text-sm",
                                    style={"display": "inline-block"},
                                ),
                            ],
                            href="#",
                            className="flex items-center justify-start px-3 py-2 rounded-lg bg-indigo-600",
                        ),
                        html.A(
                            children=[
                                html.Span("🌦️", className="text-xl"),
                                html.Span(
                                    "Meteorología",
                                    id="label-met",
                                    className="ml-3 text-sm",
                                    style={"display": "inline-block"},
                                ),
                            ],
                            href="#",
                            className="flex items-center justify-start px-3 py-2 rounded-lg hover:bg-slate-800",
                        ),
                        html.A(
                            children=[
                                html.Span("🟢", className="text-xl"),
                                html.Span(
                                    "CO₂",
                                    id="label-co2",
                                    className="ml-3 text-sm",
                                    style={"display": "inline-block"},
                                ),
                            ],
                            href="#",
                            className="flex items-center justify-start px-3 py-2 rounded-lg hover:bg-slate-800",
                        ),
                        html.A(
                            children=[
                                html.Span("💧", className="text-xl"),
                                html.Span(
                                    "H₂O / ET",
                                    id="label-h2o",
                                    className="ml-3 text-sm",
                                    style={"display": "inline-block"},
                                ),
                            ],
                            href="#",
                            className="flex items-center justify-start px-3 py-2 rounded-lg hover:bg-slate-800",
                        ),
                    ],
                ),

                html.Div(
                    className="mt-auto text-xs text-slate-500",
                    children="v0.1 demo",
                ),
            ],
        ),

        html.Div(
            className="flex-1 p-6 space-y-4",
            children=[
                # Header
                html.Div(
                    className="flex items-center justify-between",
                    children=[
                        html.Button(
                            "☰",
                            id="btn-toggle-sidebar",
                            n_clicks=0,
                            className="mr-4 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700",
                        ),
                        html.H1(
                            "Dashboard de Flujos",
                            className="text-2xl font-semibold flex-1",
                        ),
                        html.Div(
                            className="text-sm text-slate-400",
                            children="Demo mínima con Dash 3 + Tailwind CDN",
                        ),
                    ],
                ),

                html.Div(
                    className="grid grid-cols-2 md:grid-cols-4 gap-4",
                    children=[
                        html.Div(
                            className="rounded-2xl bg-slate-800/70 p-4",
                            children=[
                                html.Div(
                                    "CO₂ total",
                                    className="text-xs text-slate-400",
                                ),
                                html.Div("1234", className="text-2xl font-semibold"),
                            ],
                        ),
                        html.Div(
                            className="rounded-2xl bg-slate-800/70 p-4",
                            children=[
                                html.Div(
                                    "H₂O / ET",
                                    className="text-xs text-slate-400",
                                ),
                                html.Div("56.7", className="text-2xl font-semibold"),
                            ],
                        ),
                    ],
                ),

                html.Div(
                    className="rounded-2xl bg-slate-800/70 p-4",
                    children=[
                        html.Div(
                            "Ejemplo de gráfica",
                            className="mb-2 text-sm text-slate-300",
                        ),
                        dcc.Graph(
                            id="main-graph",
                            figure=fig,
                            className="h-80",
                        ),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(
    Output("sidebar", "style"),
    Output("sidebar-title", "style"),
    Output("label-overview", "style"),
    Output("label-met", "style"),
    Output("label-co2", "style"),
    Output("label-h2o", "style"),
    Input("btn-toggle-sidebar", "n_clicks"),
)
def toggle_sidebar(n_clicks):
    if n_clicks is None or n_clicks % 2 == 0:
        sidebar_style = {"width": "16rem"}
        show = {"display": "inline-block"}
        return sidebar_style, show, show, show, show, show

    sidebar_style = {"width": "4.5rem"}
    hide = {"display": "none"}
    return sidebar_style, hide, hide, hide, hide, hide


if __name__ == "__main__":
    app.run(debug=True)
