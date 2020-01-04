from dataloaders.datasets import xor
from torch.utils.data import DataLoader

def make_data_loader(args, **kwargs):
        
	if args.dataset == 'xor':
		train_dataset, test_dataset = xor.XOR(), xor.XOR(split='test')
		num_classes = 1
		train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, **kwargs)
		test_loader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False, **kwargs)
		return train_loader, test_loader, test_loader, num_classes
	else:
		print("Dataloader for {} is not implemented".format(args.dataset))
		raise NotImplementedError
