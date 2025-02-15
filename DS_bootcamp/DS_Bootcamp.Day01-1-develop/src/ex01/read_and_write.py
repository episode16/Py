def rewrite():
    with open('ds.csv', 'r') as f:
        data = f.readlines()
    with open ('ds.tsv', 'w') as f_res:
        for line in data:
            res_lines = line.replace(',', '\t')
            f_res.write(res_lines)

if __name__ == '__main__':
    rewrite()