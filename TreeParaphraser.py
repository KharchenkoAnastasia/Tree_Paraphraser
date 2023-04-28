
import itertools
from nltk import ParentedTree
import copy


class TreeParaphraser:
    def __init__(self, parse_tree_str):

        self.parse_tree_str=parse_tree_str

    def generate_permutation_options(self, lists):
        # Generate all possible permutations of the elements in each input list
        permutations = [list(itertools.permutations(lst)) for lst in lists]

        # Combine the permutations of each input list into new lists
        new_lists = [list(itertools.chain(*combo)) for combo in itertools.product(*permutations)]

        # Remove duplicates from the new lists
        new_lists = list(set(map(tuple, new_lists)))

        # Convert the tuples back to lists
        new_lists = [list(t) for t in new_lists]

        return new_lists

    def swap_np_children(self, max_new_trees):
        # Convert parse tree string to NLTK ParentedTree object
        parse_tree = ParentedTree.fromstring(self.parse_tree_str)

        # Find all NP subtrees in the parse tree
        np_subtrees = list(parse_tree.subtrees(lambda t: t.label() == 'NP'))

        # Filter and save position to only include NP subtrees with multiple child NPs separated by commas or conjunction "and"
        child_nps_pos_list = []
        for np_subtree in np_subtrees:
            child_nps = [child for child in np_subtree if child.label() == 'NP']
            if len(child_nps) > 1 and (',' in np_subtree.leaves() or 'and' in np_subtree.leaves()):
                child_pos_np_subtree = []
                for child in np_subtree:
                    if child.label() == 'NP':
                        pos = child.treeposition()
                        child_pos_np_subtree.append(pos)
                child_nps_pos_list.append(child_pos_np_subtree)

        # Generate options for permuting child NPs with each other
        perm_child_np_pos_list = self.generate_permutation_options(child_nps_pos_list)

        # Replacing NP in the tree with NP from the list of options for permuting child NPs with each other
        list_new_trees = []
        num_new_trees = 0
        while num_new_trees < max_new_trees and num_new_trees< len (perm_child_np_pos_list):
            # new_tree=TreeParaphraser("")
            new_tree = copy.deepcopy(parse_tree)
            np_pos_in_perm = 0
            for child_np in child_nps_pos_list:
                for pos_np in child_np:
                    # new_subtree = ParentedTree.fromstring("({})".format(parse_tree[perm_child_np_pos_list[num_new_trees][np_pos_in_perm]]))
                    new_subtree = ParentedTree.fromstring(str(parse_tree[perm_child_np_pos_list[num_new_trees][np_pos_in_perm]]))
                    new_tree[pos_np] = new_subtree
                    np_pos_in_perm += 1
            num_new_trees += 1
            list_new_trees.append(str(new_tree))
            
        list_new_trees =[ tree.replace('\n', '')  for tree in list_new_trees]

        return list_new_trees
