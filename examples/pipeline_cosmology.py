from d10z.sdk.client import D10ZClient

if __name__ == "__main__":
    client = D10ZClient.default()
    result = client.run_rotation_curve_demo()
    print("Demo cosmológica (skeleton):")
    print(result)
