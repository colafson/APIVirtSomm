# goal for this is to save our tree to a file
import pickle

header = []
virt_somm_tree = []

packaged_objest = [header, virt_somm_tree]
#pickle packaged output to a file tree.p
outfile = open("tree.p", "wb")
pickle.dump(packaged_object, outfile)
outfile.close()
