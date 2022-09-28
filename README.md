# pano2thumb

Generates a Cartesian thumbnail from an equirectangular image.

This script is a proof of concept for this blog post: https://www.trekview.org/blog/2022/create-thumbnail-from-equirectangular-image/

## Install

In a virtual environment:

```shell
python3 -m venv pano2thumb_venv
source pano2thumb_venv/bin/activate
pip3 install -r requirements.txt
```

## Run

```shell
python3 pano2thumb.py --input INPUT_EQUI_IMAGE.JPG --width=WIDTH_IN_PIXELS --height=HEIGHT_IN_PIXELS --fov=FIELD_OF_VIEW --latitude=LATITUDE --longitude=LONGITUDE
```

Where;

* `input`: the equirectangular image you would like to get at thumbnail from
* `width`, `height`: the size of the desired thumbnail, in pixels
* `latitude`, `longitude`: the center of the thumbnail (when input image projected as a equirectangular)
* `fov`: the field of view (angle of the camera), for example, if you set FOV in width direction to 60 degree, and width x length: 1000 x 500, then in width direction, the view angle is 60 degree, the view angle in height direction will be "about" 30 degree. smaller FOV makes you feel "zoom in"(larger focal length), while large FOV makes feel "zoom out" (smaller focal length)
* `help`: prints information on flags above in the command line

### Note, on `latitude`, `longitude`

In this script these values are relative to the camera (put another way; are not real lat/lon values).

To help you 

* `--latitude=90 --longitude=0` is up (zenith)
* `--latitude=-90 --longitude=0` is down (nadir)
* `--latitude=0 --longitude=-90` is forward
* `--latitude=0 --longitude=90` is backwards

## Examples

See `examples/` for output images.

### Facing forward

```shell
python3 pano2thumb.py --input GSAD6231.JPG --width=1200 --height=675 --fov=120 --latitude=0 --longitude=-90 --output GSAD6231-forward.JPG
```

### Facing back

```shell
python3 pano2thumb.py --input GSAD6231.JPG --width=1200 --height=675 --fov=120 --latitude=0 --longitude=90 --output GSAD6231-back.JPG
```

### Facing up

```shell
python3 pano2thumb.py --input GSAD6231.JPG --width=1200 --height=675 --fov=120 --latitude=90 --longitude=90 --output GSAD6231-up.JPG
```

### Facing down

```shell
python3 pano2thumb.py --input GSAD6231.JPG --width=1200 --height=675 --fov=120 --latitude=-90 --longitude=-90 --output GSAD6231-down.JPG
```

### Facing forward (zoom in)

```shell
python3 pano2thumb.py --input GSAD6231.JPG --width=1200 --height=675 --fov=100 --latitude=0 --longitude=-90 --output GSAD6231-forward-zoom-in.JPG
```

### Facing forward (zoom out)

```shell
python3 pano2thumb.py --input GSAD6231.JPG --width=1200 --height=675 --fov=140 --latitude=0 --longitude=-90 --output GSAD6231-forward-zoom-out.JPG
```

## Support

[Trek View are committed to providing best effort support via Slack](https://join.slack.com/t/trekview/shared_invite/zt-1gb4upchi-52pmWhPiwhFaAQqm0vWmJg).

If you notice a bug or have a feature request, [please submit them as issues on Github](https://github.com/trek-view/pano2thumb).

## License

[MIT LICENSE](/LICENSE).