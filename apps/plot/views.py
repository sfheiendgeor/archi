from django.views.generic import TemplateView
import plotly.graph_objects as go
from django.shortcuts import render
import pandas as pd

def index(request):
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                        open=df['AAPL.Open'],
                                        high=df['AAPL.High'],
                                        low=df['AAPL.Low'],
                                        close=df['AAPL.Close'])])

    plot_fig = fig.to_html(fig, include_plotlyjs=False)
    return render(request, "plot/plot.html", {
        "graph": plot_fig
    })