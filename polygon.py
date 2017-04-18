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
<a-entity position="0 0 -1"
geometry="primitive: ring; radiusOuter: 0.015; radiusInner: 0.01;"
material="color: cyan; shader: flat" 
cursor="maxDistance: 30; fuse: true">
<!--a-animation begin="click" easing="ease-in" attribute="scale"
fill="backwards" from="0.1 0.1 0.1" to="1 1 1" dur="150"></a-animation-->
<!--a-animation begin="fusing" easing="ease-in" attribute="scale"
fill="forwards" from="1 1 1" to="0.1 0.1 0.1" dur="1500"></a-animation-->
<a-text align="center" color="black" wrap-count="200" value=""></a-text>
</a-entity>
<!--a-entity position="0.3 -0.1 -1" text="color: #01ff02; value: polar coords:;"></a-entity-->
</a-entity>
<a-entity position="8.420 1.11 5.40" rotation="0 242.000000 0" geometry="primitive: circle; radius: 0.3" material="opacity: 0.5" color="#CCC">
<a-animation begin="mouseenter" attribute="position" to="4.21 .55 2.7" dur="2000" fill="both"></a-animation>
<a-animation begin="mouseleave" attribute="position" to="8.420 1.11 5.40" dur="2000" fill="both"></a-animation>
<a-animation begin="mouseenter" attribute="material.opacity" to="0" dur="2000" fill="both"></a-animation>
<a-animation begin="mouseleave" attribute="material.opacity" to="0.3" dur="2000" fill="both"></a-animation>
<a-entity position="1.93 0 -0.06" geometry="primitive: plane; height: 1; width: 3" color="#DDD"></a-entity>
</a-entity>
</a-scene>
<script>
    var defaultCameraUserHeight; 
    function addRenderStartListener () {
        document.querySelector('a-scene').addEventListener('renderstart', function (evt) {
            var camera = evt.detail.target.camera.el.components.camera;
            setInterval(function () { 
                document.querySelector('a-text').setAttribute('value', 'Camera rotation: ' + JSON.stringify(camera.el.getAttribute('rotation'))); 
            }, 100);
        });
    }
    addRenderStartListener(); //document.body.addEventListener('DOMContentLoaded', addRenderStartListener);
</script>
</body>
</html>"""
