if __name__ == '__main__':
    results = []
    for a in range(2, 101):
        for b in range(2, 101):
            num = a**b
            if num not in results:
                results.append(num)
    print(len(results))
