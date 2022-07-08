"""
File of util functions for loading datasets of MoleculeNet from dgllife
"""
import argparse
from functools import partial
import numpy as np
import torch
import torch.nn as nn

from functools import partial
from dgllife.utils import *
import multiprocessing
# from yaml import load

from pdb import set_trace

def load_MolDataset(args, path):
    '''
    Loading and preprocessing datasets from moleculeNet, then saving them
    in the specified path. (same path as in model_manager.py)

    Following has different methods for featurizing
    https://github.com/awslabs/dgl-lifesci/blob/master/docs/source/api/utils.mols.rst
    '''

    # FIXME: test with different pre-processing method
    atom_featurizer = None
    bond_featurizer = None
    num_wrokers = multiprocessing.cpu_count() if args.num_workers == -1 else args.num_workers    
    if args.dataset == 'MUV':
        from dgllife.data import MUV

        dataset = MUV(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                      node_featurizer=atom_featurizer,
                      edge_featurizer=bond_featurizer,
                      n_jobs= num_wrokers,
                      cache_file_path = path,
                      load = True
                      )

    elif args.dataset == 'BACE':
        from dgllife.data import BACE
    
        dataset = BACE(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                       node_featurizer=atom_featurizer,
                       edge_featurizer=bond_featurizer,
                       n_jobs= num_wrokers,
                       cache_file_path = path,
                       load = True
                       )
        
    elif args.dataset == 'BBBP':
        from dgllife.data import BBBP

        dataset = BBBP(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                       node_featurizer=atom_featurizer,
                       edge_featurizer=bond_featurizer,
                       n_jobs= num_wrokers,
                       cache_file_path = path,
                       load = True
                       )

    elif args.dataset == 'ClinTox':
        from dgllife.data import ClinTox

        dataset = ClinTox(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                          node_featurizer=atom_featurizer,
                          edge_featurizer=bond_featurizer,
                          n_jobs= num_wrokers,
                          cache_file_path = path,
                          load = True
                          )
    elif args.dataset == 'SIDER':
        from dgllife.data import SIDER

        dataset = SIDER(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                        node_featurizer=atom_featurizer,
                        edge_featurizer=bond_featurizer,
                        n_jobs= num_wrokers,
                        cache_file_path = path,
                        load = True
                        )
    elif args.dataset == 'ToxCast':
        from dgllife.data import ToxCast

        dataset = ToxCast(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                          node_featurizer=atom_featurizer,
                          edge_featurizer=bond_featurizer,
                          n_jobs= num_wrokers,
                          cache_file_path = path,
                          load = True
                          )
    elif args.dataset == 'HIV':
        from dgllife.data import HIV

        dataset = HIV(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                      node_featurizer=atom_featurizer,
                      edge_featurizer=bond_featurizer,
                      n_jobs= num_wrokers,
                      cache_file_path = path,
                      load = True
                      )
    elif args.dataset == 'PCBA':
        from dgllife.data import PCBA

        dataset = PCBA(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                       node_featurizer=atom_featurizer,
                       edge_featurizer=bond_featurizer,
                       n_jobs= num_wrokers,
                       cache_file_path = path,
                       load = True
                       )
    elif args.dataset == 'Tox21':
        from dgllife.data import Tox21

        dataset = Tox21(smiles_to_graph=partial(smiles_to_bigraph, add_self_loop=True),
                        node_featurizer=atom_featurizer,
                        edge_featurizer=bond_featurizer,
                        n_jobs= num_wrokers,
                        cache_file_path = path,
                        load = True
                        )
    else:
        raise ValueError('Unexpected dataset: {}'.format(args.dataset))

    return dataset

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Test')
#     parser.add_argument('-d', '--dataset', type=str, default='None')
#     parser.add_argument('-n', '--num_workers', type=int, default=1, help="number of processors used for processing data. default 1, -1 uses all cpu cores")
#     args = parser.parse_args()
#     dataset = load_MolDataset(args=args, path="test.bin") 
#     set_trace()