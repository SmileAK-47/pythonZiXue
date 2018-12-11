'''
unprinted_designs = ['iphone cas','robot pendant','dodecahedron']
completed_models = []

while unprinted_designs:
    current_dision = unprinted_designs.pop()

    print("model："+ current_dision)
    completed_models.append(current_dision)
print("-----")
for a in completed_models:
    print(a)

'''
def print_models(unprinted_desions,conmpleted_models):
    while unprinted_desions:
        current_design = unprinted_desions.pop()
        print("moder : "+current_design)
        conmpleted_models.append(current_design)

def show_completed(completed_models):
    print("The followingmodels have been printd:")
    for i in completed_models:
        print(i)
unprinted_designs = ['iphone cas','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed(completed_models)

print(unprinted_designs)