import camelot
tables = camelot.read_pdf(r'source.pdf', pages='2')
print(tables)

tables.export('foo.xlsx', f='excel') # json, excel, html, sqlite

