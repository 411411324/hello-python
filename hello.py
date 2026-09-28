import datetime
import time


def main():
    print("Hello! I am 411411324 on GitHub.")
    print(f"Today is {datetime.date.today()}")
    print("Countdown begins:")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(0.5)
    print("Go!")


if __name__ == "__main__":
    main()
