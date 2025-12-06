"""Run lightweight stress simulations for the D10Z models."""
import time


def main():
    start = time.time()
    iterations = 10000
    total = 0
    for i in range(iterations):
        total += (i % 7) * 0.01
    duration = time.time() - start
    print(f"Executed {iterations} iterations in {duration:.3f}s (total={total:.2f})")


if __name__ == "__main__":
    main()
