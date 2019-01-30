def do_git(command, cwd):
    import subprocess
    cmd = [command.split(" ")]
    p = subprocess.Popen(cmd, cwd=cwd)
    p.wait()

def launch():
    from time import sleep

    import os 
    #os.popen("mkdocs build")

    cwd = os.getcwd()
    temp_folder = "/".join(cwd.split("\\")[:-2]) + "/temp"

    import shutil
    shutil.rmtree(temp_folder)
    #os.mkdir(temp_folder)
    shutil.copytree("site", temp_folder)

    from dulwich import porcelain

    #git_lines_1 = [
    #    "git checkout gh-pages"
    #]

    #git_lines_2 = [
    #    "git commit -m '.'",
    #    "git push -u origin gh-pages",
    #    "git checkout -b master"
    #]

    #for gl in git_lines_1:
    #    do_git(gl, cwd)


    #shutil.rmtree(".")
    #shutil.copytree(temp_folder+"/temp", ".")

    #for gl in git_lines_2:
    #    do_git(gl, cwd)



if __name__ == "__main__":
    launch()