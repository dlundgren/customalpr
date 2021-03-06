# utility function
# load and parse data from "config.yml"

import yaml
from camera_datatype import cameraDatatype


def load_config(path="config.yml"):
    # load config file data
    print("")
    print("loading config file")

    config_file_path = path
    with open(config_file_path, 'r') as stream:
        config = yaml.load(stream)

    gui = config['GUI_toggle']
    gui_resolution_x = config['GUI_resolution_X']
    gui_resolution_y = config['GUI_resolution_Y']
    gui_resolution = (gui_resolution_x, gui_resolution_y)

    camera_list = []
    for camera in config['camera_addresses']:
        for name in camera:
            camera_id = camera[name]
            camera_name = name
            camera_url = camera_id[0]['url']
            camera_aoi = []
            for aoi in camera_id[1]['aoi']:
                for entry in aoi:
                    x = aoi[entry][0]['X']
                    y = aoi[entry][1]['Y']
                    w = aoi[entry][2]['W']
                    h = aoi[entry][3]['H']
                    temp_dict = {entry: (x, y, w, h)}
                    camera_aoi.append(temp_dict)

        camera_list.append(cameraDatatype(camera_name, camera_url, camera_aoi))

    print("config file loaded")

    return camera_list, gui, gui_resolution
