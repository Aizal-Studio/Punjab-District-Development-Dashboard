import matplotlib.pyplot as plt


def create_development_chart(selected):

    district = selected["District"]
    score = selected["DevelopmentScore"]

    plt.figure(figsize=(6,4))

    plt.bar(
        [district],
        [score]
    )

    plt.ylabel("Development Score")
    plt.title("District Development Score")

    file = f"reports/charts/{district}_development.png"

    plt.savefig(
        file,
        bbox_inches="tight"
    )

    plt.close()

    return file



def create_indicator_chart(selected):

    labels = [
        "Literacy",
        "Hospitals",
        "Schools"
    ]

    values = [
        selected["LiteracyRate"],
        selected["Hospitals"],
        selected["TotalSchools"]
    ]

    plt.figure(figsize=(7,4))

    plt.bar(
        labels,
        values
    )

    plt.title(
        f"{selected['District']} Indicators"
    )

    file = f"reports/charts/{selected['District']}_indicators.png"

    plt.savefig(
        file,
        bbox_inches="tight"
    )

    plt.close()

    return file