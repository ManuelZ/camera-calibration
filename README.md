

## Intrinsic matrix

```math 
Z \begin{pmatrix} u \\ v \\ 1 \end{pmatrix} = \begin{pmatrix} fx & 0 & cx \\ 0 & fy & cy \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} X \\ Y \\ Z \end{pmatrix} \overset{\Delta}{=} \boldsymbol{KP}
```
- K: The camera’s inner parameter matrix (o intrinsics). It is generally assumed that the camera’s internal parameters are fixed after manufacturing and will not change during usage.
- fx, fy: focal length in pixels
- cx, cy: the principal point —the pixel coordinate of the point where the optial axis intersects the image plane with respect to the new origin— in pixels


### Coordinates
There are four coordinates:
- the world coordinates
- the camera coordinates
- the normalized coordinates
- the pixel coordinates


## References
```
{
  title = {14 Lectures on Visual SLAM: From Theory to Practice},
  publisher = {Publishing House of Electronics Industry},
  year = {2017},
  author = {Xiang Gao and Tao Zhang and Yi Liu and Qinrui Yan},
}
```
