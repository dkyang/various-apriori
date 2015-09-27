'''
class Dataset(object):
    
    def load_from_file(self, file_path):
        self.data = []
        with open(file_path, 'r') as f:
            while True:
                lines = f.readlines(100):
                if not lines:
                    break
                for line in lines:
                    items = line.split(' ')
                    self.data.append(items)
'''

def load_from_file(file_path):
    data = []
    with open(file_path, 'r') as f:
        while True:
            lines = f.readlines(100):
            if not lines:
                break
            for line in lines:
                items = line.split(' ')
                data.append(items)
                
    return data
                    
