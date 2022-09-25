# pano2thumb

Generates a Cartesian thumbnail from an equirectangular image
.
## Install

In a virtual environment:

```shell
python3 -m venv pano2thumb_venv
source pano2thumb_venv/bin/activate
pip3 install -r requirements.txt
```

## Run

```shell
python3 pano2thumb.py --input GSAS6231.JPG --width=1200 --height=900 --focal_length=100 --latitude=90 --longitude=90
```

Where 

* `input`: the equirectangular image you would like to get at thumbnail from
* `width`, `height`: the size of the desired thumbnail, in pixels
* `focal_length`: the zoom level of the photo
* `latitude`, `longitude`: the center of the thumbnail (when input image projected as a equirectangular), e.g. `--latitude=90 --longitude=0` is (zenith), and `--latitude=-90 --longitude=0` is south (nadir)

## Support

[Trek View are committed to providing best effort support via Slack](https://join.slack.com/t/trekview/shared_invite/zt-1gb4upchi-52pmWhPiwhFaAQqm0vWmJg).

If you notice a bug or have a feature request, [please submit them as issues on Github](https://github.com/trek-view/pano2thumb).

## License

[MIT LICENSE](/LICENSE).