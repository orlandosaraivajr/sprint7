import os
import sys
import platform

if sys.platform == 'linux':
    print(os.getcwd())
    os.chdir('/tmp')
    print(os.getcwd())  

    with open('teste.txt', 'w') as f:
        f.write('oi mundo')


    os.listdir()
    os.listdir('mintUpdate')

    os.mkdir('Napp')
    os.mkdir('Napp/auditoria')
    os.chdir('/tmp/Napp/auditoria')
    for num in range(1,10):
        os.system('touch arquivo' + str(num) + '.txt')


    # os.rename('teste.txt','teste_new.txt')

    # os.remove('teste.txt')
    # os.rmdir('napp')

    # import shutil
    # shutil.rmtree('napp')

    walk = os.walk('/tmp')  
    print(next(walk))


    def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)


    find('arquivo1.txt', '/tmp') 
    find('*.txt', '/tmp')

    import glob
    def find(name, path):
        old_path = os.getcwd()
        os.chdir(path)
        looking_for = '**/' + name
        matched = glob.glob(looking_for, recursive=True)
        os.chdir(old_path)
        return matched
        
    find('arquivo1.txt', '/tmp') 
    find('*.txt', '/tmp')


print(os.environ)
os.environ.get('PATH')
print(os.name)
print(platform.system())
print(platform.release())
print(platform.version())




