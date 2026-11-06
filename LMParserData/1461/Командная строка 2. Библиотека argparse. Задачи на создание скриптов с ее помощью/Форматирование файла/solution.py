import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
        new_text = []
        for line in lines:
            line = line.rstrip('\n')
            while len(line) > frame_width:
                new_text.append(line[:frame_width])
                line = line[frame_width:]
                if len(new_text) >= frame_height:
                    break
            new_text.append(line)
            if len(new_text) >= frame_height:
                break
        return "\n".join(new_text[:frame_height])
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', type=int, default=10)
    parser.add_argument('--frame-width', type=int, default=30)
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.filename))