def parse_record(line):
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Неверное количество полей")

    city, temp, date = parts

    city = city.strip()
    temp = temp.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("Город или дата не указаны")

    try:
        temp = float(temp)
    except ValueError:
        raise ValueError("Некорректная температура")

    return {
        "city": city,
        "temperature": temp,
        "date": date
    }


def read_valid(lines):
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
            records.append(record)
        except ValueError:
            continue

    return records


def average_by_city(records):
    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temp = record["temperature"]

        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1

    averages = {}

    for city in total:
        averages[city] = total[city] / count[city]

    return averages



def warmest_city(records):
    if not records:
        return None

    total = {}
    count = {}

    for record in records:
        city = record["city"]
        temp = record["temperature"]

        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1

    averages = {}

    for city in total:
        averages[city] = total[city] / count[city]

    return max(averages, key=averages.get)
