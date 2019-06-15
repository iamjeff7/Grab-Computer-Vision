import scipy.io as sio
import pandas as pd

def read_file(filename):
    matfile = sio.loadmat(filename)
    return matfile


def print_annotation(matfile):
    annos = matfile['annotations'][0]
    size = annos.shape[0]
    print('Size:',size,'\n')

    label = []
    filename = []
    
    for i in annos:
        for j in range(len(i)):
            if j == len(i)-1:
                #print(i[j][0],end=' ')
                name = i[j][0]
                fname = name.split('.')[0]
                file_extension = name.split('.')[1]
                new_name = str(int(fname)-1)
                full_name = new_name+'.'+file_extension
                filename.append(full_name)
            elif j == len(i)-2:
                #print(i[j][0][0],end=' ')
                label.append(int(i[j][0][0])-1)
    df = pd.DataFrame({'filename':filename, 'label':label})
    print(df)

def main():
    mat_file = read_file('cars_train_annos.mat')
    print_annotation(mat_file)

    #mat_file = read_file('cars_meta.mat')
    #print(mat_file)

if __name__ == "__main__":
    print()
    main()
