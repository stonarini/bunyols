import matplotlib.pyplot as plt


def generate_price_graph(path, dates, prices):

    plt.figure(figsize=(7.11, 3.55), facecolor="white")
    plt.rcParams["font.sans-serif"] = ["Verdana", "Dejavu Sans"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams.update({"axes.facecolor": "black"})

    plt.plot(dates, prices, linewidth=3, color="white")

    tick_dates = []
    current_year = ""
    for date in dates:
        if date[:4] == current_year:
            tick_dates.append(date[5:10])
        else:
            current_year = date[:4]
            tick_dates.append(date[:10])

    price_min = lambda x: str(round(float(min(x)[1:])))
    price_max = lambda x: str(round(float(max(x)[1:])))

    plt.xticks(dates, tick_dates, fontsize=12)
    plt.yticks(
        (0, len(prices) - 1),
        ["$" + price_min(prices), "$" + price_max(prices)],
        fontsize=12,
    )
    plt.tick_params(axis=u"both", which=u"both", length=0)

    plt.title("Prices", fontsize=20)
    plt.savefig(path + "/price.svg")
