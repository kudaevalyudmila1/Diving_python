from pathlib import Path


def rename_file(new_name_file, num, extension, extension_new, old_name):
    p = Path(Path().cwd())
    i = 0
    for obj in p.iterdir():
        if obj.is_file():
            if obj.name.split('.')[-1] == extension:
                Path(obj).rename(f'{new_name_file}_{obj.name.split(".")[0][old_name[0]:old_name[1]]}{str(i).zfill(num)}.{extension_new}')
                i += 1
               
      
if __name__ == '__main__':
    rename_file("res_name", 3, "doc", "txt", [0,2])