#/opt/local/bin/python

import math
import sys
i=0
n=13
r=10.0
verts=[]

def distance(p1, p2):
    dx=abs(p2[0] - p1[0])
    dy=abs(p2[1] - p1[1])
    return math.sqrt((dx * dx) + (dy * dy))

while i != n:
    vert = [ r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n) ]
    i+=1
    verts.append(vert)

edges = {}
for i in xrange(1,len(verts)):
    edges[i] = [ verts[i-1],verts[i] ]
edges[0]=[ verts[n-1], verts[0] ]

rots={}
for k,v in edges.iteritems():
    rots[k]=325 - ((k + 1) * 360 / n)

width=1.05 * distance(edges[0][0], edges[0][1])
# base the height on the aspect ratio of the source panels
height=width * 2558 / 1982
print """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Panorama</title>
<meta name="description" content="Eadward Muybridge Panorama">
<script src="http://aframe.io/releases/0.5.0/aframe.min.js"></script>
</head>
<body>
<a-scene>
<a-assets>"""
for k,v in edges.iteritems():
    print '<img id="empp%02d" src="http://sublimation.org/test/empp-%02d.jpg">' % (k, k)

print '</a-assets>'
for k,v in edges.iteritems():
    print '<a-plane src="#empp%02d" position="%6f 0 %6f" rotation="0 %6f 0" width="%6f" height="%6f"></a-plane>' % (k, v[0][0], v[0][1], rots[k], width, height)
print """<a-entity camera="userHeight: 0.0; zoom: 3" look-controls>
<a-entity position="0 0 -1" geometry="primitive: ring; radiusOuter: 0.015; radiusInner: 0.01;" material="color: cyan; shader: flat" cursor="maxDistance: 30; fuse: true">
  <a-text position="0 -0.25 0" align="center" color="yellow" wrap-count="300" value=""></a-text>
  <a-plane position="0 -0.255 -0.01" scale="0.3 0.04 0" color="black"></a-plane>
</a-entity>
<!--a-entity position="0.3 -0.1 -1" text="color: #01ff02; value: polar coords:;"></a-entity-->
</a-entity>
<a-entity position="8.420 1.11 5.40" rotation="0 242.000000 0" geometry="primitive: circle; radius: 0.3" material="opacity: 0.5" color="grey">
  <a-animation begin="mouseenter" attribute="position" to="4.21 .55 2.7" delay="100" dur="500" fill="forward"></a-animation>
  <a-animation begin="mouseenter" attribute="material.opacity" to="0" delay="0" dur="100" fill="forward"></a-animation>
  <a-animation begin="mouseleave" attribute="material.opacity" to="0.3" delay="1000" dur="2000" fill="backward"></a-animation>
  <a-animation begin="mouseleave" attribute="position" to="8.420 1.11 5.40" delay="1500" dur="500" fill="backward"></a-animation>
  <a-entity position="0.09 -0.37 -0.39" geometry="primitive: plane; height: 0.5; width: 1.5" color="lightgrey">
    <a-text position="0 0 0" align="center" wrap-count="100" value="This is a spite wall!" color="black"></a-entity>
  </a-entity>
</a-entity>
</a-scene>
<script>
    function addRenderStartListener () {
        document.querySelector('a-scene').addEventListener('renderstart', function (evt) {
            var camera = evt.detail.target.camera.el.components.camera;
            setInterval(function () {
                var rot = camera.el.getAttribute('rotation');
                var msg = 'Cam: ' + rot['x'].toFixed(2) + ',' + rot['y'].toFixed(2);
                document.querySelector('a-text').setAttribute('value', msg);
            }, 100);
        });
    }
    addRenderStartListener();
</script>
</body>
</html>"""
