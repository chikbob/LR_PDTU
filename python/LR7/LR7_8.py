def extract_series_info(arr):
    seriesLengths = []
    seriesValues = []

    currentLength = 1
    currentValue = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == currentValue:
            currentLength += 1
        else:
            seriesLengths.append(currentLength)
            seriesValues.append(currentValue)

            currentLength = 1
            currentValue = arr[i]

    seriesLengths.append(currentLength)
    seriesValues.append(currentValue)

    return seriesLengths, seriesValues


inputMassive = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5]
lengths, values = extract_series_info(inputMassive)

print("Довжини серій:", lengths)
print("Значення серій:", values)
