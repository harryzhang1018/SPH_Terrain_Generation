import bpy

def write_verts():
    obj = bpy.context.object

    if obj is None or obj.type != "MESH":
        return

    # Output geometry
    obj_eval = obj.evaluated_get(bpy.context.view_layer.depsgraph)
    filepath = "/home/harry/dense_blayer_4.csv"
    
    with open(filepath, "w") as file:
        # Write the header, pos x | pos y | pos z
        file.write("pos x,pos y,pos z\n")

        for v in obj_eval.data.vertices:
            # ":.3f" means to use 3 fixed digits after the decimal point.
            file.write(f",".join(f"{c:.3f}" for c in v.co) + "\n")

if __name__ == "__main__":
    write_verts()