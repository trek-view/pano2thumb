#!/usr/bin/python3
import cv2
import numpy as np
from scipy.spatial.transform import Rotation as R
import argparse

# coordinate definition:
# x: down, y: right

# latitude: rotate around global y
# longitude: rotate around global x
# do latitude rotation first

def sphericalFromCartesian(cartisian):
    pt_num = len(cartisian)
    sph = np.zeros([pt_num, 3])
    for i in range(pt_num):
        x = cartisian[i,0]
        y = cartisian[i,1]
        z = cartisian[i,2]

        # latitude [-pi, pi]
        # longitude [-pi, pi]
        # altitude [0, inf]

        sph[i,0] = np.arctan2(x, np.sqrt(z*z + y*y))
        sph[i,1] = np.arctan2(z,y)
        sph[i,2] = np.sqrt(x*x + y*y + z*z)

    return sph

def pixelDirection(lati, longi, resolution, focal_length, pixels):
    f_ = focal_length
    c_ = resolution * 0.5
    directions = np.zeros([len(pixels), 3])
    # print(directions.shape)
    rot_lati = R.from_rotvec(np.array([0,1,0]) * lati)
    rot_longi = R.from_rotvec(np.array([1,0,0]) * longi)
    for i in range(len(pixels)):
        px = pixels[i]
        directions[i,0] = (px[0] - c_[0]) / f_[0]
        directions[i,1] = (px[1] - c_[1]) / f_[1]
        directions[i,2] = 1

    ret = rot_longi.apply(rot_lati.apply(directions))
    return ret

def pixelCoordinateFromSpherical(sph, img_reso):
    pt_num = len(sph)
    ret = np.zeros([pt_num, 2])
    for i in range(pt_num):
        ret[i,0] = (sph[i, 0] + np.pi * 0.5) / (np.pi) * (img_reso[0] - 1)
        ret[i,1] = (sph[i, 1] + np.pi) / (np.pi * 2) * (img_reso[1] - 1)

    return ret

# def pixelCoordinateGeneration(resolution):
#     ret = np.ndarray(resolution[0] * )

def createParser():
    # initialize argparse options
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input_filename', help='specify the filename of the panoramic image', required=True)
    parser.add_argument('--longitude', dest='longitude', help='longitude of view', default='0')
    parser.add_argument('--latitude', dest='latitude', help='latitude of view', default='0')
    parser.add_argument('--output', dest='output_filename', help='specify the filename of the thumbnail image', default='output.png')
    parser.add_argument('--fov_width', dest='fov_width', help='field of view in width direction', default='60')
    parser.add_argument('--width', dest='width', help='width of thumbnail', default='200')
    parser.add_argument('--height', dest='height', help='height of thumbnail', default='200')

    return parser



if __name__ == "__main__":

    parser = createParser()
    args = parser.parse_args()

    img = cv2.imread(args.input_filename)

    print(img.shape)
    input_resolution = img.shape[0:2]
    # focal_length = np.array([float(args.focal_length)] * 2)
    output_resolution = np.array([int(args.height), int(args.width)])
    focal_length = float(args.width) / np.tan(0.5 * float(args.fov_width) * np.pi / 180.) * 0.5
    focal_length = [focal_length] * 2
    img_out = []

    output_px_coord = []

    for x in range(output_resolution[0]):
        for y in range(output_resolution[1]):
            output_px_coord.append([x,y])

    cam_latitude = float(args.latitude) * np.pi / 180 * -1
    cam_longitude = float(args.longitude) * np.pi / 180

    dirs = pixelDirection(cam_latitude, cam_longitude, output_resolution, focal_length, output_px_coord)
    sph_coord = sphericalFromCartesian(dirs)
    px_coord = pixelCoordinateFromSpherical(sph_coord, input_resolution)

    interpolated_pixel = np.ndarray([1, len(output_px_coord), img.shape[2]])
    for i in range(interpolated_pixel.shape[1]):
        interpolated_pixel[:,i,:] = cv2.remap(img, np.array([px_coord[i,1]* -1 + (img.shape[1] - 1)], np.float32), np.array([px_coord[i,0]], np.float32), cv2.INTER_LINEAR)
        # interpolated_pixel[:,i,:] = cv2.remap(img, np.array([px_coord[i,1]], np.float32), np.array([px_coord[i,0]], np.float32), cv2.INTER_LINEAR)

    img_out = interpolated_pixel.reshape([output_resolution[0], output_resolution[1], img.shape[2]])

    # print(dirs)
    output_filename = args.output_filename

    cv2.imwrite(output_filename, img_out)