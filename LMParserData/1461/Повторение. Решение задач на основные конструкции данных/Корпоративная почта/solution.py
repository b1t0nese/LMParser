boxes = [input() for _ in range(int(input()))]
for new_box in [input() for _ in range(int(input()))]:
    repeat_boxes = list(map(lambda x: x.split("@")[0], filter(lambda x: x.startswith(new_box), boxes)))
    repeat_boxes_numbers = list(map(lambda x: int(x) if x.isdigit() else 0,
                                    [s[len(s.rstrip('0123456789')):] for s in repeat_boxes]))
    box_number = max(repeat_boxes_numbers) + 1 if repeat_boxes_numbers else ""
    boxes.append(f"{new_box}{box_number}@untitled.py")
    print(boxes[-1])