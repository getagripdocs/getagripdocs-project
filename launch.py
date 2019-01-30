
def launch():
    from time import sleep

    import os 
    os.popen("mkdocs build")

    # now copy /site to ../getagripdocs

    # and commit+push both repos
    # using dulwich porcelain



if __name__ == "__main__":
    launch()