import csv

# Read data from the text file
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Parse the data and store it in a list of lists
data = []
for line in lines[1:]:  # Skip the header line
    parts = line.strip().split('\t')
    date = parts[0]
    open_price = float(parts[1].replace(',', ''))
    high = float(parts[2].replace(',', ''))
    low = float(parts[3].replace(',', ''))
    close = float(parts[4].replace(',', ''))
    adj_close = float(parts[5].replace(',', ''))
    volume = int(parts[6].replace(',', ''))
    data.append([date, open_price, high, low, close, adj_close, volume])

# Write the data to a CSV file
with open('stock_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])  # Write header row
    writer.writerows(data)
