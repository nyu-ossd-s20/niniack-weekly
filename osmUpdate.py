import osmapi
api = osmapi.OsmApi()
data = api.ChangesetsGet(username='niniack')
changesetIDs = list(data)

# print(changesetIDs)

for i in range(len(changesetIDs)):
    with open('contributions.md','a+') as f:
        if (str(changesetIDs[i]) not in f.read()):

            id = changesetIDs[i]

            f.write('| {} |\
            https://www.openstreetmap.org/changeset/{} | \
                    OpenStreetMap | \
                    {} |\n\
                    '.format(data[id]['created_at'].strftime('%b %d'),
                             data[id]['id'],
                             data[id]['tag']['comment']
                             ))
