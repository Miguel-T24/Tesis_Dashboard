from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# =========================
# Configuración básica
# =========================

external_scripts = ["https://cdn.tailwindcss.com"]

app = Dash(
    __name__,
    external_scripts=external_scripts,
    title="Dashboard CIHH – Manglar Juan Díaz",
)

SIDEBAR_BASE_CLASSES = (
    "h-screen bg-slate-950 border-r border-slate-800 p-4 "
    "flex flex-col transition-all duration-200"
)

# =========================
# Datos de ejemplo con fechas
# =========================

date_range = pd.date_range("2020-01-01", "2020-12-31", freq="D")
df_time = pd.DataFrame(
    {
        "date": date_range,
        "value": 50 + 10 * np.sin(np.linspace(0, 6 * np.pi, len(date_range))),
    }
)

# =========================
# Layout
# =========================

app.layout = html.Div(
    className="min-h-screen bg-slate-900 text-slate-100 flex",
    children=[
        # ==== SIDEBAR ====
        html.Div(
            id="sidebar",
            className=SIDEBAR_BASE_CLASSES,
            style={"width": "16rem"},  # ancho grande inicial
            children=[
                # Título con logo + texto
                html.Div(
                    id="sidebar-title",
                    className="text-xl font-semibold mb-6 whitespace-nowrap",
                    style={"display": "block"},
                    children=html.Div(
                        className="flex items-center",
                        children=[
                            html.Img(
                                src="/assets/CIHH Logo.png",  # logo en ./assets
                                className="w-8 h-8 mr-3 rounded-full",
                                alt="Logo CIHH",
                            ),
                            html.Span("CIHH"),
                        ],
                    ),
                ),

                # Menú
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

        # ==== CONTENIDO PRINCIPAL ====
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

                # Cards
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

                # Gráfica + DatePickerRange
                html.Div(
                    className="rounded-2xl bg-slate-800/70 p-4 space-y-4",
                    children=[
                        html.Div(
                            "Ejemplo de gráfica con rango de fechas",
                            className="text-sm text-slate-300",
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=df_time["date"].min().date(),
                            max_date_allowed=df_time["date"].max().date(),
                            start_date=df_time["date"].min().date(),
                            end_date=df_time["date"].max().date(),
                            display_format="YYYY-MM-DD",
                            className="cihh-datepicker",  # 👈 nuestra clase
                        ),
                        dcc.Graph(
                            id="main-graph",
                            className="h-80",
                        ),
                    ],
                ),
            ],
        ),
    ],
)

# =========================
# Callbacks
# =========================

# Sidebar expandido/colapsado
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
    # Por defecto (None o par) => EXPANDIDO
    if n_clicks is None or n_clicks % 2 == 0:
        sidebar_style = {"width": "16rem"}
        show = {"display": "inline-block"}
        title_style = {"display": "block"}
        return sidebar_style, title_style, show, show, show, show

    # Impar => COLAPSADO
    sidebar_style = {"width": "4.5rem"}
    hide = {"display": "none"}
    title_style = {"display": "none"}
    return sidebar_style, title_style, hide, hide, hide, hide


# Gráfica filtrada por rango de fechas
@app.callback(
    Output("main-graph", "figure"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
def update_main_graph(start_date, end_date):
    if start_date is None or end_date is None:
        filtered = df_time
    else:
        start = pd.to_datetime(start_date)
        end = pd.to_datetime(end_date)

        # Seguridad extra por si el usuario invierte fechas
        if start > end:
            start, end = end, start

        filtered = df_time[
            (df_time["date"] >= start) & (df_time["date"] <= end)
        ]

    fig = px.line(filtered, x="date", y="value", markers=True)
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis_title="Fecha",
        yaxis_title="Valor",
    )
    return fig


# =========================
# Run
# =========================

if __name__ == "__main__":
    app.run(debug=True)
