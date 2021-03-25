import os
import platform
import sys
import argparse
import shutil

def create_sdf(author_name, author_email, description, world_name):

    #--------------------create model.config file--------------------
    f = open("../worlds/" + world_name + "/model.config", "w+")
    f.write("<?xml version=\"1.0\"?>\n\
\n\
<model>\n\
  <name>"+str(world_name)+"</name>\n\
  <version>1.0</version>\n\
  <sdf version=\"1.5\">model.sdf</sdf>\n\
\n\
  <author>\n\
    <name>" + str(author_name) + "</name>\n\
    <email>" + str(author_email) + "</email>\n\
  </author>\n\
\n\
  <description>\n\
    " + str(description) + "\n\
  </description>\n\
</model>\n\
\n")
    f.close()
    print("../worlds/" + world_name + "model.config" + " created")
    return

def create_config(world_name, world_length_m, world_height_m):
    f = open("../worlds/" + world_name + "/model.sdf", "w+")

    f.write("<?xml version=\"1.0\" ?>\n\
<sdf version=\"1.5\">\n\
    <model name=\"heightmap\">\n\
      <static>true</static>\n\
      <link name=\"link\">\n\
        <collision name=\"collision\">\n\
          <geometry>\n\
            <heightmap>\n\
              <uri>model://" + str(world_name) + "/media/materials/texture/random_world.png</uri>\n\
              <size>" + str(world_length_m) + " " +\
               str(world_length_m) + " " +\
               str(world_height_m) + "</size>\n\
              <pos>0 0 0</pos>\n\
            </heightmap>\n\
          </geometry>\n\
        </collision>\n\
        <visual name=\"visual_abcedf\">\n\
          <geometry>\n\
            <heightmap>\n\
              <use_terrain_paging>false</use_terrain_paging>\n\
              <texture>\n\
                <diffuse>file://media/materials/textures/dirt_diffusespecular.png</diffuse>\n\
                <normal>file://media/materials/textures/flat_normal.png</normal>\n\
                <size>1</size>\n\
              </texture>\n\
              <texture>\n\
                <diffuse>file://media/materials/textures/grass_diffusespecular.png</diffuse>\n\
                <normal>file://media/materials/textures/flat_normal.png</normal>\n\
                <size>1</size>\n\
              </texture>\n\
              <texture>\n\
                <diffuse>file://media/materials/textures/fungus_diffusespecular.png</diffuse>\n\
                <normal>file://media/materials/textures/flat_normal.png</normal>\n\
                <size>1</size>\n\
              </texture>\n\
              <blend>\n\
                <min_height>0.1</min_height>\n\
                <fade_dist>1</fade_dist>\n\
              </blend>\n\
              <blend>\n\
                <min_height>0.1</min_height>\n\
                <fade_dist>1</fade_dist>\n\
              </blend>\n\
              <uri>model://" + str(world_name) + "/media/materials/texture/random_world.png</uri>\n\
              <size>" + str(world_length_m) + " " +\
               str(world_length_m) + " " +\
               str(world_height_m) + "</size>\n\
              <pos>0 0 0</pos>\n\
            </heightmap>\n\
          </geometry>\n\
        </visual>\n\
      </link>\n\
    </model>\n\
</sdf>\n\
\n")
    f.close()
    print("../worlds/" + world_name + "model.sdf" + " created")

def create_map(world_name, world_length_m, world_height_m):
    #TODO: Read from terminal?
    author_name = "Martin Nievas"
    author_email = "mnievas@frc.utn.edu.ar"
    default_description = "Random world"

    # ----------Generate tag material script----------
    try:
        os.makedirs("../worlds/" + world_name)
    except FileExistsError:
        print("File already exist")
        overwrite = input("Do you want to overwrite it? y/n: ")
        if  overwrite == "n":
            print("Abort")
            return False
        elif overwrite == "y":
            shutil.rmtree("../worlds/" + world_name)
            os.makedirs("../worlds/" + world_name)

            #--------------------create model.sdf file--------------------
            create_sdf(author_name, author_email, default_description, world_name)

            #--------------------create model.config file--------------------
            create_config(world_name, world_length_m, world_height_m)

            return True
        else:
            print("bad option")
            return False

    print("New world!")
    #--------------------create model.sdf file--------------------
    create_sdf(author_name, author_email, default_description, world_name)

    #--------------------create model.config file--------------------
    create_config(world_name, world_length_m, world_height_m)

    return True

def export_map(world_name):
    os.system("cp -r ../worlds/" + str(world_name) + " ~/.gazebo/models/")
    os.system("cp -r ../random_world/media/ ~/.gazebo/models/" + str(world_name) + "/")
    print("map exported to:  ~/.gazebo/models/" + str(world_name))
    return

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

    parser.add_argument("-m","--mapid", help="Map Id", default="1")
    parser.add_argument("-c","--circlecount", help="Number of Circles", default="0")
    parser.add_argument("-s","--squarecount", help="Number of Squares", default="0")
    parser.add_argument("-r","--robotsize", help="Robot size (px*0.03898)", default="5")
    parser.add_argument("-x","--mapsizex", help="Map Size (x)", default="513")
    parser.add_argument("-y","--mapsizey", help="Map Size (y)", default="513")
    parser.add_argument("-cm","--mincircle", help="Min Circle Radius", default="0")
    parser.add_argument("-cmm","--maxcircle", help="Max Circle Radius", default="0")
    parser.add_argument("-sm","--minsquare", help="Min Square Size", default="0")
    parser.add_argument("-smm","--maxsquare", help="Max Circle Radius", default="0")
    parser.add_argument("--ramp", help="Add Ramp", default="0")
    parser.add_argument("--showmap", help="Show Map", default="0")

    args = parser.parse_args()


    os.system("../build/map_editor "+ \
    str(args.mapid) + " " +\
    str(args.circlecount) + " " +\
    str(args.squarecount) + " " +\
    str(args.robotsize) + " " +\
    str(args.mapsizex) + " " +\
    str(args.mapsizey) + " " +\
    str(args.mincircle) + " " +\
    str(args.maxcircle) + " " +\
    str(args.minsquare) + " " +\
    str(args.maxsquare) + " " +\
    str(args.ramp) + " " +\
    str(args.showmap)
    )

    map_name = "random_map" + str(args.mapid)
    exit_code = create_map(map_name, 20, 1)
    if  exit_code == True:
        export_map(map_name)



if __name__ == "__main__":
    main()

