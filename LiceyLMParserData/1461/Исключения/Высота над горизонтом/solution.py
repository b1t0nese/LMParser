import math

try:
    parts = list(map(int, input().split()))
    if len(parts) != 2:
        raise ValueError(f"not enough values to unpack (expected 2, got {len(parts)})")
    angle = math.degrees(math.atan2(*parts))
    if parts[0] < 0 or parts[1] < 0 or angle < 0:
        print("Negative sun height.")
    else:
        print(round(angle))
except ValueError as e:
    print(f"Wrong input data: {e}")