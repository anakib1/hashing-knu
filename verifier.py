if __name__ == '__main__':
    false_positives = 0
    false_negatives = 0
    with open('reference.txt', 'r') as reference:
        with open('C:\\Users\\bsvja\\CLionProjects\\algolab1\\output.txt', 'r') as w:
            reference_lines = reference.readlines()
            output = w.readlines()

            if len(reference_lines) != len(output):
                print(len(reference_lines), len(output))
                print("Error! Length of reference and output don't match")
                exit(1)
            total = len(reference_lines)
            for i, (ref, out) in enumerate(zip(reference_lines, output)):
                if ref != out:
                    print(f"Error! Line {i} don't match")
                    if ref == 'yes':
                        false_negatives += 1
                    else:
                        false_positives += 1

    if false_positives + false_negatives == 0:
        print('Correct.')
    else:
        print(f'Incorrect. {false_negatives} out of {total} false negatives and {false_positives} out of {total} false positives.')
