from datasets import load_dataset, Image
from tqdm import tqdm
import os


def main():
    dataset = load_dataset('pykale/bln600-img-patch')
    os.makedirs('data/patch', exist_ok=True)

    for split in dataset.values():
        split = split.cast_column('image', Image(decode=False))
        for row in tqdm(split):
            with open(os.path.join('data/patch', row['Image Patch']), 'wb') as f:
                f.write(row['image']['bytes'])


if __name__ == '__main__':
    main()