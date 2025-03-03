import matplotlib
import matplotlib.pyplot as plt
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

def main(page: ft.Page):
    fig, ax = plt.subplots()

    fruits = ["maçã", "mirtilio", "cereja", "laranja"]
    counts = [40, 100, 30, 55]
    bar_labels = ["vermelho", "azul", "_vermelho", "laranja"]
    bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
    
    ax.set_ylabel("Suprimento de frutas")
    ax.set_title("Fornecimento de frutas por tipo e cor")
    ax.legend(title="Cor da Fruta")

    chart = MatplotlibChart(
        figure=fig,
        isolated=True,
        original_size=False,
        transparent=True,
    )

    page.add(chart)
    

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')