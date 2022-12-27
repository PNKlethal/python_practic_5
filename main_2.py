
def calc_lines_words(file_path):
    result = dict()
    line_num = 0
    try:
        with open(file_path, 'r') as f:
            for line_num, fl in enumerate(f, 1):
                result[line_num] = len(fl.split())
    except Exception as err:
        print(err)
    return line_num, result


if __name__ == '__main__':
    num, counts = calc_lines_words('text_2.txt')
    print(f'Found {num} line(s)')
    for k, v in counts.items():
        print(f'Line {k}: {v} word(s)')
