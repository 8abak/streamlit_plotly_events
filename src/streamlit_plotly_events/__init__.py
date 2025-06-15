
import streamlit.components.v1 as components

def live_append_chart(chart_data, override_height=600):
    return components.html(
        f"""
        <div id="plot"></div>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <script>
        let data = {chart_data};
        let layout = {{
            margin: {{ t: 40 }},
            xaxis: {{ rangeslider: {{ visible: true }} }},
            yaxis: {{ fixedrange: false }},
            template: "plotly_dark"
        }};
        Plotly.newPlot("plot", data, layout);

        const addNewPoint = () => {{
            fetch("/new-tick")
                .then(resp => resp.json())
                .then(tick => {{
                    if (!tick) return;
                    Plotly.extendTraces("plot", {{
                        x: [[tick.timestamp]],
                        y: [[tick.price]]
                    }}, [0]);
                }});
        }};
        setInterval(addNewPoint, 2000);
        </script>
        """,
        height=override_height
    )
