list_of_tuples = [
    ('Russia', '25'),
    ('France', '132'),
    ('Germany', '132'),
    ('Spain', '178'),
    ('Italy', '162'),
    ('Portugal', '17'),
    ('Finland', '3'),
    ('Hungary', '2'),
    ('The Netherlands', '28'),
    ('The USA', '610'),
    ('The United Kingdom', '95'),
    ('China', '83'),
    ('Iran', '76'),
    ('Turkey', '65'),
    ('Belgium', '34'),
    ('Canada', '28'),
    ('Switzerland', '26'),
    ('Brazil', '25'),
    ('Austria', '14'),
    ('Israel', '12')
]

def list_to_dict():
    res = {country: int(number) for country, number in list_of_tuples}
    sorted_by_name = sorted(res.items(), key=lambda item: item[0])
    sorted_countries = sorted(sorted_by_name, key=lambda item: item[1], reverse=True)
    for country in sorted_countries:
        print(country[0])

if __name__ == "__main__":
    list_to_dict()
