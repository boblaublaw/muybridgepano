#/opt/local/bin/python

import math
import sys
i=0
n=13
r=10.0
verts=[]
while i != n:
    vert = [ r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n) ]
    i+=1
    verts.append(vert)

edges = {}
for i in xrange(1,len(verts)):
    edges[i] = [ verts[i-1],verts[i] ]
edges[0]=[ verts[n-1], verts[0] ]

def distance(p1, p2):
    dx=abs(p2[0] - p1[0])
    dy=abs(p2[1] - p1[1])
    return math.sqrt((dx * dx) + (dy * dy))

width=1.05 * distance(edges[0][0], edges[0][1])
# base the height on the aspect ratio of the source panels
height=width * 2558 / 1982
print """<a-scene>
    <a-assets>"""
for k,v in edges.iteritems():
    print '     <img id="empp%02d" src="http://sublimation.org/test/empp-%02d.jpg">' % (k, k)

print ' </a-assets>'
for k,v in edges.iteritems():
    print '<a-plane src="#empp%02d" position="%6f 0 %6f" rotation="0 %6f 0" width="%6f" height="%6f"></a-plane>' % (k, v[0][0], v[0][1], 325 - ((k + 1) * 360 / n), width, height) 
print """   <a-camera>
        <a-cursor>
        </a-cursor>
    </a-camera>
</a-scene>"""
