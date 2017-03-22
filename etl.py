import cPickle as pkl
import glob
import json

def json2numpy():
	'''
	Takes the bbox labels and saves a dict which contains the image number (unique) and corresponding bboxes list
	'''
	files = glob.glob("bbox_labels/*")
	bbox_dict = {}
	lista = []
	for f in files:
		species = json.load(open(f))
		for each_img in species:
			filepath = str(each_img['filename'])
			filename = str(filepath.split('/')[-1].split('.')[0])
			lista.append(filename)
			bbox = []
			annotations = each_img['annotations']
			for each_annotation in annotations:
				x = int(each_annotation['x'])
				y = int(each_annotation['y'])
				height = int(each_annotation['height'])
				width = int(each_annotation['width'])
				bbox.append([x,y,width,height])

			bbox_dict[filename] = bbox

	pkl.dump(bbox_dict,open("bbox_dict.pkl",'w'))

def path_bbox_pairs():
	'''
	1. Takes the previous dict and saves another dict with full path as key and the same bbox as value
	2. This has the information of which class it belongs as well as the whole path
	3. The exception is for NoF class
	'''
	
	allfiles = glob.glob("/home/pdguest/Datasets/NCFM/train/*/*.jpg")
	bbox_dict = pkl.load(open("bbox_dict.pkl"))
	usable_bbox_dict = {}
	for f in allfiles:
		filenumber = f.split('/')[-1].split('.')[0]
		try:
			usable_bbox_dict[f] = bbox_dict[filenumber]
		except KeyError:
			print f, "error"
			continue
		

	pkl.dump(usable_bbox_dict,open("usable_bbox_dict.pkl",'w'))