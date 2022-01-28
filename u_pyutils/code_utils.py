from .low_level import collect_exist_files

def code_count_lines(folder, suffix='.py', encoding='utf'):
    fp = collect_exist_files(folder, suffix=suffix)
    counter = 0
    for i in fp:
        try:
            with open(i, mode='r', encoding=encoding) as f:
                code = f.read()
            counter += len(code.split('\n'))
        except:
            print(i.name)
    return '{: >5d} lines in {: >3d} files'.format(counter, len(fp))