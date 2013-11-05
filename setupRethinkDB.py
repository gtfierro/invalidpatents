import rethinkdb as r

print 'Checking for expected RethinkDB database and table'

r.connect().repl()
if 'invalid' not in r.db_list().run():
    r.db_create('invalid').run()

db = r.db('invalid')
print 'DB: "invalid" created'

if 'invalid' not in db.table_list().run():
    db.table_create('invalid').run()

print 'Table: "invalid" created'
