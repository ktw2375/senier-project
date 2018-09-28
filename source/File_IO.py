import pickle



def read_review(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line for line in f.read().split('\n')]
    return data

def read_train_data(filename):
  with open(filename, 'r', encoding='utf-8') as f:
     data = [line.split(' ') for line in f.read().splitlines()]
  return data

def read_data3(filename):
  with open(filename, 'r', encoding='utf-8') as f:
     data = [line.split('@') for line in f.read().splitlines()]
  return data

def write_pickle(data,name):
    with open(name, 'wb') as f:

        pickle.dump(data, f)
def read_pickle(name):
    with open(name, 'rb') as f:

        data = pickle.load(f)  # 단 한줄씩 읽어옴
    return data