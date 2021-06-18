#filename, title, categories, year, technique_english, technique_portuguese, size_of_painting, statement
#filename, title, categories, year, desc1, desc2, desc3, desc4
import csv

with open('paulinapinsky.tsv') as csvfile:
    database = csv.reader(csvfile, delimiter='\t')
    for row in database:
        f = open('../content/blog/' + row[0] + '.md','w+')
        f.write('+++\r\n' )
        f.write('title="' + row[1] + '"\r\n' )
        f.write('image="/blog/' + row[0] + '.jpeg' + '"\r\n' )
        f.write('categories=[' + ', '.join('"{0}"'.format(w) for w in row[2].split(',')) + ']\r\n' )
        f.write('tags=[' + ', '.join('"{0}"'.format(w) for w in row[3].split(',')) + ']\r\n' )
        f.write('year="' + ','.join(row[3].split(',')) + '"\r\n')
        f.write('technique_english="' + row[4] + '"\r\n')
        f.write('technique_portuguese="' + row[5] + '"\r\n')
        f.write('size_of_painting="' + row[6] + '"\r\n')
        try:
            f.write('statement="' + row[7] + '\r\n' + row[8] + '"\r\n')
        except:
            f.write('statement="' + row[7] + '"\r\n')
        f.write('+++\r\n')
        f.close()