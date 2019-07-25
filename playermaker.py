def get_stats(*args):
    result = dict()
    for num_session, session in enumerate(args):
        for player in session:
            if player in result:
                result[player].append("session {}".format(num_session + 1))
            else:
                result[player] = ["session {}".format(num_session + 1)]
    return result


s1 = ["Mbappe", "Griezman", "Pogba", "Giroud", "Pavard", "Lloris", "Dembele", "Fekir", "Hernandez", "Kante"]
s2 = ["Mbappe", "Griezman", "Pogba", "Matuidi", "Pavard", "Lloris", "Dembele", "Fekir", "Hernandez", "Umtiti"]
s3 = ["Thuram", "Zidane", "Rami", "Matuidi", "Pavard", "Lloris", "Dembele", "Fekir", "Hernandez", "Umtiti"]
s4 = ["Ronaldo", "Benzema", "Neymar", "Countinho", "Pavard", "Lloris", "Dembele", "Firmino", "Hernandez", "Umtiti"]
s5 = ["Ronaldo", "Benzema", "Pogba", "Giroud", "Pavard", "Neymar", "Dembele", "Firmino", "Hernandez", "Umtiti"]

print(get_stats(s1, s2, s3, s4, s5))
