
import plotly.express as px
import pandas as pd
import plotly


fig = px.bar(x=kategorien, y=summierte_ausgaben)
                fig.update_layout(
                    title="Ausgaben pro Kategorie",
                    xaxis_title="Kategorien",
                    yaxis_title="Ausgaben")
                div = plot(fig, output_type="div")
                print(div)
