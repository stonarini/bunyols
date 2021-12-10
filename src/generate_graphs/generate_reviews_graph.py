import matplotlib.pyplot as plt


def generate_reviews_graph(path, total_reviews, reviews):

    plt.figure(figsize=(7.11, 3.55), facecolor="white")
    plt.rcParams["font.sans-serif"] = ["Verdana", "Dejavu Sans"]
    plt.rcParams["font.family"] = "sans-serif"

    plt.title("Reviews", fontsize=20)
    textstr = "Total Reviews: " + str(total_reviews)
    plt.text(2.7, 37, textstr, fontsize=14, color="white")
    plt.rcParams.update({"axes.facecolor": "black"})

    x = [num for num in range(len(reviews))]
    top_rev = max(reviews.values())

    plt.bar(x, reviews.values(), color="white")

    plt.xticks(x, reviews.keys(), fontsize=12)
    plt.yticks((0, top_rev), ["0", str(top_rev)], fontsize=12)
    plt.tick_params(axis=u"both", which=u"both", length=0)

    plt.savefig(path + "/reviews.svg")
    plt.close()
