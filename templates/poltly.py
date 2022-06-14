
import plotly.express as px
import numpy
 

fig = px.bar(x=kategorien, y=summierte_ausgaben)
                fig.update_layout(
                    title="Ausgaben pro Kategorie",
                    xaxis_title="Kategorien",
                    yaxis_title="Ausgaben")
                div = plot(fig, output_type="div")
                return render_template("statistik2.html", visualisierung=div)
