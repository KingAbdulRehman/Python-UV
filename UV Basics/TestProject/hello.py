import matplotlib.pyplot as plot

def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 4, 5, 6]
    plot.plot(x, y, label="test")
    plot.show()
    plot.legend()

    print("Hello from testproject!")


if __name__ == "__main__":
    main()
