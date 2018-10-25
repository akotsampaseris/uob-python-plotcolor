import matplotlib.pyplot as plt

def getdata(path, *args):
    # Open the csv files to read the data
    with open(path, 'r') as csvfile:
        data = csv.DictReader(csvfile)

        for arg in args:
            print(arg)
            list = []
            for row in data:
                list.append(float(row[arg]))
            return list


def plotcolormesh(x, y, z, cmap='RdBu', title="Figure"):
    fig, ax = plt.subplots()
    cs = ax.pcolormesh(x, y, z, cmap=cmap)
    fig.colorbar(cs)
    ax.set_title(title)

    plt.show()
