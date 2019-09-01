# SPR4 Robot

**Authors:** [Manuel Bernal]

SPR4 is an Open Source, LowCost four legged Robot based on the Raspberry Pi platform. 
It has arise as response of the necesity of cheap robotic platforms orientated to the development of IA, ML and RL algorithims.

SPR4 is the first final version of a series of prototipes, the SPR family. They all had 4 legs, and this model has two joints per leg, giving a total of 8 servo motors controlling the movement of this little quadruped. Designed in the spider mode, it has a very low price (150 USD) and brings lots of development oportunities.

<a href="https://www.youtube.com/embed/ufvPS5wJAx0" target="_blank"><img src="http://img.youtube.com/vi/ufvPS5wJAx0/0.jpg" 
alt="ORB-SLAM2" width="240" height="180" border="10" /></a>

# 1. License
SPR4 Software is released under a [GPLv3 license](https://https://github.com/TomBlackroad/SPR4/blob/master/LICENSE).

For a closed-source version of ORB-SLAM2 for commercial purposes, please contact the authors: 619901 (at) unizar (dot) es.

# 2. Prerequisites
We have tested the code in **Raspbian Buster Lite**, but it should be easy to compile in other platforms. The board installed in the robot is a Raspberry Pi 3 Model B, also B+ was tested with same results.

In order to use the code, a SPR4 Robot would be needed.

# 3. Building your own SPR4 Robot

Clone the repository:
```
git clone https://github.com/raulmur/ORB_SLAM2.git ORB_SLAM2
```

We provide a script `build.sh` to build the *Thirdparty* libraries and *ORB-SLAM2*. Please make sure you have installed all required dependencies (see section 2). Execute:
```
cd ORB_SLAM2
chmod +x build.sh
./build.sh
```

This will create **libORB_SLAM2.so**  at *lib* folder and the executables **mono_tum**, **mono_kitti**, **rgbd_tum**, **stereo_kitti**, **mono_euroc** and **stereo_euroc** in *Examples* folder.

# 4. Future Versions

## OpenCV
OpenCV is not used in this first version, nevertheless we are working to bring new functionalities based on this librery.

## ROS (optional)
Currently testing the code into the ROS structure, new version would have all the ROS capabilities ready to use. 

# 4. Comments

## Other Designs
New configuration for the SPR4 Legs are almost ready to come out. Four legged 3 joints SPR6 would be released very soon.
