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

def cal_crossing_distance(ray: np.array, vertexs: np.array, meshes: np.array):
   
    for mesh in meshes:
        edge1 = np.zeros((1,3))
        edge1 = vertexs[int(mesh[1])] - vertexs[int(mesh[0])]
        
        edge2 = np.zeros((1,3))
        edge2 = vertexs[int(mesh[2])] - vertexs[int(mesh[0])]

        r_offset = ray[0,:] - vertexs[int(mesh[0])]

        A = np.linalg.det(np.array([edge1, ray[1,:], edge2]))
        deltaE = 1e-6 #Möller97

        #if((A > -deltaE) and (A < deltaE)): #裏表両方を判定する場合
        if((A < deltaE)): #表のみの場合
            pass #rayとメッシュが平行 or 裏側で交差

        else:
            u = np.linalg.det(np.array([ray[1,:], edge2, r_offset])) / A

            if((u >= 0) and (u <= 1)):
                v = np.linalg.det(np.array([ray[1,:], r_offset, edge1])) / A
                
                if((v >= 0) and (v <= 1)):
                    t = np.linalg.det(np.array([edge2, r_offset, edge1])) / A
                
                    if(t >= 0):
                        print("Intersection coordinates : {}".format(ray[0,:]+ray[1,:]*t))
                        print("distance : {}".format(t))

if __name__ == '__main__':
    test_ray = np.array([[0,0.01,0.01],[1,0,0]]) #(start point , direction)
    vertexArray, meshArray = read_obj_file("sample.obj")
    cal_crossing_distance(test_ray, vertexArray, meshArray)
