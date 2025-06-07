import launch_docker

for i in range(1):
    print(str(i+1)+"-th trial")
    launch_docker.main()
