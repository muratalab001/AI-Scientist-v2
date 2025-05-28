import launch_docker

for i in range(2):
    print(str(i+1)+"-th trial")
    launch_docker.main()
