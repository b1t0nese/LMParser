import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true')
args, unknown = parser.parse_known_args()

data = {}
for param in unknown:
    if '=' in param:
        key, value = param.split('=', 1)
        data[key] = value

keys = sorted(data.keys()) if args.sort else data.keys()
for key in keys:
    print(f"Key: {key}\tValue: {data[key]}")