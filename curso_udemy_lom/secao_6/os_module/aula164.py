# os + shutil - mover, copiar e apagar
# shutil.move -> mover/renomear
# os.rename -> mover/renomear
# shutil.copy -> copiar
# os.unlink -> apagar
# shutil.rmtree -> apagar diretorio recursivamente
# shutil.copytree -> copiar diretorio recursivamente
import os
import shutil

parent_dir = os.path.join(
    os.path.abspath('curso_udemy_lom'),
    'secao_6'
)

dir_dest = os.path.join(parent_dir, 'os_module', 'os_shutil')

print(parent_dir, dir_dest, sep='\n')

# os.makedirs(dir_dest, exist_ok=True)

# for root, dirs, files in os.walk(parent_dir):
#     if root == dir_dest:
#         continue

#     _, dir_ = os.path.split(root)
#     dest_path = os.path.join(dir_dest, dir_)
#     # print(dest_path)

#     for file in files:
#         file_path = os.path.join(root, file)
#         destination = file_path.replace(root, dest_path)
#         print(destination)
#         dir_, _ = os.path.split(destination)
#         os.makedirs(dir_, exist_ok=True)
#         if not os.path.exists(destination):
#             shutil.copy(file_path, destination)

# shutil.rmtree(dir_dest, ignore_errors=True)

dir_dest = parent_dir + '_os'
shutil.copytree(parent_dir, dir_dest, dirs_exist_ok=True)
shutil.rmtree(dir_dest, ignore_errors=True)

shutil.move(parent_dir, dir_dest)
shutil.move(dir_dest, parent_dir)
