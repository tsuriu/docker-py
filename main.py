import docker
import os
import csv
from html_gen import generate_html

dockerClient = docker.from_env()

header = ["Id", "Name", "State", "Docker Compose", "Image", "Volumes", "Volume Size(Mib)"]
data = []

def calculate_files_size(path):
        size = 0
        for path, _, files in os.walk(path):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
        return "{:.2f}".format(size / (1024 ^2))

def get_data():
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    for container in dockerClient.containers.list():
        selected_container = client.inspect_container(container.id)
        docker_compose_dir = selected_container['Config']['Labels']["com.docker.compose.project.working_dir"]
        if os.getcwd() in docker_compose_dir:
            id          = selected_container["Id"]
            name        = selected_container["Name"][1:]
            state       = selected_container["State"]["Status"]
            config      = selected_container['Config'] #ignore
            image       = config["Image"]
            volume      = []
            volume_size = []
            
            for vol in selected_container["Mounts"]:
                volume.append([
                    vol["Source"],
                    vol["Destination"]
                ])
                volume_size.append(calculate_files_size(vol["Source"]))
            
            #Dir + file
            docker_compose = config['Labels']["com.docker.compose.project.working_dir"] + "/" + config['Labels']["com.docker.compose.project.config_files"]
            data.append([id, name, state, docker_compose, image, volume, volume_size])

    # Sort by directory
    new_data = sorted(data, key=lambda x: x[3])
    create_csv(new_data)
    generate_html(new_data)

def create_csv(container_data):
    with open(os.getcwd() + "/docker_list.csv", "w") as list_file:
        docker_file = csv.writer(list_file)
        docker_file.writerow(header)
        docker_file.writerows(container_data)

get_data()