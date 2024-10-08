
## Coordinates

There are four coordinates:
- **The world coordinates**
- **The camera coordinates**
- **The normalized coordinates:** The normalized coordinates can be seen as a point in the z=1 plane (the "normalized plane") in front of the camera [1, p. 81].
- **The pixel coordinates:** coordinate system o'-u-v fixed on the physical imaging plane. The origin o′ is in the upper left corner of the image, the u axis is parallel to the x axis, and the v axis is parallel to the y axis. We set the pixel
coordinates to scale α times on the u axis and β times on v. At the same time, the origin is translated by $[cx , cy ]^T$. [1, p. 79].


## Perspective projection

### Image plane

- In a camera, the image plane is ﬁxed at the surface of the sensor chip [2].
- In the perspective central projection model, the image plane is located at a distance f (focal length) from the camera plane.

![image](https://github.com/ManuelZ/camera-calibration/assets/115771/09f747da-70bc-4040-9115-d38fc13160cf)

Image from [2].


## Intrinsic matrix

```math 
Z \begin{pmatrix} u \\ v \\ 1 \end{pmatrix} = \begin{pmatrix} fx & 0 & cx \\ 0 & fy & cy \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} X \\ Y \\ Z \end{pmatrix} \overset{\Delta}{=} \boldsymbol{KP}
```

- Pixel plane: 0-u-v, fixed on the physical image plane.
- K: The camera’s inner parameter matrix (o intrinsics). It is generally assumed that the camera’s internal parameters are fixed after manufacturing and will not change during usage.
- fx, fy: focal length in pixels
- cx, cy: the principal point —the pixel coordinate of the point where the optical axis intersects the image plane with respect to the new origin— in pixels

##### Note: The focal length `f` is normally in meters, but it gets transformed into `fx` or `fy` when is multiplied by alpha or beta respectively, which are in pixels/meter.




## References
```
[1] {
  title = {14 Lectures on Visual SLAM: From Theory to Practice},
  subtitle={Fundamental Algorithms In MATLAB® Second, Completely Revised, Extended And Updated Edition}
  edition={2}
  publisher = {Publishing House of Electronics Industry},
  year = {2017},
  author = {Xiang Gao and Tao Zhang and Yi Liu and Qinrui Yan},
}

[2] {
  title = {Robotics, Vision and Control}
  publisher = {Springer Cham}
  year = {2017}
  author = {Peter Corke}
}
```
