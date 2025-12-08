"""Enterprise pipeline example."""
from d10z.sdk.client import D10ZClient


def run():
    client = D10ZClient(endpoint="https://enterprise.example.com")
    result = client.run_validation()
    print(result)


if __name__ == "__main__":
    run()
