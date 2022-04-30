import argparse
import collections
from pathlib import Path
from PIL import Image
import numpy as np
import itertools
import glob


parser = argparse.ArgumentParser(description='Smash together images that have Alpha')
parser.add_argument('--root-object', type=str,
                    help='Base Image group name to Add To', required=True)
parser.add_argument('--groups', dest='groups', nargs='+',
                    help='Names of files to combine (expects name+#)',required=True)

args = parser.parse_args()



groups = args.groups
group_images = {}
root_images = glob.glob(args.root_object + "*")
permutes = root_images
for group in groups:
    group_images[group] = glob.glob(group + "*")
    permutes = itertools.product(permutes, group_images[group])
recipes = []
for permute in permutes:
    recipes.append(list(itertools.chain(*permute[:-1])) + [list(permute)[-1]])
    # There is definitely a better way to do this but I have to pee.
#print(recipes)
issuance = 0    
for recipe in recipes:
    issuance = issuance + 1
    with Image.open(recipe[0]) as im:
        for element in recipe[1:]:
            with Image.open(element) as compositor:
                im.alpha_composite(compositor)
        im.save("./"+args.root_object+"_nft_"+str(issuance) + ".png")
