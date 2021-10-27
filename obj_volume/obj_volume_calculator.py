import numpy as np

def read_obj_file(path: str):

    with open(path) as f:
    
        vertexArray = np.zeros((1,3))
        meshArray = np.zeros((1,3))

        for line in f:
            data = line.split() # white space
            
            if data[0] == "v":
                vertexArray = np.append(vertexArray , [[float(data[1]), float(data[2]), float(data[3])]], axis=0)
            
            elif data[0] == "f":
                v1 = data[1].split("//")[0]
                v2 = data[2].split("//")[0]
                v3 = data[3].split("//")[0]
                meshArray = np.append(meshArray , [[int(v1), int(v2), int(v3)]], axis=0)
            
            else:
                pass

    print("total vertex num : {}".format(np.shape(vertexArray)))
    print("total mesh num : {}".format(np.shape(meshArray)))

    return vertexArray,meshArray

def cal_volume(vertexs: np.ndarray, meshes: np.ndarray):
    total_volume = 0
    
    for mesh in meshes:
        dV = np.zeros((3,3))

        dV[:,0] = vertexs[int(mesh[0])]
        dV[:,1] = vertexs[int(mesh[1])]
        dV[:,2] = vertexs[int(mesh[2])]

        total_volume = total_volume + np.linalg.det(dV)/6
    
    print("result : {}".format(total_volume))

if __name__ == '__main__':
    vertexs, meshes = read_obj_file("./sample.obj")
    cal_volume(vertexs, meshes)