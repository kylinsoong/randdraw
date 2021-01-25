import csv
import json

def main():
    with open("in.csv") as f:
        spamreader = csv.reader(f)
        accepted = [row[0] for row in list(filter(lambda x: x[1] == 'Yes', [row for row in spamreader]))]
        print(len(accepted))
        part = []
        for row in accepted:
            part.append({"name":row.split(" <")[0],"phone":row.split("<")[1].replace(">","")})
        x = json.dumps(part, indent=2)
        x = "var member = " + x
        with open("out.js","w") as f2:
            f2.write(x)

if __name__ == "__main__":
    main()