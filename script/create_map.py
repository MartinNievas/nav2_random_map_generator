import os
import platform
import sys
import argparse



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

    parser.add_argument("-m","--mapid", help="Map Id", default="0")
    parser.add_argument("-c","--circlecount", help="Number of Circles", default="0")
    parser.add_argument("-s","--squarecount", help="Number of Squares", default="0")
    parser.add_argument("-r","--robotsize", help="Robot size (px*0.03898)", default="0")
    parser.add_argument("-x","--mapsizex", help="Map Size (x)", default="0")
    parser.add_argument("-y","--mapsizey", help="Map Size (y)", default="0")
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

if __name__ == "__main__":
    main()

