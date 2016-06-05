import couchdb

couch = couchdb.Server()
db = couch['workouts']

divider = '-------------------------------------------'
post = 'post'

for id in db:
    if id[0] == '_':
        continue3
    doc =  db[id]
    date =  doc['Date']
    print date
    work = doc['Workout']
    find = work.lower().find(post)
    if find > 0:
        print find
        print work[:find-1]
    else:
        print work
    print divider
