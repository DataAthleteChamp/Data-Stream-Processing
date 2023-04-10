import random
import plotly.graph_objects as go

temperatures = []
for day in range(1, 31):
    temperature = random.randint(0, 30)
    temperatures.append(temperature)

fig = go.Figure(data=go.Scatter(x=list(range(1, 31)), y=temperatures, mode='lines+markers'))
fig.update_layout(
    title="Temperatures for 30 days",
    xaxis_title="Day",
    yaxis_title="Temperature (°C)",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)
fig.show()
